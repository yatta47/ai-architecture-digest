---
type: announcement
title: 米財務省の120万ページ規模文書で汎化性能を測るベンチマーク『OfficeQA Pro V2』
title_original: 'Introducing OfficeQA Pro V2: A New Benchmark for Enterprise Grounded Reasoning'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- eval
- document-processing
components:
- Databricks Genie
- ai_parse
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/introducing-officeqa-pro-v2-new-benchmark-enterprise-grounded-reasoning
published_at: '2026-08-06'
---

## 概要

Databricksは、既存のOfficeQAベンチマークが特定コーパスへの過学習を測れていないという課題意識から、米財務省の未公開文書約1400件・12万ページを新規コーパスとしたOfficeQA Pro V2を公開した。素のエージェントハーネスの平均精度は26%にとどまる一方、Databricks Genie（ai_parseによる事前パース込み）を使うと相対92%の改善で最大60%まで精度が向上し、ハーネス設計の差が根拠付き推論の成否を大きく左右することを示した。

## 設計のポイント

- 既存ベンチマークへの過学習と真の汎化能力を切り分けるため、モデル未見の新規コーパス・新規タスクで評価するベンチマークを別途用意する
- モデル単体ではなくエージェントハーネス（文書パース・検索・推論の組み合わせ）を評価単位とし、ハーネスの差が精度に与える影響を定量化する
- コストと正答率の両軸でモデル×ハーネスの組み合わせをプロットし、パレートフロンティア上の構成を可視化して選定材料にする

## 使いどころ

- 文書横断の分析的な質問応答エージェントを社内展開する前に、汎化性能を客観的に評価したいAI基盤チームとして
- モデル選定だけでなく、文書パース方式を含めたハーネス設計がコスト・精度に与える影響を検証したい場合として
