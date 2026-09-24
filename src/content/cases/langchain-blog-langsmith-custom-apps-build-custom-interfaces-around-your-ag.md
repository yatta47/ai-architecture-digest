---
type: announcement
title: 'LangSmith Custom Apps: エージェントデータ上に独自UIを作って共有'
title_original: 'Introducing LangSmith Custom Apps: Build custom interfaces around your agent data'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- human-in-the-loop
components:
- LangSmith
- LangSmith Chat
- LangSmith API
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-custom-apps
published_at: '2026-09-24'
---

## 概要

LangSmith Custom Appsは、LangSmithのデータ上に独自UIを構築・公開し、LangSmith内で実行できる機能。ホスティング、認証、権限管理の手間なく、アノテーション、実験比較、トレースレビュー向けの専用画面を作れる。

## 設計のポイント

- チャットで要望を伝えてアプリを生成するか、テンプレートとコーディングエージェントで自前実装するかを選べる。
- レビュー担当者に応じて、エンジニアには全トレース、専門家には依頼と応答とルーブリックだけを出す。
- 実験比較を顧客セグメントや失敗カテゴリ別のビューにして、リリースレビューで再利用する。
- 公開先をワークスペース内にして、認証や権限を基盤に任せる。

## 使いどころ

- 専門家アノテーションの画面を評価基準に合わせたい場合。
- プロンプトやモデル変更の回帰確認を定型化したい場合。
- エージェント種別ごとのトレースレビューを定期的に行いたい場合。
