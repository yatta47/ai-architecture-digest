---
type: guidance
title: エージェントのツール呼び出し(Function Calling)能力を測るベンチマーク
title_original: Benchmarking Agent Tool Use
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- llmops
components:
- GPT-4
- GPT-3.5
- Claude 2.1
- Mistral 7B
- Mixtral 8x7B
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/benchmarking-agent-tool-use
published_at: '2026-06-30'
---

## 概要

LangChainはエージェントのツール利用・Function Calling能力を測定するため、Typewriter・Relational Data・Multiverse Mathなど4種類のベンチマークタスクを新たに公開した。GPT-4やGPT-3.5、Claude-2.1、Mistral/Mixtral系のオープンソースモデルを比較したところ、複数ステップにわたるツール呼び出しの精度はモデルやタスクによって大きくばらつくことが分かった。関数呼び出しのスキーマ正しさは高くてもタスク全体の正解率は別問題であり、複数ステップのトラジェクトリ全体を評価する重要性を指摘している。

## 設計のポイント

- 正解率だけでなく環境の最終状態一致・中間ステップの順序一致・実行ステップ数の比率など複数の観点でエージェントの軌跡を評価する
- スキーマ整合性(function calling成功率)とタスク正解率を分けて計測しどちらが欠けているか切り分ける
- プロンプト戦略やモデルの事前学習バイアスがタスクによって性能を悪化させる場合があるため利用前に実タスクで検証する
- エージェント用にモデルをファインチューニングする場合は単発呼び出しだけでなく複数ステップのトラジェクトリで学習させる

## 使いどころ

- エージェントに組み込むLLMやプロンプト戦略を選定する前に実タスクで比較検証したいチーム
- Function Calling機能を持つモデルをエージェント用にファインチューニングしたい開発者
- 複数ステップの計画・ツール呼び出しが必要なワークフローを設計するアーキテクト
