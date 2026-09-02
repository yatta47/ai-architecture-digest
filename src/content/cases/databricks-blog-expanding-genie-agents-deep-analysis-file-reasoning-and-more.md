---
type: announcement
title: 構造化データと非構造化ファイルを横断推論するGenie Agentsの拡張
title_original: 'Expanding Genie Agents: Deep Analysis, File Reasoning, and More'
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- text-to-sql
- document-processing
- rag
components:
- Genie Agents
- Genie Code
- Unity Catalog
- Agent Mode API
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/expanding-genie-agents-deep-analysis-file-reasoning-and-more
published_at: '2026-09-02'
---

## 概要

DatabricksはGenie Agentsに複数ステップで調査計画を立てて実行するAgent modeとそのAPIを追加し、外部アプリからも深い推論を呼び出せるようにした。あわせてUnity Catalogボリューム上のPDFや文書などの非構造化データを構造化データと同一の会話内で分析できるようにし、Genie Codeによるエージェントの作成・診断・改善提案も強化した。

## 設計のポイント

- Chatモードでは対応できない複雑な業務質問に対し、Agent modeが調査計画の作成・複数回のデータ探索・可視化と根拠付きレポート生成までを自律的に行う
- Agent Mode APIをServer-Sent Eventsでストリーミング配信することで、社内チャットボットやダッシュボードなど任意のアプリに深い推論機能を組み込める
- Unity Catalogボリュームに最大10個のファイルをアタッチし、権限に応じたアクセス制御とコンテンツ検索インデックスにより構造化データと非構造化データを統合分析できる
- Genie Codeが既存のテーブルメタデータやクエリ履歴からエージェントの雛形生成・失敗診断・利用トレンド分析までを支援し、curator(作成者)の負荷を下げる

## 使いどころ

- 従来はデータアナリストが手作業で行っていたオープンエンドな業務調査の代替パートナーとして使いたいチーム
- チャーン理由の分析や契約書比較など、表データと文書コンテンツを横断して答える必要がある業務担当者
- 自社のSlack botや顧客向け分析ポータルに深い推論機能を組み込みたい開発者
- Genie Agentの品質を継続的に改善したいエージェント管理者・データ専門家
