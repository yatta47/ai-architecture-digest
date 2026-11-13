---
type: guidance
title: 統制と観測を各段に組み込むエンタープライズAIエージェント参照アーキテクチャ
title_original: 'Inside an enterprise AI agent: A governed, observable loop architecture'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- guardrails
- defense-in-depth
- context-engineering
components:
- Amazon Bedrock
- API Gateway
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/inside-an-enterprise-ai-agent-a-governed-observable-loop-architecture/
published_at: '2026-11-12'
---

## 概要

エンタープライズAIエージェントの参照アーキテクチャを、APIゲートウェイ、5フェーズのエージェントランタイム、知識・状態層、プラットフォームサービス、横断のトラスト制御の5層で示す。各層をAWSマネージドサービスに対応づけ、よくある失敗も紹介する。

## 設計のポイント

- 理解・計画・検索・推論・実行/観測の5フェーズでループを構成する。
- ガバナンスと観測を各ステップに置く。
- ID・ポリシー処理はAPIゲートウェイ層に集約する。

## 使いどころ

- チャットボットから目標駆動のエージェントへ移行する企業。
- エージェントの統制設計をレビューする担当者。
