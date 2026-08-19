---
type: case
title: 長文書・大量出力・複雑スキーマに強いエージェント型文書抽出Precision Mode
title_original: 'Databricks Document Intelligence: Pushing the frontier for complex document extraction'
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- document-processing
- multi-agent-orchestration
- parallel-execution
- fine-tuning
components:
- Databricks Document Intelligence
- ai_extract
- Databricks MemEx
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/databricks-document-intelligence-pushing-frontier-complex-document-extraction
published_at: '2026-08-18'
---

## 概要

Databricksは、ページ間参照が必要な長文書、数千行に及ぶ大量出力、複雑な推論が必要なスキーマという3つの失敗しやすいケースに対応するため、抽出特化のカスタムモデルとエージェントハーネスを組み合わせたPrecision Modeをai_extractに追加した。約9000件のベンチマークで最良のフロンティアモデル（チャンク分割+マージ方式）を7ポイント上回る94.7%の精度を達成し、Intercontinental Exchangeなどの実運用顧客で採用されている。

## 設計のポイント

- 汎用の巨大モデルに頼らず、構造化抽出というタスクに特化した効率的なカスタムモデルを訓練する
- 大規模な抽出ジョブを意味的に分解し、並列サブエージェントで実行して中間結果を保持してから最終出力にマージするハーネスを設計する
- 単純なチャンク分割+マージ方式ではなく、ページ間参照や巨大スキーマに対応できるエージェント的な段階推論を組み込む

## 使いどころ

- 数百ページにわたる契約書やリース契約でページ間の条項参照を正確に解決したい法務・契約管理部門
- 数千行の明細を持つ請求書や船荷証券を扱う財務・物流のバックオフィス処理
- 300以上のネストしたフィールドを持つ複雑スキーマからの構造化データ抽出が必要な金融・製造・医療分野
