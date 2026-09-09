---
type: case
title: メタデータと実行時テレメトリを統合したエージェント型org健全性モニタリング
title_original: How metadata and runtime telemetry reveal which enterprise system problems to fix first
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- data-federation
- root-cause-analysis
- decision-execution
- ai-agent
components:
- Salesforce Health Insights
- MuleSoft
- Agentforce
- Data 360
outcome:
  type: quality
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-metadata-and-runtime-telemetry-reveal-which-enterprise-system-problems-to-fix-first/
published_at: '2026-09-08'
---

## 概要

Salesforceは設定メタデータ（静的）と実行時テレメトリ（動的）を紐付け、billions規模のトランザクションを扱うエンタープライズorgの健全性を約400以上のシグナルで評価するSalesforce Health Insightsを構築した。静的なPDFレポートから、findingsの状態（是正/受容/対象外）を保持し優先度と対応工数で次善アクションを提示するアプリ内のエージェント型体験へ進化させた。

## 設計のポイント

- 既存のメタデータパイプラインを壊さず、共有ハーモナイゼーション層とコネクタパターンで後付けする追加型アーキテクチャを採用
- 設定メタデータと実行時テレメトリという性質の異なる2つのデータソースを、トラフィック・タイミング・季節性を考慮して紐付ける
- findingsを標準オブジェクト化してdispositionを保持し、既に対応済み/対象外と判断した問題が繰り返し検出されないようにする
- セキュリティ・プロセス自動化・エージェント対応など領域ごとに異なる指標を共通スキーマでロールアップしつつ個別の文脈は失わない設計

## 使いどころ

- billions規模のトランザクションを扱う大規模エンタープライズSaaS運用チームの健全性可視化と優先順位付け
- 複数の監視ツールに情報が分散し『何から手を付けるべきか』の判断に迷う状況の意思決定支援
- Agentforceなどエージェント機能導入前に既存org構成の『エージェント対応可否』を点検したいケース
