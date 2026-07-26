---
type: case
title: AI SDRのオンボーディングをLlamaParseで自動化し立ち上げ期間を数日に短縮
title_original: 'Building smarter AI SDRs with LlamaParse: How 11x AI shrinks ramp time to days'
company: 11x
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
components:
- LlamaParse
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-smarter-ai-sdrs-with-llamaparse-how-11x-ai-shrinks-ramp-time-to-days
published_at: '2026-07-19'
---

## 概要

11xは営業アウトバウンドを自動化するAI SDR「Alice」のオンボーディングにおいて、PDF・PPT・通話録音など多様な非構造化資料を取り込む必要があった。自前OCR＋Mistralの組み合わせでは品質・保守コストの課題があったため、LlamaParseを採用しマルチモーダル文書からのコンテキスト抽出を自動化した。

## 設計のポイント

- 自前OCRパイプラインの内製ではなく、マルチモーダル文書解析に特化したLlamaParseを採用して開発・保守コストを削減する
- 共有ドライブに資料を投入するだけで人間の新人SDRオンボーディングに近い体験をエージェントに再現させる

## 使いどころ

- 画像・テキスト・図表・音声など多様な形式の資料からAIエージェント向けにコンテキストを自動生成したい場合
- 顧客数百〜数千規模のオンボーディングを人手のドキュメント整理なしにスケールさせたい営業/CSチーム
