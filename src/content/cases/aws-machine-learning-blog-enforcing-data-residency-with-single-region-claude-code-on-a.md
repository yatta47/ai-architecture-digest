---
type: guidance
title: Claude CodeをAmazon Bedrock上で単一リージョンに固定し、データレジデンシー要件を満たす構成
title_original: Enforcing data residency with single-Region Claude Code on Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- data-residency
- llmops
- guardrails
components:
- Claude Code
- Amazon Bedrock
- Amazon Bedrock Mantle
- AWS IAM
- AWS CloudTrail
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/enforcing-data-residency-with-single-region-claude-code-on-amazon-bedrock/
published_at: '2026-08-06'
---

## 概要

推論処理そのものを特定リージョン内に留めたいという厳格なデータレジデンシー要件に対し、Amazon Bedrock上のClaude Codeを単一リージョンに固定する2つの経路（クラシックInvoke API＋アプリケーション推論プロファイル、またはMantleのAWS_REGION指定）を整理。どちらの経路でもIAMのRegion条件で強制し、CloudTrailで遵守を検証する。

## 設計のポイント

- 『どこかEUなら良い』のような地理要件はクロスリージョン推論のままでよく、単一リージョン固定は特定リージョン限定の要件のときだけ使う
- エンドポイント（クラシックBedrockかMantleか）によって単一リージョン化の手段とリージョン対応範囲が異なるため、対象リージョンから逆算して経路を選ぶ
- aws:RequestedRegion条件を持つIAMポリシーをクライアント側の環境変数設定と組み合わせ、開発者の設定ミスがあってもIAM側で拒否させる
- CloudTrailログを遵守確認の一次情報とし、承認された経路以外でのモデル呼び出しがないことを検証する

## 使いどころ

- コンプライアンス部門が『呼び出し元』ではなく『推論処理そのもの』のリージョン内保持を求める規制業界の開発チームとして
- Claude Codeなどコーディングエージェントを国際展開する企業が、拠点ごとのデータ主権要件に対応する場合として
- IAMポリシーとCloudTrailだけで技術的に遵守を強制・監査したいセキュリティチームのリファレンスとして
