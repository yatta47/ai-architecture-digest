---
type: announcement
title: Amazon Quick Appsで承認済みデータをリアルタイム照会するLive Data in Apps
title_original: Serve live, governed data in AI-built apps with Amazon Quick
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- text-to-sql
- guardrails
components:
- Amazon Quick
- Quick Apps
- Amazon Quick Sight
- SPICE
- Direct Query
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/serve-live-governed-data-in-ai-built-apps-with-amazon-quick/
published_at: '2026-10-01'
---

## 概要

自然言語でアプリを生成するAmazon Quick Appsに、ガバナンス済みのQuick Sightデータセットを閲覧時にライブ照会するLive Data in Appsが追加された。エージェントが関連データセットを探してSQLを書き、公開後は閲覧のたびに同じSQLを閲覧者権限で実行するため、行・列レベルのセキュリティが自動で効く。データセット単位の同意とサーバー側での強制も備える。

## 設計のポイント

- ビルド時の数値の固定をやめ、閲覧時に同じSQLを再実行して常に最新の値を返す。
- クエリを閲覧者本人の権限で実行し、既存のRLS/CLSをそのまま適用する。
- ビルダーと閲覧者それぞれがデータセット単位で同意し、同意をサーバー側で毎回検証する。
- 匿名・公開アクセスは認めず、認証済みユーザーに限定する。

## 使いどころ

- 営業リーダーが更改案件と収益データを組み合わせた業務アプリをIT待ちなしで作りたいとき。
- 日次・週次のレポート作成と共有を、閲覧するだけで最新になるアプリに置き換えたいとき。
- 権限モデルを増やさずに社内データをアプリ公開したいデータ管理者。
