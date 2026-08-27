---
type: opinion
title: OpenAIのAssistants API/GPTsが体現する『閉じた認知アーキテクチャ』への賭け
title_original: OpenAI's Bet on a Cognitive Architecture
industry: cross-industry
cloud: []
patterns:
- ai-agent
components: []
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/openais-bet-on-a-cognitive-architecture
published_at: '2026-08-26'
---

## 概要

LangChain創業者Harrison Chaseは、OpenAIが発表したAssistants APIとGPTsが共に「LLM自身が遷移を全て決めるエージェント型」という同じ認知アーキテクチャへの賭けであると分析する。単一LLM呼び出しからチェーン、ルーター、ステートマシン、エージェントまでの認知アーキテクチャの段階を整理し、OpenGPTsのような、企業が自分たちで認知アーキテクチャを制御できるオープンな代替案の重要性を論じている。

## 設計のポイント

- LLMアプリの「認知アーキテクチャ」を、単一LLM呼び出し→チェーン→ルーター→ステートマシン→エージェントという制御の委譲度で段階的に整理するフレームワークを提示した
- エージェント型アーキテクチャを「LLM呼び出し→アクション実行→観測結果をプロンプトに追加して再度LLM呼び出し」というループとして定式化した
- 特定ベンダーの閉じた認知アーキテクチャに依存するのではなく、企業が自社のユースケースに合わせて認知アーキテクチャ自体を選択・制御できるようにすべきだと主張した

## 使いどころ

- 自社のLLMアプリにどの程度エージェント的な自律性を持たせるべきか設計判断をしたいチーム
- OpenAIのAssistants API/GPTsとオープンな自前実装（OpenGPTsなど）を比較検討している開発者
