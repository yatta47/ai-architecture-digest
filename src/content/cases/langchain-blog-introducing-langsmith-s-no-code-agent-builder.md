---
type: announcement
title: LangSmith Agent Builderが対話形式のプロンプト生成でノーコードのエージェント構築を非開発者にも開放
title_original: Introducing LangSmith's No Code Agent Builder
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- memory-consolidation
components:
- LangSmith
- LangGraph
- deepagents
- MCP
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-agent-builder
published_at: '2026-06-18'
---

## 概要

LangSmith Agent Builderは、ビジュアルワークフロービルダーではなく「エージェントビルダー」として、プロンプト・ツール・トリガー・サブエージェントの4要素からエージェントを組み立てるノーコード体験を提供する。白紙のキャンバスではなく対話形式で要件をヒアリングしながらシステムプロンプトを自動生成し、MCP経由で承認済みツールに接続、記憶機能によって過去の訂正を継続的に反映する。

## 設計のポイント

- 複雑さを固定的なビジュアルフローではなくプロンプトに集約し、LLMがより多くの意思決定を動的に担えるようにすることで、決められた経路をなぞるだけのワークフロービルダーの限界を超える。
- 白紙のキャンバスではなく対話から始め、要件を深掘りする質問を重ねてシステムプロンプト・ツール接続・トリガー設定を自動生成することで、プロンプトエンジニアリングの経験がなくても効果的なプロンプトを作れるようにする。
- エージェント自身がプロンプトとツールアクセスの両方について記憶を持ち、一度訂正された内容は以後のセッションでも再度指示せずに反映され続ける。

## 使いどころ

- プロンプトエンジニアリングの経験がない業務担当者が、メールやSlackアシスタントなど自分用のエージェントを作りたい場合。
- 複雑化したタスクをサブエージェントに分割し、システム全体の見通しを保ったまま拡張していきたいチーム。
- 承認済みのGmail・Slack・LinearなどのSaaSツールに、ガバナンスを保ったままエージェントを接続したい組織。
