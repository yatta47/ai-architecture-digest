---
type: announcement
title: 人手評価とLLM-as-a-Judgeのズレを可視化して較正する「Align Evals」
title_original: 'Introducing Align Evals: Streamlining LLM Application Evaluation'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-align-evals
published_at: '2026-06-15'
---

## 概要

LangSmithに追加された「Align Evals」は、LLM-as-a-Judge評価器のスコアと人間の評価がずれる問題に対応する機能。人手でグレーディングした『ゴールデンセット』とLLM評価器のスコアを並べて比較し、不一致な事例を洗い出しながら評価者プロンプトを反復改善できる。

## 設計のポイント

- 評価基準ごとに良い例・悪い例を含む代表データを人手でグレーディングし、評価器のベンチマークとなるゴールデンセットを作る
- 評価器プロンプトの各バージョンをゴールデンセットに対して実行し、人手スコアとの整合度(alignment score)を可視化する
- 整合していない事例を並べて確認し、評価器が過剰採点/過小採点している傾向を特定してプロンプトを修正する
- 変更前のベースラインスコアを保存し、プロンプト変更の効果を継続的に比較できるようにする

## 使いどころ

- LLM-as-a-Judgeのスコアと社内レビュアーの感覚がずれて困っているチーム
- 評価器プロンプトの改善を勘に頼らずデータドリブンに進めたいチーム
