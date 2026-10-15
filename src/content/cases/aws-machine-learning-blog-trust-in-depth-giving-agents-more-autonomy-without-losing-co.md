---
type: guidance
title: エージェントの自律性を層状の検証で広げる Trust in Depth
title_original: 'Trust in Depth: Giving agents more autonomy without losing control'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- defense-in-depth
- guardrails
- policy-as-code
- human-in-the-loop
components:
- Amazon Bedrock AgentCore
- Kiro
- Strands
- AWS IAM
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/trust-in-depth-giving-agents-more-autonomy-without-losing-control/
published_at: '2026-10-15'
---

## 概要

AWSがエージェントに自律性を与えつつ統制を保つ考え方「Trust in Depth」を提示した。Scope・Know・Bound・Observeの4つの問いを実行ライフサイクルの各時点に置き、検証可能な部分は自動推論で証明し、曖昧な部分は人に回す。

## 設計のポイント

- 実行前に権限・ツール・禁止事項を絞り込む（スコープ設計に最も労力をかける）
- 厳密に書けるルールは自動推論で全経路を検証し、書けないものは評価と人の判断に回す
- エージェントごとに固有のIDを持たせ、行動の都度検証する
- 実行後にトレースから行動と理由を再構成して学習に回す

## 使いどころ

- 金融取引など誤動作の影響が大きい業務にエージェントを導入する企業
- 人手承認のレビュー疲れを減らしたいガバナンス担当
