---
type: guidance
title: 'AzureのAI基盤入門: Work IQ・Fabric IQ・Foundry IQでエージェントに組織文脈を接地させる'
title_original: Get started with AI architecture design
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- rag
- context-engineering
components:
- Microsoft Foundry
- Azure OpenAI
- Azure Machine Learning
- Microsoft Copilot Studio
- Foundry Tools
- Microsoft Fabric
- Azure AI Search
- Azure Databricks
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/ai-get-started
published_at: '2026-07-02'
---

## 概要

Microsoft FoundryやAzure Machine Learning、Copilot StudioなどAzureのAI開発プラットフォーム群を俯瞰し、Work IQ（M365の業務シグナル）・Fabric IQ（構造化データ）・Foundry IQ（マルチソースのナレッジ）という3層のエンタープライズインテリジェンスレイヤーでAIエージェントに組織文脈を与える設計思想を紹介する入門ガイド。あわせて、App Gateway＋WAF・プライベートエンドポイント・Foundry Agent Serviceを組み合わせたベースラインAIチャットアーキテクチャの参照実装も示す。

## 設計のポイント

- Work IQ（M365シグナル）・Fabric IQ（構造化データ）・Foundry IQ（マルチソースナレッジ）という3層にコンテキストの出所を分離し、RAGの応答をこの3層に接地させることで、単発プロンプトでなく組織の実際の業務文脈にAIを根付かせる。
- 本番想定のベースライン構成では、App Gateway＋WAFを唯一の公開エントリポイントにし、Foundry・Azure OpenAI・AI SearchなどのバックエンドはすべてプライベートエンドポイントとマネージドIDで接続してパブリック露出を避ける。
- Foundry Agent Serviceはマネージドアイデンティティ経由でFoundryプロジェクトからAzure OpenAIにアクセスする構成とし、エージェント実行基盤と推論基盤の権限を分離する。

## 使いどころ

- 自社のAI基盤をゼロから設計するアーキテクトが、Foundry・Azure ML・Copilot Studio・Fabricなど各サービスをどの用途に使うべきか最初に俯瞰したい場合。
- RAGエージェントの回答を社内のメール・チャットや構造化KPIなど複数ソースに正確に接地させたい場合。
- セキュリティ・ガバナンス要件が厳しいエンタープライズが、プライベートネットワーク前提のAIチャットアーキテクチャ参照実装を探している場合。
