---
type: guidance
title: 劣化スキャンの法務ディスカバリー文書をマルチモーダル解析で検索可能にする手引き
title_original: 'Parsing the Unreadable: How LlamaParse Handles Legal Discovery Documents'
industry: legal
cloud: []
patterns:
- document-processing
- rag
components:
- LlamaParse
- LlamaCloud
- Relativity
- Everlaw
- DISCO
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/parsing-the-unreadable-how-llamaparse-handles-legal-discovery-documents
published_at: '2026-07-18'
---

## 概要

訴訟のディスカバリー（証拠開示）では、相手方から渡されるのは低解像度・白黒・傾き付きの大量スキャン文書で、従来のOCRと正規表現検索では取りこぼしが多い。LlamaParseはビジョン（マルチモーダル）モデルでページの視覚レイアウトを解釈し、劣化スキャンからも構造化テキストを抽出しつつ、写真・チャートといった非テキスト情報も記述して索引化できるようにする。良質なパースがその後の検索・分類システムで「見つけられるか否か」を決めるという主張を、実装手順とともに示したガイドである。

## 設計のポイント

- 下流の検索・分類の精度上限はパース精度で決まるため、取り込み時点の抽出品質に投資する
- 劣化スキャンや複雑レイアウトには `tier="agentic_plus"` を選ぶ
- `expand` で markdown（LLM向け）/text（ページ単位）/items（表・図検出用の構造ツリー）を用途別に取り出す
- `custom_prompt` にドメイン知識（ディスカバリー文書である旨、OCRの空白崩れ補正、写真の内容記述など）を自然言語で与え、アップロード→パースの二段APIとして組む

## 使いどころ

- Relativity・Everlaw・DISCOなどのeDiscovery基盤上で、写真・スライド・表・手書きを含む雑多なスキャン文書を検索/分類したい法務チーム
- 証拠開示文書の取り込みパイプラインを設計するエンジニア
