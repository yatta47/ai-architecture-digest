---
type: announcement
title: LangSmith BYOCがAWS・Azure・GCPに対応
title_original: LangSmith BYOC is now available on AWS, Azure, and Google Cloud
company: LangChain
industry: cross-industry
cloud:
- aws
- azure
- gcp
- multi-cloud
patterns:
- llmops
- defense-in-depth
components:
- LangSmith
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-byoc-aws-gc-azure
published_at: '2026-11-04'
---

## 概要

LangSmithのBYOCがAWS（GA）、Azure・Google Cloud（Beta）で使えるようになった。コントロールプレーンはLangChainが運用し、トレースや評価、データセット、デプロイを含むデータプレーンは顧客のクラウドアカウントに置く。

## 設計のポイント

- 認証や課金メタデータと機微データのプレーンを分離する。
- リージョン・環境・事業部ごとに複数のデータプレーンを持てる。
- アップグレードとスケールは提供側に任せ、セルフホストの保守負担を減らす。

## 使いどころ

- コンプライアンス上、トレースを自社境界に置きたいが運用は減らしたいとき。
- 複数クラウドにまたがるエージェント基盤。
