---
type: guidance
title: 非推論・推論エージェント・ディープリサーチの3段階で使い分けるWeb検索統合
title_original: Web search
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
components:
- Responses API
- gpt-5.5
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/tools-web-search
published_at: '2025-08-14'
---

## 概要

OpenAIモデルに最新のWeb情報と出典付き回答を与えるWeb検索ツールを、非推論の即時検索・推論モデルによるエージェント的検索・バックグラウンド実行前提のディープリサーチという3段階のユースケースに分けて解説する。

## 設計のポイント

- レイテンシ重視の単純検索と、精度重視で反復検索するエージェント的検索を明確に使い分ける
- 数百ソースを横断する長時間のディープリサーチはバックグラウンドモードと組み合わせて実行する
- 推論レベル(reasoning effort)を調整することで検索の深さとレイテンシのトレードオフを制御する

## 使いどころ

- 最新情報や出典付き回答が必要なチャットボット・検索アシスタントの開発者
- 数百件のソースを横断調査する必要があるリサーチ・分析ワークロード
