---
type: announcement
title: 行・単語・セル単位まで追跡できるLlamaParseの詳細バウンディングボックス
title_original: Announcing Granular Bounding Boxes in LlamaParse
industry: financial-services
cloud: []
patterns:
- document-processing
- guardrails
components:
- LlamaParse
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/announcing-granular-bounding-boxes-in-llamaparse
published_at: '2026-07-18'
---

## 概要

従来の粗いレイアウトレベルのバウンディングボックスでは、1行に多数の数値が密集する財務報告書などで引用元の特定ができなかった。LlamaParseは行・単語・セルの3段階の粒度で座標を返せるようになり、監査グレードの引用表示や単語単位の高精度なPII redactionを可能にした。

## 設計のポイント

- 座標付与の対象をページ上に実在するテキストに限定し、推論やAI要約による再構成コンテンツには座標を付けない
- output_optionsのgranular_bboxesパラメータでオプトインとし、既存ワークフローへの影響を最小化する
- 属性精度が重要なワークフローではAgentic Plusティアで追加の検証ラウンドを実行する

## 使いどころ

- 監査担当者が抽出値の出典をピクセル単位で確認する必要があるコンプライアンスレビュー
- PII/機密情報を単語単位で正確にマスキングしたいredactionツール
