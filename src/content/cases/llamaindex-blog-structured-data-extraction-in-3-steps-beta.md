---
type: announcement
title: スキーマ指定だけで非構造化文書から構造化データを抽出するLlamaExtractの提供開始
title_original: 'Introducing LlamaExtract: Unlocking Structured Data Extraction in Just a Few Clicks (beta)'
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaExtract
- LlamaParse
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-llamaextract-unlocking-structured-data-extraction-in-just-a-few-clicks
published_at: '2026-07-19'
---

## 概要

LlamaIndexが、ユーザーが定義したJSONスキーマに沿って非構造化文書（PDF・スキャン画像など）から型付きの構造化データを抽出するLlamaExtractをパブリックベータとして公開。LlamaParseの解析基盤上に構築されており、OCR・スキャン処理・テーブル解析を意識せず使える。

## 設計のポイント

- スキーマ定義→自動抽出→SDK連携の3ステップに操作を簡略化し、ユーザーはJSONまたはUIでスキーマを指定するだけで済むようにしている
- 抽出結果がスキーマに準拠しない場合はエラーメッセージを返し、下流タスクで型の妥当性を保証する
- 既存のLlamaParse解析基盤を再利用することで、OCRやテーブル抽出などの前処理を個別実装せずに済む設計にしている

## 使いどころ

- SEC提出書類や請求書、履歴書など、フォーマットが多様な文書から特定フィールドを大量に抽出したい財務・経理・HR・保険部門
- ルールベースやカスタムMLパイプラインでの構造化抽出運用に限界を感じている開発者
