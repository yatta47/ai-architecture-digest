---
type: announcement
title: 'LlamaIndexニュースレター: vibe-llama docuflowsと永続ワークフロー'
title_original: LlamaIndex Newsletter 2025-09-02
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- document-processing
- context-engineering
- memory-consolidation
components:
- vibe-llama
- LlamaExtract
- SemTools
- LlamaIndex Workflows
- Cursor
- Claude Code
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-09-02
published_at: '2025-09-02'
---

## 概要

LlamaIndexの週次ニュースレター。自然言語から文書処理ワークフローを生成するvibe-llama v0.3.0のdocuflows、ワークフローを複数回の実行にまたがって保持する3つの永続化方式、LlamaExtractのスキーマ自動生成を紹介している。

## 設計のポイント

- コーディングエージェントに最新のAPI文脈を注入し、古いAPIの提案を防ぐ。
- インスタンス保存・Contextの状態ストア・外部チェックポイントでワークフロー状態を永続化する。
- プロンプトと例ファイルから抽出スキーマを推論させ、手作業の定義を省く。

## 使いどころ

- 長時間動く文書処理や多段のエージェントを運用する開発者。
- CursorやClaude CodeでLlamaIndexアプリを作る人。
