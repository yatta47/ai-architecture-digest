---
type: opinion
title: '失礼なプロンプトは効くか: 6モデルでの検証'
title_original: Does being rude to AI work? What 6 models revealed
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- prompt-optimization
components:
- Arize AX
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/does-being-rude-to-ai-work/
published_at: '2026-10-13'
---

## 概要

丁寧・中立・敵対的なプロンプトを6モデルで比較し、精度・トークン数・挙動を調べた。見かけの節約の多くは、口調ではなく簡潔化の指示によるものだった。

## 設計のポイント

- 口調と簡潔化指示を分離して要因を切り分ける。

## 使いどころ

- プロンプトの口調調整の効果を検証したい場面。
