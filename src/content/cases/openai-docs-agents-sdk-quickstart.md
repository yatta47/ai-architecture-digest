---
type: guidance
title: OpenAI Agents SDKで最小構成のエージェントを構築するクイックスタート
title_original: Quickstart
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- OpenAI Agents SDK
- Runner
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://openai.github.io/openai-agents-python/quickstart/
published_at: '2025-07-21'
---

## 概要

openai-agents PythonパッケージをインストールしAgentにinstructions・name・モデルを与えるだけで、Runner.runを呼び出して即座にエージェントを実行できる。2ターン目以降はresult.to_input_list()を次の入力に渡すか、セッションをアタッチすることで会話状態を維持する。

## 設計のポイント

- エージェント定義はinstructions・name・任意のモデル指定という最小限の構成で始められる。
- マルチターン会話はto_input_list()による手動の状態引き回しか、セッション機構のいずれかで維持する。

## 使いどころ

- エージェントSDKを初めて触るチームがまず動くものを最短で立ち上げたい場合。
- シンプルなQ&Aエージェントのプロトタイピング。
