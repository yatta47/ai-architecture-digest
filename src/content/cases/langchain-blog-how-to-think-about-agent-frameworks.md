---
type: opinion
title: エージェントフレームワークの本質は『各ステップでLLMに適切な文脈を渡す制御』
title_original: How to think about agent frameworks
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- LangGraph
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-to-think-about-agent-frameworks
published_at: '2026-06-15'
---

## 概要

LangChainのHarrison Chaseは、信頼できるエージェントシステムを作る本質的な難所は各ステップでLLMに適切な文脈を渡すことにあると論じる。多くのエージェントフレームワークは宣言的/命令的なオーケストレーションではなく単なる『エージェント抽象化』の集合に過ぎず、それが立ち上げを容易にする一方でコンテキスト制御を見えにくくすると指摘する。

## 設計のポイント

- システムを『ワークフロー』と『エージェント』の二択ではなく、両者が混在するグラデーションとして設計する
- 高レベルなエージェント抽象化は着手を早めるが、LLMに渡す文脈の内容やステップ順序を隠蔽しやすいトレードオフを理解して選ぶ
- 宣言的・命令的の両APIを持つ低レベルなオーケストレーション基盤を土台にし、その上に必要なエージェント抽象だけを積む
- 常にエージェントが必要なわけではなく、決定的で予測可能なワークフローで十分な場面ではそちらを選ぶ

## 使いどころ

- 乱立するエージェントフレームワークをどの軸で比較すべきか整理したいアーキテクト
- 既存フレームワークの抽象化がLLMへの文脈制御を妨げていないか見直したいチーム
