---
type: case
title: パーソナルAI「Dot」のエージェント型メモリ検索をLangSmithで50%改善
title_original: 'Improving Memory Retrieval: How New Computer achieved 50% higher recall with LangSmith'
company: New Computer
industry: cross-industry
cloud: []
patterns:
- memory-consolidation
- rag
- eval
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/customers-new-computer
published_at: '2026-06-15'
---

## 概要

パーソナルAI「Dot」を開発するNew Computerは、静的ドキュメント集合に頼らず動的に生成・構造化する『エージェント型メモリ』を実装している。合成ユーザーによるラベル付きデータセットをLangSmithで管理し、意味検索・キーワード検索・BM25・メタフィールドフィルタなど複数の検索手法をprecision/recall/F1で比較評価することで、ベースライン比でrecallを50%、precisionを40%改善した。

## 設計のポイント

- メモリに status や日時などのメタフィールドを付与し、フィルタ検索と組み合わせて高頻度クエリの精度を上げる
- 実ユーザーデータを使わずLLM生成の合成ユーザーでラベル付きデータセットを作り、プライバシーを保ちながら評価を回す
- 意味検索・BM25・メタフィールドフィルタなど複数の検索手法を並行評価し、クエリ種別ごとに最適な手法を選ぶ
- プロンプト変更の全体への影響を実験比較ビューで可視化し、リグレッションを検知する

## 使いどころ

- 長期的なユーザー文脈を保持するパーソナルAI/アシスタントを開発するチーム
- 複数の検索手法を比較しながらretrieval精度をデータドリブンに改善したいチーム
