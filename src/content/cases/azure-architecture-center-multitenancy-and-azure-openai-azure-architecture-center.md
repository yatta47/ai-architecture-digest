---
type: guidance
title: マルチテナントSaaSにおけるAzure OpenAIのテナント分離設計
title_original: Multitenancy and Azure OpenAI
industry: cross-industry
cloud:
- azure
patterns:
- multi-tenant-rag
- llmops
- cost-optimization
components:
- Azure OpenAI
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/openai
published_at: '2026-02-05'
---

## 概要

Azure OpenAIを複数テナントで利用するSaaSにおいて、専用インスタンス・共有インスタンス上の専用/共有モデルデプロイ・テナント提供インスタンスという4つの分離モデルをデータ分離度、性能分離度、運用複雑さの観点で比較する。テナント数やコンプライアンス要件、ファインチューニングの要否、モデルバージョン管理の必要性に応じて適切なモデルを選ぶ指針を示す。

## 設計のポイント

- テナント数・コンプライアンス要件・ファインチューニング要否・モデルライフサイクル要件に応じて専用/共有/テナント提供インスタンスを選定する
- 共有インスタンスではTPMクォータ枯渇やnoisy neighbor問題に備え、アプリ側でテナントごとのトークン使用量を追跡する仕組みを実装する
- ファインチューニング済みモデルを利用するテナントには共有インスタンスを使わせず、専用のモデルデプロイを割り当てる
- モデルデプロイ単位でコンテンツフィルタリングポリシーやデータレジデンシー要件、PTU割当を設定し、テナントへのアクセス制御はアプリケーション側で強制する

## 使いどころ

- 複数テナントに生成AI機能を提供するAzure OpenAIベースのSaaS事業者
- テナントごとに異なるデータレジデンシーやコンプライアンス要件がある場合の分離設計判断
- テナント単位のコスト配分やクォータ管理を厳密に行いたいマルチテナントプラットフォーム
