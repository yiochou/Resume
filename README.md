<!-- The (first) h1 will be used as the <title> of the HTML page -->
# 周易佑 Yio

<!-- The unordered list immediately after the h1 will be formatted on a single
line. It is intended to be used for contact details -->
- <span>🏡</span> [yiochou.com](http://yiochou.com)
- <span>✉️</span> <hi@yiochou.com>
- <span>📱</span>0927309966

<!-- The paragraph after the h1 and ul and before the first h2 is optional. It
is intended to be used for a short summary. -->

---

## Summary 

- 3 年的軟體開發經驗，主要使用的語言為 NodeJS 與 Golang，NodeJS 有扎實的實戰工作經驗，Golang 做過個人的 Side Project。
- 攥寫程式碼時，注重可維護性及可閱讀性，並以 SOLID 的觀念下去設計。
- 在資料庫上 RDB 及 NoSQL 都使用過，根據其特性設計對應 Schema，並依據需求建立合理的 Index。
- 有 GCP, K8S 的經驗，部署應用到 K8S 上，並建立監控系統，主動通知異常發生。
- 會寫前端，使用 React/Redux 在實戰上，前端人力不足時能夠支援。

---

## Work Experience

<!-- You have to wrap the "left" and "right" half of these headings in spans by
hand -->
### <span> SoundOn 聲浪科技 </span> 2020/7 - 2021/7
##### Backend Developer
##### Tech: NodeJS, PostgresSQL, GCP, K8S, BigQuery, Dataflow, CircleCI, Firebase, React

  - 開發 SoundOn Podcast Hosting / SoundOn Player 的後端需求，規劃後實作並優化既有程式碼。
  - 檢測分析 SQL，並加上合理的 Index 優化過慢的 Query。
  - 部署應用到 GKE (K8S)，並在 GCP 上建立監控系統，整合 Slack 後主動通知異常事件發生。
  - 使用 Google Dataflow 建立 ETL Job 來處理/分析資料，並在 Google Data Studio 做視覺化報表，供其他部門分析與下判斷。
  - 在無 downtime 的目標下，移除原先使用的 Firestore (NoSQL)，而改用 Postgres 作為 DB，一致化資料格式後，搬移舊資料。
  - 開發 7 天上線的 SoundClub 專案 (類似 Clubhouse)。
  - 支援前端 (React, Redux, 設定 Prerender), App 端 (Flutter)。
  
### <span> LJIT 利頡資訊 </span> 2018/5 - 2020/2
##### Backend Developer
##### Tech: NodeJS, Express.js, MongoDB, MySQL, Redis, AWS S3, React/Redux, Webpack, Docker

  - 為專案公司，所以接觸到的技術多元，從前端一路接觸到後端，而後專職後端開發。
  - 積極參加公司內讀書會，並分享過 SOLID, React/Redux, Database Transaction/Isolation ... 
  - 參與過的專案：
    - Dapp 遊戲(類似資金盤)：修改智能合約並部署到以太坊，前端使用 React, Redux 開發，並用 web3 與部署的智能合約溝通，最後以 Webpack 打包應用。
    - 影音平台：開發前端與後端，根據需求規劃及討論 DB Schema，並使用 AWS S3 儲存影音檔案，加上 CDN 加速影片的讀取速度，也實作了以 HMAC Token 認證的演算機制。
    - 博弈專案：開發各式彩票開獎演算法，用 Jest 寫單元測試，並寫腳本方便把 csv 的資料轉成 test cases，節省團隊攥寫測試的時間。負責實作認證(登入)系統，包含二階段驗證。

---
## Education
### <span> 國立中央大學 資訊工程系 </span> 2013/9 - 2017/7
##### Major in **Computer Science**.
### <span> 國立彰化高中 </span> 2010/9 - 2013/7

---

## Skills
 - Programming Languages: Javascript(NodeJS, TypeScript), Golang
 - Database: MySQL, PostgresSQL, MongoDB, Firestore, Redis
 - Infra: GCP(GKE, BigQuery, Dataflow, CloudRun), AWS S3, K8S, Terraform, CircleCI
 - Frontend Framework: React, Redux, JQuery
 - Other: Git, Docker, Firebase, OneSignal, BullMQ, MailGun, TapPay, SOLID
