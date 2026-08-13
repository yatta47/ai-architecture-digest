---
type: case
title: カナダの大手貨物鉄道がGenie Codeでパイプライン開発を自動化し数日→数分に短縮
title_original: How a major freight railroad scaled pipeline creation with Genie Code
industry: logistics
cloud: []
patterns:
- ai-agent
- spec-driven-development
components:
- Databricks Genie Code
- Unity Catalog
- Databricks Apps
- PySpark
- Delta Lake
- Lakeflow Jobs
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-major-freight-railroad-scaled-pipeline-creation-genie-code
published_at: '2026-08-12'
---

## 概要

カナダ最大級の貨物鉄道会社が、数百本に及ぶレガシーパイプラインの刷新をDatabricks Genie CodeとカスタムAgent Skillsで自動化。Unity Catalogのメタデータに基づき、短いYAMLプロンプトからDDL・履歴ロード・ストリーミング取り込み・増分マージ・テストまで6種類の本番用成果物を生成し、新規テーブル取り込みの90%以上を自動化、パイプライン開発を数日から数分に短縮した。

## 設計のポイント

- カスタムAgent Skill（SKILL.md＋パターンファイル群）に自社の取り込み規約・命名規則・マージロジックをバージョン管理された形でエンコードし、開発者間で再利用する
- Unity Catalogのスキーマ情報を根拠にコード生成することで、LLMの確率的な推論と決定的なエンタープライズ標準の適用を分離する
- 監査列の配置や変更シーケンス保護マージ、ソフトデリート整合など『正しいと分かっていること』は自動化し、解釈が必要な部分だけをLLMに任せる

## 使いどころ

- 数百本規模のレガシーETLパイプラインを手作業で書き換える余力がない大規模データ基盤チーム
- 生成コードにエンタープライズの規約・監査要件を一貫して適用したいデータエンジニアリング組織
