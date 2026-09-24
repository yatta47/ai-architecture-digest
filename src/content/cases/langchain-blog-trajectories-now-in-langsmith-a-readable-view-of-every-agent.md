---
type: announcement
title: 'LangSmith Trajectories: エージェントのセッションを時系列で読める表示'
title_original: 'Trajectories now in LangSmith: A readable view of every agent session'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- human-in-the-loop
- root-cause-analysis
components:
- LangSmith
- LangChain
- LangGraph
- Deep Agents
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-trajectories-tracing
published_at: '2026-09-24'
---

## 概要

LangSmithが、メインエージェントとサブエージェントを含むセッションのメッセージを出現順に並べた軌跡(Trajectory)ビューを提供開始した。原因の特定、専門家によるレビュー、オンライン評価、微調整用データ化に使える。

## 設計のポイント

- 入れ子の実行木から重複を除いた射影として軌跡を持ち、詳細が必要なときだけトレースに降りる二層構造にする。
- オンライン評価を軌跡に対して実行し、累積する文脈の重複によるノイズを避ける。
- アノテーションキューで専門家に読みやすい形でレビューさせる。
- 良い軌跡をデータセットに保存し、SFTに再利用する。

## 使いどころ

- 長時間のマルチターンエージェントで、どこで挙動がずれたかを早く特定したい場合。
- 医療・金融などの専門家にエージェントの挙動をレビューしてもらう場合。
- 本番セッションを評価や微調整の資産にしたい場合。
