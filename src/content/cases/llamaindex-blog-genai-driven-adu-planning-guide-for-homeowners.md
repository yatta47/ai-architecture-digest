---
type: case
title: 衛星画像と建築条例PDFから離れの建設計画を支援する生成AIアプリ
title_original: GenAI-driven ADU Planning
industry: other
cloud: []
patterns:
- ai-agent
- rag
- document-processing
components:
- GPT-3.5
- GPT-4V
- LlamaIndex
- LlamaParse
- Chroma
- Google Maps
- React
- Flask
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/pioneering-the-future-of-housing-introducing-genai-driven-adu-planning-ea950be71e2f
published_at: '2024-02-12'
---

## 概要

ハッカソン優勝作のADU Plannerは、住所から衛星画像を取得してGPT-4Vで建設可能領域を判定し、条例PDFをRAGで解析する。条件に合う間取りを地元業者サイトから探して重ねて表示する。

## 設計のポイント

- 画像解析（敷地）と文書解析（条例）を別経路に分けて結果を突き合わせる。
- 自治体ごとの条例索引をエージェントのツールとして持たせる。

## 使いどころ

- 敷地と規制の事前調査を自動化したい建設・不動産事業者。
- 画像と法令文書を組み合わせるアプリの開発者。
