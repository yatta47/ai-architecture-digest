---
type: case
title: 投資家向けAIアシスタントをマルチグラフ構成からDeep Agentsに全面刷新
title_original: How Harmonic Rebuilt Scout on Deep Agents and 4x'd Retention with LangSmith
company: Harmonic
industry: financial-services
cloud: []
patterns:
- ai-agent
- context-engineering
- llmops
components:
- LangSmith
- LangGraph
- Deep Agents
- LangSmith Deployment
outcome:
  type: revenue
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-harmonic-rebuilt-scout-on-deep-agents-and-4xd-retention-with-langsmith
published_at: '2026-08-26'
---

## 概要

VC向けデータプラットフォームHarmonicのAIアシスタント「Scout」は、当初LangGraph上の複数サブグラフとノード単位の大量evalで構築されていたが、想定外の意図には対応できず保守負荷も高かった。V2では単一のフロンティアモデルをDeep Agentsハーネス上で動かし、グローバルデータ層と顧客固有データにアクセスするツール群だけを与えるシンプルな構成に刷新し、可視化や検索結果をモデルも参照できる共有コンテキストとして扱うことでUXの断絶を解消、開発速度とリテンションを大きく改善した。

## 設計のポイント

- 固定的な複数サブグラフ+ノード単位evalの構成から、単一フロンティアモデルとツール群のみで動くシンプルなDeep Agents構成へ移行し、新機能追加のたびにサブグラフを作る必要をなくした。
- 『ユーザーに見えるものは全てモデルも参照できるようにする』という設計原則を徹底し、可視化やUI上のアーティファクトをモデルとユーザーが同じ会話コンテキストで共有できるようにした。
- モデルが生成したSVGなどの可視化をチャット内の一次的な要素として直接レンダリングし、専用のチャート機能を個別開発しなくても多様な可視化要求に対応できるようにした。
- 大量の検索結果は共有ファイルシステムに書き出し、モデルがオンデマンドでページングして参照できるツールを用意することで、結果セットに関する後続の質問にも答えられるようにした。

## 使いどころ

- 固定ワークフローでは対応しきれない、自由記述の調査・分析依頼が多いドメイン特化型データプロダクトのAIアシスタント刷新。
- チャットUIとエージェントの認識にズレが生じやすい、可視化やリッチな検索結果を扱うプロダクトのUX設計。
- 少人数の開発チームで本番運用の耐久性・観測性を確保しつつ、頻繁なプロダクトイテレーションを行いたい場合。
