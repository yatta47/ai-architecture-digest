---
type: announcement
title: LangChain開発者会議Interrupt 2025で発表されたエージェント基盤群
title_original: 'Recap of Interrupt 2025: The AI Agent Conference by LangChain'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- eval
- llmops
components:
- LangGraph Platform
- Open Agent Platform
- LangGraph Studio
- LangSmith
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/interrupt-2025-recap
published_at: '2026-06-15'
---

## 概要

LangChain初のカンファレンスInterrupt 2025で、長時間稼働するステートフルエージェントを1クリックでデプロイできる「LangGraph Platform」のGA、MCPツールやプロンプトをUIで組み合わせるノーコードの「Open Agent Platform」、Swarm/Supervisor/tool-calling agentなど定番構成を提供する「LangGraph Pre-Builts」、エージェント専用メトリクスやLLM-as-Judgeの人間フィードバックによる較正機能などが一斉に発表された。

## 設計のポイント

- 長時間稼働するステートフルなエージェントをCloud/Hybrid/セルフホストいずれでも1クリックでデプロイできる基盤を用意する
- Swarm・Supervisor・tool-calling agentなど頻出のマルチエージェント構成をプリビルドとして提供し実装コストを下げる
- MCPツール・モデル・データソースをUIで組み合わせるノーコードのエージェントビルダーを非エンジニア向けに用意する
- ツール呼び出しや行動経路(trajectory)を追跡できるエージェント専用メトリクスを観測基盤に組み込む

## 使いどころ

- 自前でエージェント基盤を組む前に定番アーキテクチャやデプロイ基盤を再利用したいチーム
- 非エンジニアもエージェントを構築できるようにしたい組織
- LLM-as-Judgeの品質を人間フィードバックで継続的に較正したいチーム
