---
type: guidance
title: Foundry Modelsへの直接アクセスとゲートウェイ経由アクセスをWell-Architectedの5本柱で比較
title_original: Access Foundry Models and other language models through a gateway
industry: cross-industry
cloud:
- azure
patterns:
- llm-gateway
- multi-model-routing
- cost-optimization
components:
- Microsoft Foundry
- Foundry Models
- Microsoft Agent Framework
- Semantic Kernel
- LangChain
- Foundry Agent Service
- Microsoft Entra ID
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/azure-openai-gateway-guide
published_at: '2026-07-02'
---

## 概要

Microsoft FoundryのモデルAPIをクライアントやオーケストレーター(Agent Framework、Semantic Kernel、LangChainなど)に直接公開した場合に生じる課題を、Azure Well-Architected Frameworkの信頼性・セキュリティ・コスト最適化などの観点から整理する記事。特定のゲートウェイ実装ではなく、いつ・なぜリバースプロキシ型ゲートウェイを挟むべきかというアーキテクチャ判断の指針に焦点を当てている。

## 設計のポイント

- Global/Data Zoneデプロイはそれ自体がスロットリング緩和や容量融通というゲートウェイ的な機能を内包するため、独自ゲートウェイを構築する前にまずこれらのデプロイ形態の採用を検討する。
- フェイルオーバーやスケールアウトの切替ロジックをクライアント任せにすると、変更のロールアウトが複数クライアントにまたがり展開リスクが増すため、ゲートウェイ側にロジックを集約して一括で制御する。
- Foundryの認証はリソース/プロジェクト単位でしかスコープできないため、モデルデプロイ単位で最小権限やクライアントごとの識別を強制したい場合はゲートウェイでアクセス制御を肩代わりする。
- Global/Data Zoneデプロイは保存データのリージョンを保証するが推論処理は他リージョンに及びうるため、データ主権要件があるワークロードではゲートウェイでリージョンアフィニティを制御する設計を検討する。

## 使いどころ

- 複数のFoundryリソースやモデルデプロイを横断してフェイルオーバーやスロットリング回避を行いたいエンタープライズワークロード。
- Microsoft Entraテナント外のクライアントに単一のAPIキーを共有させず、安全にモデルへアクセスさせたい場合。
- 部門や顧客ごとにAzure OpenAI/Foundryの利用コストをチャージバック・showbackしたいマルチテナント組織。
