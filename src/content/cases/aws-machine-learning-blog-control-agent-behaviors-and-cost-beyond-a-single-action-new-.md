---
type: announcement
title: AgentCoreに時系列ポリシーとレート制限を追加、エージェントの一連の行動を統制
title_original: 'Control agent behaviors and cost beyond a single action: new capabilities in Amazon Bedrock AgentCore'
industry: cross-industry
cloud:
- aws
patterns:
- guardrails
- policy-as-code
- cost-optimization
components:
- Amazon Bedrock AgentCore
- Dogwood
- Amazon Bedrock AgentCore Gateway
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/
published_at: '2026-08-06'
---

## 概要

Amazon Bedrock AgentCoreに、単発の呼び出しではなくセッション全体の行動シーケンスを審査する「時系列ポリシー」と、ゲートウェイでのレート制限機能が追加された。個々の呼び出しは正当でも積み重なると危険・高コストになるパターン（分割送金、予算超過、再試行の暴走など）をゲートウェイ層で決定的にブロックできる。ポリシーエンジンはOSSの新言語Dogwoodで記述し、Apache 2.0で公開されている。

## 設計のポイント

- セキュリティ制御をアプリコードではなくゲートウェイ層に集約し、全エージェント・全呼び出しに一律適用する
- 個々のリクエストではなくセッション内の行動シーケンス（それまでの呼び出し履歴）を状態として評価する時系列ポリシーを導入する
- リクエスト数・トークン数・接続保持時間の3指標を秒/分単位のウィンドウで制限し、消費パターンの違う暴走（リトライ・重い推論・張り付き接続）を漏れなく捕捉する
- ポリシーはdeny-by-defaultかつ全判定をログ化し、エージェントからは判定ロジックが見えない設計にすることで説明責任を担保する

## 使いどころ

- 自律性の高いマルチステップエージェントに、口座間送金や購買のような『積み重なると危険』な操作をさせる場合のガードレールとして
- エージェントのトークン・リクエスト消費を組織のコスト上限内に収めたいプラットフォームチームの予算統制として
- セキュリティ承認者がエージェント運用の可否を判断する際の、監査可能な決定的コントロールとして
