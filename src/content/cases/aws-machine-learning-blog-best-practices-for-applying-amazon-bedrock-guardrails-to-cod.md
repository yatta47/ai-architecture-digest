---
type: guidance
title: コード生成ワークフローへのAmazon Bedrock Guardrails適用のベストプラクティス
title_original: Best practices for applying Amazon Bedrock Guardrails to code generation workflows
industry: cross-industry
cloud:
- aws
patterns:
- guardrails
- inference-optimization
components:
- Amazon Bedrock Guardrails
- Claude Code
- Kiro
- OpenAI Codex
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/best-practices-for-applying-amazon-bedrock-guardrails-to-code-generation-workflows/
published_at: '2026-07-23'
---

## 概要

会話向けに設計されたガードレール評価パターンをそのままコード生成ワークフローに適用すると、ストリーミング出力の多さと同時セッション数によりスロットリングやコスト増を招く。テキストユニット(1000文字×有効セーフガード数で乗算的に消費)の仕組みを理解し、コード生成向けのアーキテクチャパターンに調整する必要がある。

## 設計のポイント

- ガードレール消費は「文字数×有効なセーフガードポリシー数」で乗算的に増えるため、コード生成の長大な出力では会話用の既定設定がそのまま破綻要因になる
- コンテンツフィルタは有効カテゴリ数によらずポリシー単位で1テキストユニットとして課金される点を踏まえて設計する
- ストリーミング中の逐次評価(50文字ごとの評価など)ではなく、まとまった単位での評価に切り替えてAPI呼び出し数を削減する

## 使いどころ

- Claude CodeやKiroなどAIコーディングアシスタントを組織全体に展開しガードレールを適用したいチーム
- 複数開発者が同時にエージェントループを回す高スループットなコード生成基盤のキャパシティプランニング
