---
type: guidance
title: AIシステムにおける害（harm）の評価とResponsible AI設計ガイド
title_original: Foundations of assessing harm
industry: cross-industry
cloud: []
patterns:
- guardrails
- human-in-the-loop
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/responsible-innovation/harms-modeling/
published_at: '2025-04-08'
---

## 概要

AIやアルゴリズムによる意思決定システムが引き起こしうる害を事前に特定し、設計段階で対処するための「harms modeling」の考え方を紹介する。ステークホルダーの多様な視点から、身体的・心理的・経済的被害や機会損失など具体的な害の類型と評価の観点を整理する。

## 設計のポイント

- ステークホルダー（顧客・非顧客含む）ごとに便益と潜在的な害の両面を洗い出してから設計に着手する
- 人間の監督（human oversight）が欠けた自動判断ほど害のリスクが高まる点を設計時に考慮する
- 身体的・心理的・経済的機会損失など複数カテゴリの害を網羅的にチェックする

## 使いどころ

- 採用・住宅・保険など人の機会に関わる自動判断システムを設計するアーキテクト
- 医療診断支援やチャットボットなど人に直接影響するAIエージェントの責任あるAI設計を検討するチーム
