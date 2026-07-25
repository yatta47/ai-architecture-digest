---
type: opinion
title: OCRベンチマークOmniDocBenchは飽和している、次に必要な評価軸とは
title_original: OmniDocBench Is Saturated. What's Next for OCR Benchmarks?
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- eval
- document-processing
components:
- OmniDocBench
- GLM-OCR
- PaddleOCR-VL
- LlamaParse
- Gemini 3 Pro
- GPT-5.2
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/omnidocbench-is-saturated-what-s-next-for-ocr-benchmarks
published_at: '2026-07-19'
---

## 概要

GLM-OCRなど最新モデルがOmniDocBench v1.5で94%を超えるスコアを出し始めたことを受け、同ベンチマークは対象文書の種類が限定的で飽和しつつあり、さらに単一の正解表現に対する完全一致評価が意味的に正しい別表現(HTML表とMarkdown表など)を不当に減点していると指摘する。AIエージェント時代には形式の一致よりも意味的な正しさを評価する新しいベンチマークが必要だと論じる。

## 設計のポイント

- ベンチマークのカバレッジ(9文書種・1355ページ)が実世界の複雑な金融資料・保険金請求・法務文書を十分に代表していないと分析した
- 編集距離やTEDSのような連続指標は句読点や改行など無害な差分まで罰してしまうため、意味的に正しい多様な出力を不当に不利にする
- エージェントが実際に気にするのは表の行列の対応関係や図表の解釈精度であり、出力フォーマットの完全一致ではないという評価基準の転換を提案した

## 使いどころ

- 文書パーサー/OCRモデルをベンチマークスコアだけで選定しようとしている開発者への注意喚起
- 新しい評価指標や評価データセットの設計を検討している研究者・ベンダー
