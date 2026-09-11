---
type: announcement
title: 業務を横断して仕事を代行するエンタープライズAIアシスタント
title_original: Amazon Quick is now generally available on desktop
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- human-in-the-loop
components:
- Amazon Quick
- Amazon CloudWatch
- AWS CloudTrail
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-quick-is-now-generally-available-on-desktop/
published_at: '2026-09-10'
---

## 概要

Amazon Quickのデスクトップ版がmacOS/Windowsで一般提供開始。メール・カレンダー・CRM・メッセージングを横断したアクティビティフィードでエージェントが定型作業を裏で処理し、人は判断が必要な項目だけに集中できる。データはユーザーの環境内に留まり、HIPAA/FedRAMP/SOC2/ISO27001等の監査証跡・コンプライアンス要件を満たす。

## 設計のポイント

- エージェントが自律解決した項目はフィードから消し、人が判断すべき項目だけを残す優先度付けの仕組みを持つ
- 既存の業務システム(メール・CRM・カレンダー等)にそのまま接続し、移行を必要としないインテグレーション設計にする
- CloudWatch/CloudTrailによる監査証跡とHIPAA/FedRAMP等のコンプライアンス認証を組み込みで提供する

## 使いどころ

- 数万人規模の従業員を抱え、部門横断でエージェント運用を進めたい企業のIT部門
- 会議準備やフォローアップなど定型的な情報収集作業を減らしたい営業・アカウント担当
