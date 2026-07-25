---
type: announcement
title: 'LlamaIndexニュースレター: LlamaSheetsやLlamaAgentsなど週次アップデートまとめ'
title_original: LlamaIndex Newsletter 11-25-25
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- multi-agent-orchestration
components:
- LlamaSheets
- LlamaAgents
- LlamaParse
- LlamaExtract
- Gemini 3 Pro
- OpenTelemetry
- Jaeger
- llamactl
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-11-25
published_at: '2026-07-19'
---

## 概要

LlamaIndexの週次ニュースレターで、乱れたスプレッドシートを構造化するLlamaSheetsのベータ公開、ドキュメントエージェントを構築・提供・デプロイするLlamaAgentsのオープンプレビュー、Gemini 3 Proのデイゼロ統合、Agent WorkflowsのOpenTelemetry可観測性対応など複数の新機能をまとめて紹介している。

## 設計のポイント

- LlamaSheetsは40以上のセル特徴量を用いたクラスタリングで表構造を検出し、乱れた表計算シートを型付きParquetに正規化する
- LlamaAgentsはLlamaParseの文書処理とAgent Workflowsのオーケストレーションを統合し、CLI(llamactl)でローカル実行とクラウドデプロイを一括管理する
- Agent WorkflowsにOpenTelemetry/Jaegerによる分散トレーシングを組み込み、多段階ドキュメントパイプラインの可観測性を確保する

## 使いどころ

- 複雑な書式のスプレッドシートをAIエージェントで扱えるデータに変換したいチーム
- 文書分類・抽出・レビューを含む多段階のドキュメントエージェントを素早く構築・デプロイしたい開発者
