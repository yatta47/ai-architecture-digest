---
type: case
title: LLM同士で採点するQ&A評価ツール「Auto-Evaluator」の実装と課題
title_original: Auto-Evaluator Opportunities
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- rag
components:
- FAISS
- Chroma
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/auto-evaluator-opportunities
published_at: '2026-08-26'
---

## 概要

LangChainはドキュメントQ&Aチェーンの品質を自動評価する「Auto-Evaluator」をオープンソース化し、モデルによるテストセット自動生成とモデルによる採点（LLM-as-judge）を組み合わせたホスティング済みアプリ/APIとして公開した。実運用ではファイル転送や画像混入によるレイテンシ、ナイーブなQAペア生成、リトリーバー選択などが改善余地として挙げられている。

## 設計のポイント

- テストセット自動生成（入力文書からランダムにQAペアを生成）とモデルによる採点を1つのワークスペースに統合し、QAチェーンの設定（チャンクサイズ・取得件数・モデル・リトリーバー）を差し替えて比較実験できるようにした
- k近傍による埋め込み検索だけでなくSVMやTF-IDFなど代替のリトリーバーも試せるよう、リトリーバーを差し替え可能な抽象にした
- 実運用のボトルネック（大きな画像入りPDFの転送遅延など）を計測し、画像除去などの改善ポイントを具体的に特定した

## 使いどころ

- LLMベースのQ&Aシステムの評価を自動化・省力化したいチーム
- チャンクサイズやリトリーバーの選択をデータドリブンに比較検討したい開発者
