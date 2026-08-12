---
type: case
title: 検証可能なAIエージェント決済基盤(Amazon Bedrock AgentCore Payments)
title_original: 'Pay with confidence: How Solv Labs built verifiable, auditable agent payments on Amazon Bedrock AgentCore
  payments'
company: Solv Labs
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- policy-as-code
- guardrails
- confidential-computing
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock AgentCore payments
- AWS Nitro Enclaves
- AWS Automated Reasoning Checks
- Coinbase
- x402
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/pay-with-confidence-how-solv-labs-built-verifiable-auditable-agent-payments-on-amazon-bedrock-agentcore-payments/
published_at: '2026-08-12'
---

## 概要

Solv LabsはICME Labsと組み、AIエージェントが実際に送金する決済ワークフローをAmazon Bedrock AgentCore Payments上に構築した。ORACLEによる事前認可、Nitro Enclaveでの完全性アテステーション、取引ごとのリスク価格付けを経て4秒未満でCoinbase経由のオンチェーン決済を完了し、監査可能な証跡を残す。

## 設計のポイント

- 決済実行前にORACLEでALLOW/REVIEW判定を行い、ポリシー違反の取引がそもそも確定しない順序にした。
- ICME PreFlightでポリシー適合の証明を生成し、ポリシー内容や取引パラメータを開示せず第三者検証を可能にした。
- AWS Nitro Enclave内で実行記録に署名しPCR測定値と紐づけることで、事後の改ざんを防ぐハードウェアアテステーションを組み込んだ。
- リスクエンジンで取引ごとに動的なリスク乗数を算出し、一律の合否ではなく取引単位の価格付けと優先度付けレビューを可能にした。

## 使いどころ

- 自律エージェントが実際に送金・決済を行う金融・決済領域で、監査証跡と説明責任が求められる企業。
- 規制業界でエージェントの行動を事後に検証可能な形で残す必要があるコンプライアンス担当者。
- 運用者・監査人・カウンターパーティ間で取引の正当性を独立検証したいシステム設計者。
