---
type: guidance
title: AgentCoreメモリのライフサイクル管理アーキテクチャ
title_original: Designing lifecycle policies for AgentCore memory
industry: cross-industry
cloud:
- aws
patterns:
- memory-consolidation
- ai-agent
components:
- Amazon Bedrock AgentCore
- AWS Step Functions
- Amazon Bedrock
- AWS CDK
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/designing-lifecycle-policies-for-agentcore-memory/
published_at: '2026-09-04'
---

## 概要

AIエージェントのメモリを放置すると古い文脈をそのまま参照してしまう問題に対し、TTL失効・関連度スコアによる剪定・意味記憶への統合という3つのライフサイクルポリシーを組み合わせ、AWS Step FunctionsとAmazon Bedrockで夜間バッチとして運用するアーキテクチャを紹介する。

## 設計のポイント

- TTLベースの失効・関連度スコアによる剪定・意味記憶への統合という3つの補完的なポリシーを組み合わせる
- エピソード記憶は短期で失効させ、意味記憶や手続き記憶はより長く保持するなど記憶の種類ごとに保持期間を変える
- 関連度スコアは作成からの経過日数・最終アクセスからの経過日数・アクセス頻度を重み付けした指数減衰で算出し、しきい値未満を統合/削除候補にする

## 使いどころ

- 長期間稼働し会話量の多いカスタマーサポートやITヘルプデスクなど、記憶が肥大化しやすいエージェントの運用担当者
- GDPRなどのコンプライアンス要件で記憶の保持期間管理が必要な場合
- 個人アシスタントのような低頻度利用エージェントでまずTTL失効だけから始めたい場合
