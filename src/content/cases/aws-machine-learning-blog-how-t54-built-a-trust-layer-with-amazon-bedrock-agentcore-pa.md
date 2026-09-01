---
type: case
title: エージェント自律決済に信頼スコアリングの決定的ゲートを組み込んだ支払い基盤
title_original: How t54 built a trust layer with Amazon Bedrock AgentCore payments
company: t54
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- guardrails
- decision-execution
- defense-in-depth
components:
- Amazon Bedrock AgentCore
- AWS IAM
- AWS Secrets Manager
- Amazon CloudWatch
- x402
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments/
published_at: '2026-09-01'
---

## 概要

t54は、AIエージェントが自律的に第三者サービスへ支払う際のリスクを抑えるため、Amazon Bedrock AgentCore paymentsのセッション単位の支出上限・資格情報隔離と、独自のリアルタイム信頼スコアリング(x402-secure)を組み合わせた決済基盤を構築した。支払い実行前に必ず信頼チェックを通す決定的ゲートを設け、2000万件超のマイクロペイメントを人手承認なしで処理している。

## 設計のポイント

- 支払いを実行する主体と支出上限を設定する主体を役割分離し、エージェント自身が自分の上限を変更できないようにする
- 信頼スコアのチェックをモデルへの提案でなくコード上の決定的ゲートにし、モデルがそれを迂回できないようにする
- 単一の弱いシグナルだけで決済を許可しないよう、複数の独立したリスクシグナルを合成して判定する
- エージェントにはセッションスコープのトークンのみ渡し、秘密鍵や資格情報そのものには触れさせない

## 使いどころ

- AIエージェントに実際の決済権限を持たせたいが暴走リスクを許容できないプロダクトチーム
- 高頻度・低単価のマイクロペイメントで人手承認が現実的でないユースケース
- 金融規制下でエージェントの支出統制と監査証跡を求められる組織
