---
type: guidance
title: コンテキストエンジニアリング4層とDeep Insightの実装
title_original: 'Four layers of context engineering for production AI agents: How Deep Insight applies them in working code'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- context-engineering
- multi-agent-orchestration
- ai-agent
components:
- Strands Agents SDK
- Amazon Bedrock AgentCore
- Amazon Bedrock
- Claude Sonnet 4.5
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/four-layers-of-context-engineering-for-production-ai-agents-how-deep-insight-applies-them-in-working-code/
published_at: '2026-11-04'
---

## 概要

本番AIエージェントのコンテキスト逼迫に対し、アーキテクチャでの分離・プロンプトでの制御・ファイルシステムへの外部化・独立エージェントによる検証の4層を整理し、OSSのDeep Insightで実装を示す。書き込みと実行を一体化したツールで約95%、スキルのオンデマンド読み込みでシステムプロンプトを約97%削減したとする。

## 設計のポイント

- サブエージェントでコンテキストを分離し、親の窓を肥大させない。
- スクリプトの書き込みと実行を1ツールにまとめ、1回あたりのトークン追加を減らす。
- スキルを必要時にだけ読み込み、システムプロンプトを小さく保つ。
- 中間成果をファイルに外部化し、独立エージェントで検証する。

## 使いどころ

- データ分析やレポート生成など長時間タスクのエージェントで窓あふれが起きるとき。
- マルチエージェント構成のトークンコストを下げたいとき。
- Strands AgentsとAgentCoreで本番化を進める開発チーム。
