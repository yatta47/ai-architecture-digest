---
type: guidance
title: APIゲートウェイでFoundry Models(Azure OpenAI)の高度な監視を実現する設計指針
title_original: Implement advanced monitoring for Foundry Models through a gateway
industry: cross-industry
cloud:
- azure
patterns:
- llm-gateway
- llmops
- guardrails
components:
- Foundry Models
- Azure OpenAI
- Azure API Management
- Microsoft Entra ID
- Azure Monitor
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/azure-openai-gateway-monitoring
published_at: '2026-07-02'
---

## 概要

Azure OpenAI(Foundry Models)のネイティブ監視だけでは、クライアント/モデル単位の使用量追跡によるチャージバック、モデル入出力の監査、准リアルタイム監視といった生成AIワークロード特有の要件を満たせない。この記事はAPIゲートウェイ(Azure API Management等)を前段に挟むことで、クライアントIPやEntra ID、テナント識別子を一元的に記録し、KQLクエリで使用量やプロンプト内容を分析できるようにする設計を解説している。

## 設計のポイント

- Azure OpenAI単体のテレメトリはクライアントIPアドレスの末尾がマスクされるため、ゲートウェイ層でクライアントの完全なIPやMicrosoft Entra ID、カスタムのテナント/アプリ識別子を記録し、部門・顧客単位のチャージバック集計を可能にする。
- 複数リージョンのAzure OpenAIインスタンスがそれぞれ別のAzure Monitorインスタンスにログを送る分断を、ゲートウェイに使用量ログを集約させることで解消する。
- ApiManagementGatewayLogsテーブルに対するKQLクエリでモデル別・IP別のプロンプト/completionトークン数を集計し、コストとモデル性能を結び付けて分析できるようにする。
- モデルの入力と出力の両方を監査対象とし、脅威検出・利用規約違反検出・キャッシュ由来かモデル生成かの判別など、複数の監査ユースケースに同じログ基盤を再利用する。

## 使いどころ

- 複数部門・複数顧客にAzure OpenAI利用料をチャージバックし、予算策定やコスト対効果分析を行いたい組織。
- 生成AIワークロードで脅威検出や不適切利用(利用規約違反)の監査が求められる規制業種。
- 複数リージョン・複数Azure OpenAIインスタンスにまたがる使用量を一元的に把握したいエンタープライズ基盤チーム。
