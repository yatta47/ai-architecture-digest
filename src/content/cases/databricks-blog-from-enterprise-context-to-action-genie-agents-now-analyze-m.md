---
type: announcement
title: Genieエージェントが非構造化データとMCP連携に対応
title_original: 'From enterprise context to action: Genie Agents now analyze more data sources'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
- context-engineering
components:
- Databricks Genie
- Unity Catalog
- Lakeflow
- MCP
- OpenSharing
- Genie Clean Rooms
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/enterprise-context-action-genie-agents-now-analyze-more-data-sources-transform-your-work
published_at: '2026-11-11'
---

## 概要

Genie Agentsが、Unity Catalogボリューム上の大量文書をページ単位の引用付きで分析できるようになった（Public Preview）。Lakeflowやネイティブ MCP コネクタ（GA）でJira・Slack等と連携して実行でき、OpenSharingやClean Roomsで社外に統制された形で共有できる。

## 設計のポイント

- 構造化・非構造化データを同一のガバナンス下で扱う。
- MCPコネクタで外部ツールの読み取りだけでなく操作も行う。
- 社外共有は元データを見せない形で提供する。

## 使いどころ

- 文書とテーブルを横断して質問したい業務部門。
- パートナーに専用エージェントを提供したい企業。
