---
type: opinion
title: エージェント改善はトレースのデータマイニング問題である
title_original: Improving Agents is a Data Mining Problem
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- fine-tuning
- ai-agent
components:
- LangSmith Engine
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/improving-agents-is-a-data-mining-problem
published_at: '2026-07-08'
---

## 概要

LangChainのVivek Trivedy氏が、エージェントの継続学習は本質的に大量のトレースをマイニングしてシグナルを見つけるデータマイニング問題だと論じる。トレース判定用に小型オープンモデルをファインチューニングしてクローズドモデルより安価かつ高精度に運用する事例や、ハーネス改善とファインチューニングを交互に繰り返す「サンドイッチ戦略」でTerminal Bench 2.0のスコアを13.7%改善した例を紹介する。

## 設計のポイント

- 本番トレースを大量に収集・保存し、そこから改善すべき挙動のシグナルをマイニングする
- narrow taskではオープンな小型モデルをTrace judge用にファインチューニングし、クローズドな最先端モデルより低コストで高精度に運用する
- Harness Engineering→Fine-Tuning→Harness Engineeringのサンドイッチ戦略でエージェントを段階的に改善する
- 評価(evals)をエージェントの学習データそのものとして位置づけ、失敗事例を評価タスク化して改善ループに回す

## 使いどころ

- 大量のエージェントトレースを継続的な改善サイクルに組み込みたいプロダクトチーム
- 推論コストを抑えつつ特定タスクの精度を上げたいAI運用チーム
- ハーネス改善とモデルのファインチューニングのどちらを優先すべきか判断に迷うエンジニアリングチーム
