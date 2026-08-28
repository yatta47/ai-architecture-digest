---
type: case
title: 建設機械のTrackunit、IrisXで分断された機材データを自然言語インサイトへ変換
title_original: How Trackunit turns construction data into decisions with AI
company: Trackunit
industry: manufacturing
cloud: []
patterns:
- text-to-sql
- ai-agent
- data-federation
components:
- Databricks
- Unity Catalog
- MCP
- Genie
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-trackunit-turns-construction-data-decisions-ai
published_at: '2026-08-28'
---

## 概要

建設機械のテレマティクス企業TrackunitはDatabricks上にIrisXという運用データプラットフォームを構築し、OEM・レンタル会社・施工業者などエコシステム全体に分散した機材・稼働・現場データを接続、構造化、業務判断に活かす「connect・distill・amplify」の3層構成をとる。Genieによる自然言語分析とTrackunit IrisX MCPによる既存ツールへの埋め込み、業務課題ごとに用意された『IrisX Blueprints』で数日で導入できる自動化を提供する。バッテリー管理ブループリントはOEMあたり年間約300万ドル、契約外利用検知は約200万ドルの価値を創出したと報告している。

## 設計のポイント

- connect（データ接続）・distill（構造化と分析）・amplify（ワークフロー実行）の3層で、生データから業務アクションまでを一気通貫にする
- 業種特有のコンテキスト（機材履歴・稼働条件・契約条件）を保持したまま複数ソースのデータを統合し、単なる数値以上の意味を持たせる
- MCP経由で既存の業務ツールにAI分析を埋め込み、ユーザーがシステムを切り替えずに済むようにする
- 汎用的な開発基盤ではなく、業務課題ごとの『Blueprints』としてデータ接続・分析・自動化をパッケージ化し導入期間を短縮する

## 使いどころ

- OEM・レンタル会社・施工業者など異なる利害関係者間で機材データが分断されている業界のデータ統合
- 現場からの生データを非エンジニアの業務担当者が自然言語で分析できるようにしたい場合
- 契約超過利用の検知やバッテリー劣化の早期発見など、特定の業務課題に特化した自動化を素早く立ち上げたい場合
