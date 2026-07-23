---
type: guidance
title: SCIスコアでAzureアプリの炭素効率を継続測定するアーキテクチャ
title_original: Measure Azure app sustainability by using the SCI score
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/apps/measure-azure-app-sustainability-sci-score
published_at: '2026-02-24'
---

## 概要

ISO/IEC 21031:2024で標準化されたSoftware Carbon Intensity（SCI）スコアを使い、既存Azureワークロードの炭素排出量を継続的に測定・可視化するリファレンスアーキテクチャ。排出データとパフォーマンス・コストデータをData Lakeに集約し、Power BIダッシュボードで相関を追跡する。
