---
type: announcement
title: OpenDocRouter：文書パース用の各種モデルを1つのAPIで
title_original: 'Introducing OpenDocRouter: every document model under one API'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- multi-model-routing
- eval
components:
- OpenDocRouter
- LlamaParse
- ParseBench
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-opendocrouter
published_at: '2026-10-07'
---

## 概要

LlamaIndexは、OSSとフロンティアのOCR/文書モデルを、版管理されたレシピとともに統一APIで使えるOpenDocRouterを公開した。独自のグラウンディング機能で全モデルに同じレイアウトクラスとバウンディングボックスを与え、ParseBenchで品質とコストを評価する。

## 設計のポイント

- モデルごとのプロンプト・レート制限・デプロイを共通APIで吸収する
- グラウンディング層で出力形式を揃える
- 全モデルをベンチマークし、品質とコストで選べるようにする

## 使いどころ

- 文書パースのモデルを比較して切り替えたいチーム
- RAG用の文書取り込み基盤
