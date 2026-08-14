---
type: case
title: Scottish WaterがDatabricks Genieで資本投資プロジェクトデータをTeams上の自然言語対話にした事例
title_original: How Scottish Water made its capital investment data conversational with Databricks Genie
company: Scottish Water
industry: public-sector
cloud: []
patterns:
- text-to-sql
- ai-agent
- context-engineering
components:
- Databricks Genie
- Unity Catalog
- Microsoft Teams
- Microsoft Copilot
- Model Context Protocol
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-scottish-water-made-its-capital-investment-data-conversational-databricks-genie
published_at: '2026-08-13'
---

## 概要

Scottish Waterの資本投資プログラムでは、必要なデータ自体は揃っていたが大量のレポート群やデータ専門家依存でアクセスが遅く、同じ質問に答えるレポートが重複して作られていた。Databricks Genieを使い、Unity Catalogの統制されたgoldレイヤーとセマンティックレイヤー(metric views)の上に構築した『SPARK』という自然言語インターフェースをMicrosoft TeamsのCopilot経由・MCP接続で提供し、平均8クリック+ダッシュボード読み込みだった調査を1つの質問に置き換え、年間520〜1300時間相当の削減を見込む。

## 設計のポイント

- GenieをUnity Catalogの生テーブルに直結せず、ユースケースに必要なデータだけを統制されたgoldレイヤーとメトリックビュー(セマンティックレイヤー)に絞り込んでから接続し、回答の一貫性を担保する
- 会計期間の定義やマイルストーンゲートの順序などの業務ルールをGenie空間に明示的な指示として組み込み、汎用設定に頼らずドメイン固有の解釈を正しくさせる
- 実際のユーザーの言い回しと対応するSQLの組を教師データとして与え、ベンチマークスイートでデータやGenie空間定義の変更のたびに精度を回帰テストする
- 既存のTeamsという利用者が既にいる場所に会話体験を統合し、新しいツールへの切り替えコストを発生させない

## 使いどころ

- レポートが乱立し同じ質問に答える資料が重複して作られてしまっている大規模組織
- 非技術者がデータ専門家を介さず自分でプロジェクト状況を確認したい現場チーム
- 自然言語分析エージェントの回答をガバナンスされた単一の定義に揃えたい統制重視の組織
