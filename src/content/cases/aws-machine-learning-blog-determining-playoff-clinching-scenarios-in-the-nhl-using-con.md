---
type: case
title: 制約プログラミングでNHLプレーオフ進出確定シナリオを自動算出するシステム
title_original: Determining playoff clinching scenarios in the NHL using constraint programming
ai_relevant: false
company: AWS Generative AI Innovation Center
industry: media
cloud:
- aws
patterns: []
components: []
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/determining-playoff-clinching-scenarios-in-the-nhl-using-constraint-programming/
published_at: '2026-08-07'
---

## 概要

AWS Generative AI Innovation Centerは、NHLのプレーオフ進出確定条件を自動判定するシステムを、Google OR-ToolsのCP-SATソルバーによる制約プログラミングとカスタム木探索で構築した。0-day解法でその時点の確定判定を行い、n-day先読み探索で今後の試合結果パターンごとの確定条件を導出し、過去4シーズン分でNHL公式発表と完全一致する結果を検証している。
