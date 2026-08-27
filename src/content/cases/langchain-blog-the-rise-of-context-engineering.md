---
type: opinion
title: 『コンテキストエンジニアリング』の台頭——エージェントに正しい情報とツールを届ける設計論
title_original: The rise of "context engineering"
company: LangChain
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
components:
- LangGraph
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/the-rise-of-context-engineering
published_at: '2026-08-25'
---

## 概要

LangChainのHarrison Chaseは、エージェントが失敗する主因はモデル性能不足ではなく『正しい情報・ツールを正しい形式で届けられていないこと』にあると論じ、これを動的にコンテキストを組み立てる仕組みという意味で『コンテキストエンジニアリング』と呼ぶ。プロンプトエンジニアリングをその一部と位置づけ、低レベルで制御可能なLangGraphと、実際にモデルへ渡った入出力を可視化するLangSmithのトレースが、この設計を実践する土台になるとする。

## 設計のポイント

- エージェントの失敗を『モデル自体の能力不足』と『適切なコンテキストが渡っていない』の2種類に切り分け、原因ごとに異なる対処をする
- コンテキストは静的なプロンプト文字列ではなく、ツール出力・記憶・検索結果・過去の会話などから動的に組み立てる『システム』として設計する
- モデルへ渡す情報の形式（簡潔で構造化されたメッセージ vs 巨大なJSONブロブ）そのものが応答品質を左右すると捉え、フォーマットを意図的に設計する
- 何がLLMに渡っているかを完全にコントロールできる低レベルなエージェントフレームワークを選び、抽象化によって渡す内容を制御できなくなる事態を避ける

## 使いどころ

- 不安定なエージェントの失敗原因が『コンテキスト不足』か『モデル限界』かを切り分けて診断したいAIエンジニア
- プロンプトの言い回しの調整ではなく、ツール・記憶・検索を含むコンテキスト供給の仕組みそのものから設計し直したいチーム
