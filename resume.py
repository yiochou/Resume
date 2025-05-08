#!/usr/bin/env python3
import argparse
import itertools
import logging
import os
import sys
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

preamble = """\
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<div id="resume">
"""

postamble = """\
</div>
</body>
</html>
"""

CHROME_GUESSES_MACOS = (
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
)

# https://stackoverflow.com/a/40674915/409879
CHROME_GUESSES_WINDOWS = (
    # Windows 10
    os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
    os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
    os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
    # Windows 7
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    # Vista
    r"C:\Users\UserName\AppDataLocal\Google\Chrome",
    # XP
    r"C:\Documents and Settings\UserName\Local Settings\Application Data\Google\Chrome",
)

# https://unix.stackexchange.com/a/439956/20079
CHROME_GUESSES_LINUX = [
    "/".join((path, executable))
    for path, executable in itertools.product(
        (
            "/usr/local/sbin",
            "/usr/local/bin",
            "/usr/sbin",
            "/usr/bin",
            "/sbin",
            "/bin",
            "/opt/google/chrome",
        ),
        ("google-chrome", "chrome", "chromium", "chromium-browser"),
    )
]


def guess_chrome_path() -> str:
    if sys.platform == "darwin":
        guesses = CHROME_GUESSES_MACOS
    elif sys.platform == "win32":
        guesses = CHROME_GUESSES_WINDOWS
    else:
        guesses = CHROME_GUESSES_LINUX
    for guess in guesses:
        if os.path.exists(guess):
            logging.info("Found Chrome or Chromium at " + guess)
            return guess
    raise ValueError("Could not find Chrome. Please set CHROME_PATH.")


def title(md: str) -> str:
    """
    Return the contents of the first markdown heading in md, which we
    assume to be the title of the document.
    """
    for line in md.splitlines():
        if line[0] == "#":
            return line.strip("#").strip()
    raise ValueError("Cannot find any lines that look like markdown headings")


def make_html(md: str) -> str:
    """
    Compile md to HTML and prepend/append preamble/postamble.

    Insert resume.css if it exists.
    """
    try:
        with open("resume.css") as cssfp:
            css = cssfp.read()
    except FileNotFoundError:
        print("resume.css not found. Output will by unstyled.")
        css = ""
    return "".join(
        (
            preamble.format(title="Yio's Resume", css=css),
            markdown.markdown(md, extensions=["smarty"]),
            postamble,
        )
    )


def export_pdf_from_html(html_path: str, pdf_path: str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        html_file = Path(html_path).resolve().as_uri()
        page.goto(html_file)

        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            display_header_footer=False,
        )

        browser.close()

        logging.info(f"Wrote {pdf_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help="markdown input file [README.md]",
        default="README.md",
        nargs="?",
    )
    parser.add_argument(
        "--no-html",
        help="Do not write html output",
        action="store_true",
    )
    parser.add_argument(
        "--no-pdf",
        help="Do not write pdf output",
        action="store_true",
    )
    parser.add_argument(
        "--chrome-path",
        help="Path to Chrome or Chromium executable",
    )
    parser.add_argument("-q", "--quiet", action="store_true")
    args = parser.parse_args()

    if args.quiet:
        logging.basicConfig(level=logging.WARN, format="%(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(message)s")

    prefix = "index"
    outputFolder = "dist"

    with open(args.file, encoding="utf-8") as mdfp:
        md = mdfp.read()
    html = make_html(md)

    if not args.no_html:
        with open(
            outputFolder + "/" + prefix + ".html", "w", encoding="utf-8"
        ) as htmlfp:
            htmlfp.write(html)
            logging.info(f"Wrote {htmlfp.name}")

    if not args.no_pdf:
        export_pdf_from_html("dist/index.html", "dist/index.pdf")
