---
type: opinion
title: オープンモデルがエージェントの中核タスクでクローズドに並んだ
title_original: Open models have crossed a threshold
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- multi-model-routing
- cost-optimization
components:
- Deep Agents
- GLM-5
- MiniMax M2.7
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/open-models-have-crossed-a-threshold
published_at: '2026-10-13'
---

## 概要

LangChainはDeep Agentsの評価で、GLM-5とMiniMax M2.7がファイル操作・ツール利用・指示追従でクローズドの先端モデルと同等と報告した。コストは8〜10倍安く、レイテンシも低い。

## 設計のポイント

- コストとレイテンシの制約から、先端モデルを全タスクに使わず使い分ける。
- 高速推論プロバイダ上のオープンモデルで応答速度を確保する。
- 評価をカテゴリ別に実施して採否を判断する。

## 使いどころ

- 高スループットのエージェントでコストを下げたいチーム。
