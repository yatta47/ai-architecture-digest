---
type: announcement
title: Amazon Bedrock AgentCoreのWeb Searchにドメイン/公開日フィルタを追加
title_original: Domain and publish date filters for Web Search on AgentCore
industry: cross-industry
cloud:
- aws
patterns:
- rag
- policy-as-code
- guardrails
components:
- Amazon Bedrock AgentCore
- AgentCore Gateway
- Web Search
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/domain-and-publish-date-filters-for-web-search-on-agentcore/
published_at: '2026-08-19'
---

## 概要

Amazon Bedrock AgentCoreのWeb Searchコネクタv1.2.0は、エージェントの検索結果をドメインと公開日でリクエスト単位に絞り込めるサーバーサイドのランタイムフィルタリングを追加した。管理者が設定するドメインポリシーとランタイムフィルタは、includeが積集合・excludeが和集合で合成される多層モデルになっており、ランタイム側はスコープを狭めることしかできない。あわせてEU（ダブリン）・APAC（東京）へリージョンを拡大し、データ近接性要件のある規制業種向けにゼロエグレスのアクセス経路を提供する。

## 設計のポイント

- 管理者レベルのドメインポリシーとリクエスト単位のランタイムフィルタを重ねる二層モデルにし、ランタイム側はスコープを狭めることしかできないよう設計してガバナンスを常に優先する
- includeリストは積集合、excludeリストは和集合で合成することで、許可は保守的に・拒否は積極的に効かせる
- フィルタが有効な場合はドメインや公開日を検証できない結果を除外し、再現率よりも精度を優先する
- 検索クエリがAWS内に留まるゼロエグレスアーキテクチャを維持したまま、EU・APACのリージョナルエンドポイントを追加してデータ近接性要件に対応する

## 使いどころ

- コンプライアンスエージェントが.govドメインや承認済み発行元のみを参照する必要がある規制業種
- 『今週の決算発表』のように鮮度が重要で、古い四半期の情報を混入させたくない市場インテリジェンスエージェント
- マルチテナントプラットフォームでテナントごとに異なるドメインポリシーをリクエスト単位で適用したい場合
