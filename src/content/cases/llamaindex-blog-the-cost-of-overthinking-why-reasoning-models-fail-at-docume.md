---
type: case
title: '推論を強めるほど文書パース精度が下がる: GPT-5.2の思考レベル別ベンチマーク実験'
title_original: 'The Cost of Overthinking: Why Reasoning Models Fail at Document Parsing'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- inference-optimization
- eval
components:
- GPT-5.2
- LlamaParse Agentic
- OmniDocBench
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/the-cost-of-overthinking-why-reasoning-models-fail-at-document-parsing
published_at: '2026-07-19'
---

## 概要

OmniDocBenchから抽出した難易度の高い文書40件をGPT-5.2の推論レベル(Zero/Low/High/xHigh)ごとに処理させたところ、精度は約0.79前後でほぼ変化しない一方、レイテンシとコストは5〜8倍に増加し、専用パーサーのLlamaParse Agenticが精度0.821・コスト0.013ドルと全推論レベルを上回った。高い推論は表を誤って分割したり、実在しない値で空欄を補完したりする『見えないものを推論で補おうとする』失敗を招くことも示した。

## 設計のポイント

- 文書パースは『何が書かれているか』を転写する作業であり、モデルの意味理解(推論)を強めるとかえって原文への忠実性を損なうと整理した
- 推論トークンはビジョンエンコーダが取りこぼした情報(小さい・密な・縦書きの文字)を復元できないため、精度低下の根本原因はエンコード段階にあると特定した
- 単一パスの汎用モデルに全工程を任せるのではなく、専用OCRでピクセルを正確に読む工程とLLMが構造化する工程を分離するパイプライン設計を採用した

## 使いどころ

- 推論モデルの『考えさせれば精度が上がる』という前提を文書パースに適用する前に検証したいチーム
- OCR/文書抽出のコストとレイテンシを最適化したいプラットフォームエンジニア
