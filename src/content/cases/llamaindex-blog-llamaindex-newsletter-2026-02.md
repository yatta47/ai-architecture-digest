---
type: announcement
title: 'LlamaIndexニュースレター: LlamaCloudをLlamaParseに改称、推論モデルはOCRで逆効果と分析'
title_original: LlamaIndex Newsletter 2026-02-24
company: LlamaIndex
industry: cross-industry
cloud:
- gcp
patterns:
- document-processing
- eval
components:
- LlamaParse
- LlamaExtract
- Gemini 3.1 Pro
- LlamaAgent Workflows
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2026-02-24
published_at: '2026-07-19'
---

## 概要

LlamaIndexはエンタープライズ基盤『LlamaCloud』を、文書パースとエージェント型ワークフローに焦点を絞った『LlamaParse』へ改称した。あわせて、推論レベルを上げてもGPT-5.2の文書パース精度は向上せずコストとレイテンシだけが増大し、LlamaParse Agenticが18倍低コストで上回るという分析や、LlamaExtractのページ単位の引用機能を紹介している。

## 設計のポイント

- 製品名を実態(エージェント型文書処理プラットフォーム)に合わせて改称し、フレームワークではなく文書インフラとしての位置づけを明確化した
- 推論トークンを増やすことが必ずしも文書パース精度に効かないという知見を公開ベンチマークで示した

## 使いどころ

- 数百万件規模のファイルを多形式でパース・検索する必要があるAIエージェントパイプライン運用チーム
- OCR/文書パースのモデル選定でコストと精度のトレードオフを判断したい開発者
