---
type: guidance
title: 本番で重要な挙動から逆算するDeep Agentsの評価設計手法
title_original: How we build evals for Deep Agents
industry: cross-industry
cloud: []
patterns:
- eval
components:
- Deep Agents
- LangSmith
- BFCL
- Terminal Bench 2.0
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-we-build-evals-for-deep-agents
published_at: '2026-06-16'
---

## 概要

Deep Agentsチームが、評価を闇雲に増やすのではなく本番で重要な挙動をカタログ化してから狙って評価を設計する手法を解説。file_operations/retrieval/tool_use/memory等のカテゴリでタグ付けし、SDKの配線テストとモデル能力評価を分離することで、意味のあるシグナルだけを評価スコアに反映させる。

## 設計のポイント

- 場当たり的に評価を大量追加するのではなく、本番で重要な挙動をカタログ化してから狙って評価を設計する
- 評価をfile_operations/retrieval/tool_use/memory等のカテゴリでタグ付けし、集計ではなく挙動別に分析できるようにする
- SDKの配線テスト(unit/integration)とモデル能力評価を明確に分離し、スコアに無意味なノイズを混ぜない

## 使いどころ

- エージェントの評価スイートを設計・運用したいチーム
- 本番トレースを起点に継続的に評価を追加改善したい場合
