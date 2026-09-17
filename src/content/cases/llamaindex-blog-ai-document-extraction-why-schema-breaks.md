---
type: guidance
title: AIドキュメント抽出で品質を左右するのはスキーマ設計
title_original: 'AI Document Extraction: Why Schema Breaks'
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
components:
- LlamaExtract
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ai-document-extraction-schema
published_at: '2026-09-17'
---

## 概要

AIによる文書抽出はパース（構造復元）と抽出（スキーマに基づく値の特定）という別々の工程であり、精度低下の多くはモデルの読み取り誤りではなく、レビューされていないスキーマ設計の欠陥に起因する。必須項目の誤設定、発行元ごとに意味が異なるフィールド、本来配列であるべき値をスカラーに畳み込む設計などが典型的な失敗パターンとして挙げられ、nullable化・フィールドの意味の明確化・per_table_rowのような複数値抽出の指定といった『監査済みスキーマ』への修正例が示される。

## 設計のポイント

- requiredは文書集団全体で本当に普遍的なフィールドだけに絞り、無い場合はnullを許容する
- 『Total』のように発行元ごとに意味が変わるフィールドは、スキーマの説明文で定義を明示し曖昧さを排除する
- 明細行や検査結果のような繰り返し構造は最初から配列（per_table_rowなど）として宣言し、スカラーへの取りこぼしを防ぐ
- フィールド単位の精度だけでなく、レコード全体としての完全性を別指標として評価する

## 使いどころ

- 与信契約書やリース契約など、同じ概念が複数の値・条件で登場する複雑な法務・財務文書の抽出
- 検査証明書や臨床検査報告など、発行元やベンダーによって項目の呼称・定義が異なる規制文書の抽出パイプライン設計
