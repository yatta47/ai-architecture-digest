---
type: announcement
title: データ・AI利用・コストをアカウント横断で統治するGenie搭載ガバナンスハブ
title_original: 'Introducing Governance Hub: Intelligent, account-level governance over your Databricks estate'
company: Databricks
industry: cross-industry
cloud:
- aws
- azure
- gcp
patterns:
- llmops
- ai-agent
- root-cause-analysis
components:
- Unity Catalog
- Unity AI Gateway
- Genie
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/introducing-governance-hub-intelligent-account-level-governance-over-your-databricks-estate
published_at: '2026-08-26'
---

## 概要

Databricksは数百ワークスペース規模のアカウントに散らばっていたデータ健全性・AI利用状況・コストの可視化を一元化するGovernance Hubをベータ公開した。プリンシパル単位のアクセス洞察やUnity AI Gateway経由のAIトラフィック監視に加え、Genieエージェントが自然言語の問い合わせに実データに基づく原因分析や推奨アクションを返す機能を統合している。

## 設計のポイント

- データ・AI利用・コストという3つの観点をアカウント全体で横断的に可視化し、ワークスペースごとに個別ダッシュボードを作る手間を無くした
- 「このユーザーは何にアクセスできるか」をプリンシパル起点で一元化し、直接付与・グループ経由の継承・所有権を1画面で解決できるようにした
- Unity AI Gatewayを通じて社内外のモデル・エージェント・MCPのトラフィックを単一の統制ポイントに集約し、トークン消費やガードレール適用状況を可視化した
- 自然言語の問い合わせに対しGenieエージェントが実データに基づいた原因分析や推奨アクションを返す設計にし、SQLを書かずにガバナンス調査できるようにした

## 使いどころ

- 数百ワークスペース規模のDatabricksアカウントを横断的に統治したいプラットフォーム/ガバナンスチーム
- 社内のAI利用状況とコストをリアルタイムに可視化したいFinOps/AI導入チーム
- 監査・アクセスレビュー・オフボーディング時の権限棚卸しを効率化したいセキュリティチーム
