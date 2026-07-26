---
type: guidance
title: エージェント型AIシステムの設計パターン選定ガイド：単一エージェントかマルチエージェントか
title_original: Choose a design pattern for your agentic AI system
industry: cross-industry
cloud:
- gcp
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
components: []
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
published_at: '2026-07-19'
---

## 概要

Google Cloudは、タスクの特性・レイテンシ要件・コスト・人間関与の必要性という観点からエージェント型AIの設計パターンを選ぶ指針を提供する。単一エージェントから始め、ツール数やタスクの複雑さが増した場合にReActなどの改善やマルチエージェント化を検討する段階的アプローチを推奨する。

## 設計のポイント

- 定型的・高構造なタスクや単一のモデル呼び出しで完結するタスクには非エージェント型ソリューションの方がコスト効率が良い
- 開発初期は単一エージェントから始め、プロンプト・ツール定義などコアロジックを磨き込んでから複雑なアーキテクチャに拡張する
- 単一エージェントのツール数増加や複雑化に伴う精度低下・レイテンシ増大にはReActパターンでまず対処し、それでも不十分な場合にマルチエージェント化する
- マルチエージェント化では大きな目標を専門化されたサブタスクに分解し、各エージェントへのコンテキスト供給（コンテキストエンジニアリング）を設計する

## 使いどころ

- エージェントアーキテクチャを単一かマルチかで迷っているチーム
- レイテンシ・コスト・精度のトレードオフを踏まえて設計パターンを選定したいアーキテクト
