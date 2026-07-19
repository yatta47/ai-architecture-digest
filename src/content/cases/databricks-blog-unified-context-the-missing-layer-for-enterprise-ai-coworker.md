---
type: announcement
title: 散在する企業コンテキストを統合しAIコワーカーの意思決定精度を高めるGenie One
title_original: 'Unified context: The missing layer for enterprise AI coworkers'
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
- data-federation
components:
- Genie One
- Genie Ontology
- Unity Catalog
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/unified-context-missing-layer-enterprise-ai-coworkers
published_at: '2026-07-16'
---

## 概要

Databricksは、CRMやダッシュボード、SaaSアプリに散在するビジネスコンテキストを統合するナレッジグラフ「Genie Ontology」と、それを基盤にSlack・Teams・ダッシュボードなど業務の現場でAIコワーカーとして動く「Genie One」を発表した。汎用アシスタントが単発の質問には強くても意思決定に必要な文脈を横断的に踏まえられない課題に対し、ガバナンスされたビジネス定義を共有コンテキスト層として提供する。

## 設計のポイント

- データの「所在」ではなく「事業がどう動いているか」を表すナレッジグラフとしてビジネス用語・指標・関係性を組織化する。
- Unity Catalogのガバナンス（アクセス権・認定データ・共通定義）の上にGenie Ontologyを重ね、権限は既存ルールを継承しつつ関連シグナルを横断的に接続できるようにする。
- 質問応答だけでなく、レポート作成やワークフロー起動などのエージェント的なアクション実行まで一気通貫でつなげる。
- 利用状況や認定資産へのリンクなどの要因でどの定義が正とみなされるかをランク付けし、コンテキストが常に最新であり続けるようにする。

## 使いどころ

- フォーキャストレビューや案件レビューのたびに複数ツールを行き来してデータを突き合わせている営業・財務チーム。
- 汎用チャットアシスタントでは業務の文脈を十分に踏まえられず、意思決定に活かせていない組織。
- AIの回答や実行結果に既存のガバナンス・権限ルールを確実に適用したいセキュリティ・コンプライアンス部門。
