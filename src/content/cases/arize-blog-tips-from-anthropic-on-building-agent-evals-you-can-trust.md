---
type: guidance
title: 信頼できるエージェント評価の作り方(Anthropicの知見)
title_original: Tips from Anthropic on building agent evals you can trust
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
components: []
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/anthropic-tips-how-to-build-evals-you-can-trust/
published_at: '2026-07-28'
---

## 概要

Anthropicの応用AIチームは、9ポイント向上したように見えたエージェント評価が実はSQLクエリにLIMIT句を足してハーネスの欠陥を回避していただけだった事例を挙げ、スコアだけでなくトランスクリプトを確認する重要性を説く。既存動作を守る回帰評価と、能力のフロンティアを広げる能力評価を目的別に使い分けるべきだと提案する。

## 設計のポイント

- スコアの変化だけで判断せず、必ずトランスクリプトを開いて『なぜ』改善/悪化したかの因果を確認する運用にした。
- 回帰評価(既存挙動を守る、高い合格率が目標)と能力評価(フロンティアを押し広げる、あえて難しく余地を残す)を目的別に分けて運用した。
- エージェント評価は最終結果だけでなく、意思決定の系列・ツール呼び出し・ハーネス・外部システムの状態まで多層的に見る必要があると位置づけた。

## 使いどころ

- モデルやプロンプトの変更が本当の能力向上か、ハーネスの欠陥を突いた偶然の結果かを見極めたいエージェント開発チーム。
- リリースの安全性判断(回帰評価)と、次に何を作るべきかの判断(能力評価)を切り分けたいプロダクトチーム。
- 長時間稼働するエージェントで、初期の小さな誤りが後続の判断を汚染する問題を評価に反映させたいエンジニア。
