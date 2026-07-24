---
type: announcement
title: 'LlamaIndexニュースレター: Parse-FlowとGranular Bounding Boxes'
title_original: LlamaIndex Newsletter 6-10-26
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaParse
- Parse-Flow
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-6-10-26
published_at: '2026-07-18'
---

## 概要

LlamaIndexは、Parse・Classify・Split・Extractの4プリミティブをドラッグ&ドロップで組めるオープンソースのビジュアルワークフローツールParse-Flowを発表。LlamaParseには抽出値ごとに単語・行・セル単位の座標を返すGranular Bounding Boxesを追加し、コンプライアンス監査向けの追跡性を高めた。

## 設計のポイント

- Parse/Classify/Split/Extractという4つの原子的処理単位を組み合わせてワークフローを構築できるようにする
- 抽出結果に元文書上の座標(バウンディングボックス)を付与し監査証跡を確保する設計

## 使いどころ

- ノーコードで文書処理ワークフローを組みたいチーム
- 抽出データの根拠を文書中の位置までトレースする必要があるコンプライアンス業務
