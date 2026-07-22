---
type: case
title: 燃料電池R&Dデータを統合しAIエージェントにも開放するガバナンス済みDatabricks基盤
title_original: Why R&D Data Belongs in the Lakehouse, and Why Agents Need It There
company: cellcentric
industry: manufacturing
cloud:
- azure
patterns:
- context-engineering
- data-federation
- ai-agent
- human-in-the-loop
components:
- Databricks
- Unity Catalog
- Lakehouse Federation
- Delta Sharing
- Databricks Asset Bundles
- SAP S/4HANA
- MCP
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/why-rd-data-belongs-lakehouse-and-why-agents-need-it-there
published_at: '2026-07-21'
---

## 概要

水素燃料電池システムを開発するcellcentricは、Databricks上にUnity CatalogとLakehouse Federationを用いた「Data Hub」を構築し、SAP・MES・IoTテレメトリ・ラボデータなど散在するR&Dデータを「Fuel Cell Passport」という単一のデータプロダクトに統合した。同じガバナンス済みコンテキストを人間向けUIとエージェント向けMCPサーバーの両方から提供し、ドキュメントの充実度を品質指標として可視化することで、複雑なR&D調査にかかる時間を数週間から数日へと短縮した。

## 設計のポイント

- Unity Catalogによるガバナンス層の上に「データプロダクト層」を重ね、所有者・ライフサイクル状態・利用文脈(context entries)を紐付けて管理する。
- 人間向けのマーケットプレイスUIとAIエージェント向けのMCPサーバーの両方から、同一のガバナンス済みコンテキストを一貫して提供する。
- テーブル/カラムのドキュメント充足度を「context-coverageバッジ」として可視化し、ドキュメント整備をエンジニアリングワークフローの一部として組み込む。
- AIが支援生成したカラムコメントも必ず担当エンジニアがレビューしてからマージする運用にし、ヒューマンインザループで品質を担保する。

## 使いどころ

- SAP、MES、IoTテレメトリ、ラボDBなど複数の基幹システムにまたがるR&D調査を、単一のガバナンス済みデータプロダクトから行いたい製造業のエンジニアリングチーム。
- LLMエージェントに社内データを参照させる際、スキーマ情報だけでなく利用文脈やアクセス権限も含めて安全に渡したい場合。
- ドキュメント整備が形骸化しがちな組織で、カバレッジを定量化し継続的な改善インセンティブを設計したい場合。
- オンプレミスのSQLソースを含む散在データをレイクハウスへフェデレーションし、AI利用可能な形に統合したいケース。
