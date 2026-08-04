---
type: announcement
title: オープンなAIエージェントセキュリティ基盤構想（Omnigent/DASF/DAGF/BlackIce/Lakewatch）
title_original: Databricks joins the Open Secure AI Alliance to advance AI's safety and security
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- defense-in-depth
- guardrails
- multi-agent-orchestration
components:
- Omnigent
- DASF 3.0
- DAGF
- BlackIce
- Lakewatch
- NVIDIA OpenShell
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/databricks-joins-open-secure-ai-alliance-advance-ai-safety-and-security
published_at: '2026-08-04'
---

## 概要

DatabricksはNVIDIAなど75以上の組織が参加するOpen Secure AI Allianceの創設メンバーとして、AIの安全性・セキュリティ研究をオープンに共有する取り組みに参画した。オープンなエージェントメタハーネスOmnigent、リスクと対策をマッピングするAIセキュリティフレームワークDASF 3.0、企業向けAIガバナンスフレームワークDAGF、オープンソースのレッドチーミングツールBlackIce、そしてエージェント型脅威検知のためのセキュリティレイクハウスLakewatchを提供する。NVIDIAがアクセラレーテッドコンピューティングを担い、Databricksはデータ・ガバナンス・エージェント制御・セキュリティ運用を担うことで、AIスタック全体をオープンに保護する体制を目指す。

## 設計のポイント

- オープンなメタハーネス(Omnigent)によりハーネスやモデルを自由に選択・組み合わせつつ、ポリシー・支出上限・サンドボックス分離を横断的に適用する
- DASF 3.0でメモリ汚染・ゴール操作・不正なMCP接続などエージェント固有の脅威を含む97のリスクを73の緩和策にマッピングし、リスク特定から実装可能な対策までの道筋を提供する
- セキュリティレイクハウス(Lakewatch)により統合されたガバナンス済みデータ基盤上でエージェント型の脅威検知・対応をスケールさせる
- コンテナ化されたレッドチーミングツール(BlackIce)で14種のAIセキュリティツールを再現可能な単一環境にまとめ、個別導入の手間を削減する

## 使いどころ

- 複数のエージェントハーネスやモデルを横断して一貫したポリシー・ガバナンスを適用したい開発チーム
- MITRE ATLASやNIST、OWASPなど既存基準に準拠した形でAIエージェントのリスク管理を行いたいセキュリティ/コンプライアンス担当者
- プロンプトインジェクションやデータ漏洩、サプライチェーン攻撃を事前に検証したいAIレッドチーム
- エージェント型システムに対する脅威検知・対応を統合データ基盤上で運用したいセキュリティオペレーションチーム
