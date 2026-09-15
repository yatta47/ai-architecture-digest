---
type: case
title: 盗電検知のMLスコアを調査・回収・報告まで繋げるガバナンス型アクションループ
title_original: How energy teams turn theft detection into governed action with Genie and AI/BI
industry: energy
cloud: []
patterns:
- decision-execution
- text-to-sql
- multi-agent-orchestration
components:
- Databricks Apps
- Lakebase
- Unity Catalog
- Genie One
- Agent Bricks
- Databricks Model Serving
- Unity Gateway
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-energy-teams-turn-theft-detection-governed-action-genie-and-ai-business-processes
published_at: '2026-09-15'
---

## 概要

エネルギー事業者向けに、ML(盗電検知)のスコアだけで終わらせず調査・現場対応・回収・報告までを1つのガバナンスされたワークフローに統合する構成をDatabricks上に実装。Databricks App上でLakebaseがライブなケース状態と回収額を保持し、Unity Catalog・Unity Gatewayが信頼できるメトリクスとガバナンスされたAI利用を提供、Agent BricksのMulti-Agent SupervisorがGenieクエリを束ねて経営報告を自動生成する。

## 設計のポイント

- MLのスコア(予測)そのものではなく、調査・現場対応・回収・報告までの一連の業務ループを1つのガバナンスされたアプリに統合して初めてビジネス成果になる
- LakebaseのPostgresトランザクション層でライブなケース状態を低レイテンシに読み書きしケース対応をリアルタイムに保つ
- Unity Gateway経由でモデル呼び出しを経路統一することでPII保護とAIコストの可視化を両立し、モデル変更も設定変更のみで済む

## 使いどころ

- 盗電検知など不正検知のMLスコアをフィールド対応・回収・規制報告まで一気通貫で運用したいエネルギー事業者
- 保険金請求不正や与信不正など同様のML→アクション連携を必要とする規制業界のリスク管理チーム
