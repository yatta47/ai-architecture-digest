---
type: case
title: Slack常駐のデザインエージェントContent StudioをDeep Agentsで構築
title_original: How We Built Our Design Agent
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- multi-agent-orchestration
- human-in-the-loop
components:
- Managed Deep Agents
- LangSmith Sandbox
- Slack
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/design-agent
published_at: '2026-10-27'
---

## 概要

LangChainはSlackから動画・画像・スライドを生成するデザインエージェントContent Studioを自社で構築した。デザイナーの原則をスキルとして与え、スレッドごとのサンドボックスで作業させ、3,000件超の資産を生成し、1リクエストの費用は約$8から約50セントに下がった。

## 設計のポイント

- センスは文脈から来るため、デザイン原則と判断理由をスキルやチェックに書き込む。
- スレッドごとのサンドボックスでプロジェクト状態を保持し、自分のレンダリング結果を検査させる。
- 長時間ジョブは非同期サブエージェントで実行し、計画・進捗・承認をSlackに出して途中介入できるようにする。
- モデル弱点を補う規則は改善時に削除する。

## 使いどころ

- 社内の非専門職が、ブランドに沿った制作物を依頼する場面。
- 長時間のエージェント作業にチームで介入したいとき。
