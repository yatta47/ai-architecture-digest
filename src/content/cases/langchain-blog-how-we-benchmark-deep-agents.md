---
type: guidance
title: LangChainがDeep Agentsをどうベンチマークしているか
title_original: How We Benchmark Deep Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
components:
- Deep Agents
- Harbor
- LangSmith
- LangSmith Sandboxes
- Terminal-Bench
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-we-benchmark-deep-agents
published_at: '2026-07-24'
---

## 概要

オープンソースのエージェントハーネスDeep Agentsの意思決定を検証するため、LangChainはHarborを使った3種類のエンドツーエンドベンチマーク(自律作業・会話・検索)を整備した。環境ごとDockerで再現し、成果物をスクリプトで判定する点が単純なLLM評価と異なる。

## 設計のポイント

- 各タスクをDockerfile/指示文/評価スクリプトの3点セットで定義し、エージェントの成果物ごと自動判定する
- 非決定的な挙動のばらつきを補正するため各タスクを複数回実行し、平均で品質を見積もる
- 本番の全量ベンチマークとは別に、難しいが解けるタスクに絞った8倍速・6倍安価な軽量ベンチマークをイテレーション用に維持する
- ツール選択やメモリなど特定のハーネス挙動を検証する高速な決定的ユニットテスト群を統合テストの下位層として併用する

## 使いどころ

- エージェントハーネスのプロンプトやミドルウェアを削ぎ落とす際に回帰がないか確認したい開発チーム
- モデル非依存のエージェント基盤をリリース前に定量的な自信を持って検証したい場合
