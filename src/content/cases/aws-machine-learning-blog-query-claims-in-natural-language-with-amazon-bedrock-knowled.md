---
type: guidance
title: 保険請求書類を自然言語で横断検索し引用付きで回答する請求アシスタント
title_original: Query claims in natural language with Amazon Bedrock Knowledge Bases
industry: financial-services
cloud:
- aws
patterns:
- rag
- document-processing
- guardrails
- ai-agent
components:
- Amazon Bedrock Knowledge Bases
- Amazon Bedrock
- AgenticRetrieveStream API
- Amazon Bedrock Guardrails
- Amazon S3
- Boto3
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/query-claims-in-natural-language-with-amazon-bedrock-knowledge-bases/
published_at: '2026-09-30'
---

## 概要

査定日誌・見積書・警察報告書・支払台帳など散在する保険請求書類をAmazon S3からBedrock Knowledge Basesに取り込み、自然言語の質問に引用付きで回答する請求アシスタントの構築手順を解説する。AgenticRetrieveStream APIが複合質問をサブクエリに分解して証拠が揃うまで検索を繰り返し、コンテキストグラウンディングのガードレールで根拠のない回答をブロックする。合成データを用いたハウツーで、本番顧客事例ではない。

## 設計のポイント

- 各文書に同名の.metadata.jsonサイドカーを置き、claim_idや種別・金額・提出日などで検索範囲をメタデータフィルタで絞り込む。
- エージェント型検索で複合質問をサブクエリに分解し、maxAgentIterationの上限内で証拠が十分か確認してから回答を生成する。
- 規制対応のため全回答に出典引用を付け、トレースイベントで検索計画を公開して監督者が監査できるようにする。
- コンテキストグラウンディングチェックで取得記録に裏付けのない回答を遮断する。

## 使いどころ

- 契約者からの請求ステータス問い合わせに平易な言葉で即答したいコンタクトセンター。
- 金額・期間・種別など複数条件で未決案件を横断把握したい損害査定担当者。
- PDF・Word・テキストなど形式がばらばらで改訂や取消が混在する記録から有効な情報を特定したい規制業界の業務。
