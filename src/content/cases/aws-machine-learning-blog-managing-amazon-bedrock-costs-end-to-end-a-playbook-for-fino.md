---
type: guidance
title: Amazon Bedrockのコストを帰属・観測・統制する5段階FinOps運用モデル
title_original: 'Managing Amazon Bedrock costs end to end: A playbook for FinOps and platform teams'
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- llm-gateway
- llmops
components:
- Amazon Bedrock
- AWS Cost and Usage Report 2.0
- AWS Cost Explorer
- AWS IAM
- AWS STS
- AWS Billing
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/managing-amazon-bedrock-costs-end-to-end-a-playbook-for-finops-and-platform-teams/
published_at: '2026-10-30'
---

## 概要

エージェント型ワークロードではトークン消費が自律度とコンテキストサイズに比例して増えるため、コスト管理はアーキテクチャと運用の課題になる。本記事はAttribute→Observe→Enforce→Optimize→Operateの5段階ループで、Bedrockの費用を所有者に紐づけ予算で統制する方法を示す。

## 設計のポイント

- IAMプリンシパル単位のコスト帰属をCUR 2.0とコスト配分タグで有効化し、請求書レベルでチーム・アプリ別に集計する。
- LLMゲートウェイが単一ロールで呼ぶと帰属が失われるため、ユーザーごとにロールをAssumeしセッション名とタグを渡して認証情報を1時間キャッシュする。
- アプリ構成に応じてアプリケーション推論プロファイル(固定的な構成向け)とProjects(モデル変更が多い構成向け)を使い分ける。
- モデルルーティング・キャッシュ・トークン上限などの既定値をプラットフォーム側で最適化し、各チームの注意に頼らない。

## 使いどころ

- 生成AIの利用が拡大しチーム別の費用説明を求められるFinOps担当者。
- 共有LLMゲートウェイを運営し、ユーザー/テナント別のチャージバックを実現したいプラットフォームチーム。
- エージェント型ワークロードの予算超過を早期検知・遮断したい組織。
