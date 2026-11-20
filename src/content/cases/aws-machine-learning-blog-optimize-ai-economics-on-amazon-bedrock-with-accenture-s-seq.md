---
type: guidance
title: Bedrockのトークン支出を抑える6つのレバーとAccentureの適用
title_original: Optimize AI economics on Amazon Bedrock with Accenture's sequenced approach
company: Accenture
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- llmops
- multi-model-routing
components:
- Amazon Bedrock
- application inference profiles
- AWS Cost Explorer
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/optimize-ai-economics-on-amazon-bedrock-with-accentures-sequenced-approach/
published_at: '2026-11-19'
---

## 概要

AIの支出管理として、まず帰属（コスト配賦タグ）を整えてから6つのレバーで最適化する手順を紹介する。Accentureは4つの案件で適用し、測定できた範囲でトークン支出を約40〜85%削減した。

## 設計のポイント

- アプリケーション推論プロファイルをワークロードごとに作り、配賦タグで支出の持ち主を明確にする。
- 計測してから最適化し、変更の効果を測れるようにする。

## 使いどころ

- AI利用の拡大でコストが読めなくなった組織のFinOps担当に向く。
