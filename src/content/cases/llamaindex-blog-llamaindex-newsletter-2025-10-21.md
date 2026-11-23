---
type: announcement
title: llamactlとWorkflow Debugger、オープンモデルによるText-to-SQL（LlamaIndexニュースレター 2025-10-21）
title_original: LlamaIndex Newsletter 2025-10-21
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- text-to-sql
- llmops
- event-driven
components:
- llamactl
- LlamaAgents
- Workflow Debugger
- Arctic Text-to-SQL
- Apache Kafka
- Docker
- MongoDB
- LlamaParse
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-10-21
published_at: '2025-10-21'
---

## 概要

LlamaAgentsをローカルで開発・提供するCLIのllamactlと、イベントログ表示や実行比較ができるWorkflow Debuggerを紹介している。セマンティックなテーブル検索とArctic Text-to-SQLモデルでSQLを生成する手法や、KafkaとDockerでマイクロサービスをワークフロー制御する例もある。

## 設計のポイント

- ローカルで開発してからクラウドにデプロイする流れでエージェントの反復を速める。
- 実行イベントを可視化・比較できるデバッガで挙動を検証する。
- テーブルを意味検索で絞り込んでからSQLを生成し、エラー処理を組み込む。

## 使いどころ

- 社内DBへの自然言語問い合わせを実装するチーム。
- 保険や金融でエージェントを導入するアナリストや運用担当。
