---
type: announcement
title: エージェントの承認を分類器で自動判定するSmart Approvals
title_original: 'Smart Approvals in Amazon Quick: Human oversight where it matters'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- human-in-the-loop
- guardrails
- defense-in-depth
components:
- Amazon Quick
- AWS CloudTrail
- Amazon CloudWatch Logs
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/smart-approvals-in-amazon-quick-human-oversight-where-it-matters/
published_at: '2026-11-04'
---

## 概要

Amazon Quick のSmart Approvalsは、ポリシー上承認対象となる操作を別モデル（分類器）がユーザー依頼と照合し、自動承認するか人に差し戻すかを判定する機能。権限の付与や必須承認の解除はせず、承認疲れを減らしつつ重要な判断に人の注意を残す。

## 設計のポイント

- ポリシー（Custom Permissions・Guardrails・コネクタ権限）で適格性を先に決め、拒否や必須承認は分類器で覆さない。
- 自動承認は単一利用で、審査した操作とパラメータにのみ有効にする。
- 分類器は判断、権限サービスは強制と役割を分け、機微な操作はコネクタ権限で必ず人に回す。
- CloudTrailとチャットログで承認の経緯を追跡できるようにする。

## 使いどころ

- 承認プロンプトが多発するエージェント業務で承認疲れを減らしたいとき。
- 間接プロンプトインジェクション対策として依頼との整合を検査したいとき。
- 特定チームでパイロット導入し、段階的に自動化範囲を広げたいとき。
