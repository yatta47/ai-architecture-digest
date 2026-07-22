---
type: announcement
title: Claude Cowork のエンタープライズ向け統制機能（RBAC・支出上限・監査ログ）
title_original: Making Claude Cowork ready for enterprise
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- human-in-the-loop
- guardrails
components:
- Claude Cowork
- Claude Enterprise
- OpenTelemetry
- Analytics API
- Zoom MCP connector
- SCIM
- Splunk
- Cribl
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/cowork-for-enterprise
published_at: '2026-04-09'
---

## 概要

AIエージェント「Claude Cowork」が全有料プランで一般提供となり、全社展開に向けてロールベースアクセス制御・グループ単位の支出上限・利用状況分析・OpenTelemetryによる監査ログ・MCPコネクタ単位の権限制御が追加された。エンジニアリング以外の部門（運用・マーケティング・財務・法務）で採用が先行しており、Zapier・Jamf・Airtreeなど複数企業が資料作成やレビュー、投資判断支援などの周辺業務にエージェントを組み込んでいる。

## 設計のポイント

- SCIM連携によるグループ管理とカスタムロールで、AIエージェントの利用範囲をチーム単位に段階的に開放できるようにする
- OpenTelemetryでツール・コネクタ呼び出しやファイル変更、承認が手動か自動かまで含めてイベント化しSIEMへ連携する
- MCPコネクタごとに読み取り専用など操作単位の権限を組織全体に一括適用し、書き込み系操作のリスクを抑える
- 管理コンソールとAnalytics APIでチームごとの採用状況・利用量を可視化し、展開判断と予算配分に使う

## 使いどころ

- 全社展開前にどの部門・チームからAIエージェントの利用を許可するか段階的に判断したい管理者
- AIエージェントによる操作を監査ログとして残しコンプライアンス・SIEM要件を満たしたい企業
- 部門別の利用コストを予算内に収めつつ利用実態を可視化したい組織
- 会議やドキュメント連携（Zoomなど）を通じて、コア業務の周辺作業をエージェントに任せたいチーム
