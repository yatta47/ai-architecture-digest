---
type: case
title: Blockの共同作業空間Buzzとモデル統合ゲートウェイUnity Gateway
title_original: How Block powers collaborative AI agents with Buzz and Unity Gateway
company: Block
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- ai-agent
- multi-model-routing
components:
- Buzz
- Databricks Unity Gateway
- Goose
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-block-powers-collaborative-ai-agents-buzz-and-unity-gateway
published_at: '2026-11-12'
---

## 概要

Blockは社員とAIエージェントが同じ場で協働できるOSSのBuzzを開発し、Databricks Unity Gateway経由で多数の商用・オープンモデルを単一統合で提供している。モデルやエージェントハーネスをタスクごとに選べる。

## 設計のポイント

- モデル接続をゲートウェイに集約し、複数モデルへ単一統合でアクセスさせる。
- モデルとハーネスを利用者が選べるようにし、効率フロンティアで使い分ける。
- OSSでセルフホスト可能にして、閉域利用にも対応する。

## 使いどころ

- 複数モデルを社内で使い分けたい企業。
- 人とエージェントが同じ会話で作業する環境を作りたいチーム。
- モデル接続の統制を一元化したい基盤担当。
