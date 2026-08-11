---
type: guidance
title: Genie Agentsを構造化テーブルと非構造化ドキュメントの両方にグラウンディングしつつUnity Catalogでガバナンスを継承
title_original: How to Ground Genie Agents in Both Structured Data and Documents Without Losing Governance
company: Databricks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
- guardrails
- policy-as-code
components:
- Genie Agents
- Unity Catalog
- Automatic Identity Management
- Databricks Lakehouse
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-ground-genie-agents-both-structured-data-and-documents-without-losing-governance
published_at: '2026-08-10'
---

## 概要

1つのエージェントが構造化データと非構造化ドキュメントの両方にアクセスできるようになると、『誰に何を答えてよいか』というガバナンスが課題になる。Databricksは、モデル層(プロンプト)でアクセス制御を行うのではなく、Unity Catalogの権限・ABAC・行フィルタ・列マスクをそのままGenie Agentsに継承させ、エージェントをエンドユーザー本人のクレデンシャルで実行することで、データがLakehouseを離れる前に必ずアクセス権でフィルタされる設計にしている。Entra IDやOktaとのAutomatic Identity Managementでグループ所属を常に最新化し、異動や退職が即座にエージェントの回答範囲に反映される。

## 設計のポイント

- アクセス制御をLLM/プロンプト層ではなくデータカタログ層に置き、モデルが操作されてもガバナンスが破られないようにする
- エージェントをサービスアカウントではなくエンドユーザー本人のクレデンシャルで実行し、既存の権限・行フィルタ・列マスクをそのまま継承させる
- IDプロバイダとのアイデンティティ同期(AIM)とJITプロビジョニングで、グループ所属の変更が次の質問から即座に反映される状態を保つ
- オブジェクト権限・ABAC・行フィルタ・列マスクの4層を組み合わせ、テーブルへのアクセス可否と『どの行・列が見えるか』を別々に制御する

## 使いどころ

- 1つのエージェントに構造化データと非構造化ドキュメントの両方を横断して答えさせたいが、権限漏洩を避けたい組織
- 地域や部門で閲覧範囲が異なる大規模組織で、異動・退職時のアクセス制御を自動的に追従させたい場合
- 監査で『なぜこのデータが見えたか』を防御可能な形で説明する必要があるコンプライアンス要件の強い環境
