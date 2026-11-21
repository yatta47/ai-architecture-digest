---
type: announcement
title: Microsoft Foundryのエージェント継続改善ループ
title_original: Continuous improvement comes to Microsoft Foundry
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- llmops
- prompt-optimization
- human-in-the-loop
- fine-tuning
components:
- Microsoft Foundry
- GitHub Copilot
- GitHub Copilot Fusion
outcome:
  type: quality
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/continuous-improvement-comes-to-microsoft-foundry/
published_at: '2026-11-17'
---

## 概要

Foundryに、エージェントのトレースやユーザー入力を戻して継続的に改善する仕組みが加わった。改善案を自動で見つけて試し、品質と速度とコストのトレードオフを示したうえで、採用は人が決める。

## 設計のポイント

- トレースとユーザー入力を学習ループにフィードバックする。
- 改善候補を品質、速度、コストで比較し、本番反映は人が判断する。
- 軽いスキル改善から重みの学習まで段階的に改善手段を選べる。

## 使いどころ

- 本番のエージェントを運用しながら精度を上げたいとき。
- モデル更新が頻繁な環境で改善を継続したいとき。
