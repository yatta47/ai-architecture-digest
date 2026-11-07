---
type: opinion
title: エージェントを単発プロジェクトでなく継続運用の規律として扱う
title_original: Stop treating agents as one-off projects and start running them as a continuous discipline
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- cost-optimization
- multi-model-routing
- eval
- llmops
components:
- Microsoft Foundry
- Microsoft IQ
- IDC InfoBrief
outcome:
  type: cost
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/stop-treating-agents-as-one-off-projects-and-start-running-them-as-a-continuous-discipline/
published_at: '2026-11-05'
---

## 概要

IDC調査を引き、AIのスケール時のコスト予測、リクエスト単位のモデル最適化、エージェントの継続改善、支出統制とROI測定の4問で資金判断すべきと論じる。FoundryのPlan/Control/Optimizeでモデルルーティング、観測、評価を提供する。

## 設計のポイント

- コストを成果単位で追えるよう、リクエスト・エージェント・成果ごとに計測する。
- 簡単な処理は小さいモデルへルーティングし、評価で品質低下を検知する。
- 不要な検索結果・ツール定義・履歴をモデルに渡さずコンテキストを削る。
- 暴走対策にリクエストごとのサーキットブレーカーを置く。

## 使いどころ

- エージェントを本番展開する前に費用対効果で投資判断する企業のAI推進部門。
- 複数エージェントの運用コストを共通基盤で管理したいプラットフォームチーム。
