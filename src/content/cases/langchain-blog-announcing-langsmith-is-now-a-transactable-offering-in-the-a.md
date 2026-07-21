---
type: announcement
title: LangSmith、Azure Marketplaceで購入可能な顧客VPC内完結デプロイに対応
title_original: Announcing LangSmith is now a transactable offering in the Azure Marketplace
industry: cross-industry
cloud:
- azure
patterns:
- llmops
components:
- LangSmith
- Azure Kubernetes Service
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/announcing-langsmith-is-now-a-transactable-offering-in-the-azure-marketplace
published_at: '2026-06-15'
---

## 概要

LangSmithがAzure MarketplaceでAzure Kubernetesアプリケーションとして購入可能になり、顧客のAzure VPC内に完全デプロイしてデータを外部に出さない構成が取れるようになった。Moody'sなどの既存顧客が言及するように、金融・インフォセック要件の厳しい企業でも導入しやすい調達経路を提供する。

## 設計のポイント

- 顧客のAzure VPC内にLangSmithをフルデプロイし、データを外部に出さない構成でセキュリティ・コンプライアンス要件を満たす
- Azure Marketplaceのトランザクション対応により、MACC消化や調達プロセスを簡略化する

## 使いどころ

- データ主権やインフォセック要件が厳しい企業でLLM観測基盤を自社VPC内に閉じたい場合
- Azureの既存契約(MACC)を使ってLLMツールの調達を進めたい場合
