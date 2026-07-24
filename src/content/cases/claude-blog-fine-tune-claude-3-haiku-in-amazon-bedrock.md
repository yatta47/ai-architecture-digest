---
type: announcement
title: Amazon BedrockでのClaude 3 Haikuファインチューニング
title_original: Fine-tune Claude 3 Haiku in Amazon Bedrock
company: Anthropic
industry: cross-industry
cloud:
- aws
patterns:
- fine-tuning
- cost-optimization
components:
- Claude 3 Haiku
- Amazon Bedrock
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/fine-tune-claude-3-haiku
published_at: '2024-07-10'
---

## 概要

Amazon Bedrock上でClaude 3 Haikuをカスタムデータでファインチューニングできるようにした。プロンプト・コンプリーションのペアを用意し、業務特化のタスクに対してSonnetやOpusを使わずとも高精度かつ低コスト・低レイテンシで動作するカスタムモデルを作成できる。

## 設計のポイント

- 教師データとして高品質なプロンプト-コンプリーションペアを用意し、ドメイン固有知識をモデルへ転写する
- 学習データはAWS環境内に留まる設計とし、独自データがモデル学習に再利用されないことを保証する

## 使いどころ

- 分類や独自API連携など業種固有タスクの精度を上げつつコストを抑えたい場合
- 定型フォーマットでの出力を安定させ規制対応のレポート生成などを行いたい場合
