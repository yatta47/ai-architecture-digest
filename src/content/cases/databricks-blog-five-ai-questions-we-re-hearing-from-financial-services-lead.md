---
type: opinion
title: 金融機関がAI導入で直面する5つの本番運用の壁
title_original: Five AI questions we're hearing from financial services leaders
industry: financial-services
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- guardrails
- multi-agent-orchestration
components: []
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/five-ai-questions-were-hearing-financial-services-leaders
published_at: '2026-09-09'
---

## 概要

DatabricksがSibos 2026を前に、金融機関のCFO・コンプライアンス責任者・トレジャリー・リレーションシップマネージャーから聞く5つの問いを整理した記事。ガバナンスと監査可能性、AML調査でのエージェント活用、顧客対応の効率化、リアルタイムデータでの不正検知、AIコストの本番運用管理という論点を、RBC Brewin DolphinやCoinbaseなどの実例とともに紹介している。

## 設計のポイント

- AMLエージェントに人間のmaker-checkerを組み込み、SARドラフト作成は自動化しつつ提出は人間が行う権限分離設計にする
- エージェントのデータアクセスをアナリスト本人の権限範囲に限定し、根拠データ・推奨・レビュー有無を追跡可能なログとして残す
- 不正検知など意思決定にリアルタイム性が必要な処理は、サブ100ミリ秒P99など明確なレイテンシ目標を置いて設計する
- タスクごとに必要十分なモデルへルーティングし、利用拡大前からトークンコストを可視化・統制する

## 使いどころ

- AML/金融犯罪調査チームが、AIの推奨を規制当局の監査に耐える形で運用したい場合
- 資産運用会社が複数ファンドの投資コメンタリー生成をマルチエージェントで拡張しつつコンプライアンスを維持したい場合
- トレジャリー・財務部門が全エンティティ・全通貨の流動性状況をリアルタイムに把握し行動につなげたい場合
