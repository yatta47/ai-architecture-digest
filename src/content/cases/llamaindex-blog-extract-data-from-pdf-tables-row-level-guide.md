---
type: guidance
title: 表形式の繰り返しエンティティを漏れなく抽出するLlamaExtractのTable Row機能
title_original: Extracting Repeating Entities from Documents
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaExtract
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/extracting-repeating-entities-from-documents
published_at: '2026-07-19'
---

## 概要

文書全体を一度に抽出させると、LLMのU字型の位置バイアスにより数百件規模の表で後半のエントリが欠落する問題を、LlamaExtractの新しいPER_TABLE_ROW抽出ターゲットで解決する方法を解説している。表の行やリスト項目などの繰り返し構造を検出してエンティティ単位に分割してからスキーマを適用することで、380件の病院リストを取りこぼしなく抽出できた例を示している。

## 設計のポイント

- 文書全体を一括抽出するのではなく、繰り返し構造を検知してエンティティ単位に分割してからスキーマを適用する(PER_TABLE_ROW)
- 1チャンクあたり1〜5件程度に抑えることで、LLMの位置バイアスによる中間データの抜け漏れを防ぐ
- スキーマは単一エンティティに対して定義し、各セグメントの抽出結果を最後に集約してリストとして返す

## 使いどころ

- 数百件規模の保険適用病院リストや商品カタログなど、大量の繰り返し行を持つ表から全件を漏れなく抽出したい場合
- テンプレートベース抽出では書式の揺れに対応できない一方、文書全体を一度にLLMへ渡すと後半のデータが欠落してしまう場合
