---
type: announcement
title: コーディングエージェントをSageMaker推論最適化の専門家にするaws-ai-mlスキル
title_original: 'New agent skill: Amazon SageMaker optimized generative AI inference for your coding agent'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- inference-optimization
- spec-driven-development
components:
- Amazon SageMaker AI
- Agent Toolkit for AWS
- Model Context Protocol
- Kiro
- Claude Code
- SageMaker Python SDK v3
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/new-agent-skill-amazon-sagemaker-optimized-generative-ai-inference-for-your-coding-agent/
published_at: '2026-10-05'
---

## 概要

SageMaker AIの最適化生成AI推論向けに、Kiro・Claude Code・Codexなどが使えるaws-ai-mlスキルが提供開始された。エンドポイントのベンチマーク、構成の推奨、実行結果の比較、SageMaker Python SDK v3コードの生成をエージェントが代行する。

## 設計のポイント

- MCP対応の既存エージェントにスキルとして知識を後付けし、専用UIを作らずに専門性を拡張する。
- 実測ベンチマークに基づいて構成を提案し、結果を読める実行可能コードとして出力して人が確認できる状態を保つ。
- 目的・性能目標・コスト上限などを聞き返してから構成を決める、ソリューションアーキテクト的な対話にする。

## 使いどころ

- 最適なインスタンスやサービングコンテナを選べていないMLエンジニア。
- 本番投入前にモデルの性能とコストを比較検証したいチーム。
