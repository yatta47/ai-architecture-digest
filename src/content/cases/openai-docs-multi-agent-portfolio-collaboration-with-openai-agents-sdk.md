---
type: guidance
title: OpenAI Agents SDKで作るマルチエージェント型ポートフォリオ分析システム
title_original: Multi-Agent Portfolio Collaboration with OpenAI Agents SDK
industry: financial-services
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
components:
- OpenAI Agents SDK
- MCP
- Code Interpreter
- WebSearch
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/agents_sdk/multi-agent-portfolio-collaboration/multi_agent_portfolio_collaboration/
published_at: '2025-05-28'
---

## 概要

マクロ・ファンダメンタルズ・クオンツの専門エージェントをPortfolio Managerエージェントが「ツールとして」呼び出すhub-and-spoke構成で、投資リサーチを協調的に処理するマルチエージェントシステムの構築方法を解説する。MCPサーバー、コードインタープリタ、Web検索など複数のツール種別を単一のワークフローに統合している。

## 設計のポイント

- エージェントを「ツールとして」呼び出すagent-as-toolパターンを採用し、単一の制御スレッドで透明性の高いオーケストレーションを維持する
- MCPサーバー・マネージドツール・カスタムPython関数を組み合わせ、専門領域ごとにエージェントの役割を分離する
- 各専門エージェントの結果をPortfolio Managerが並列実行させたうえで統合し、最終回答を合成する

## 使いどころ

- 単一プロンプトでは扱いきれない複雑な調査・分析タスクを複数の専門エージェントに分担させたい場合
- 外部データソース（金融データAPIなど）と連携しつつ監査可能なマルチエージェントワークフローを構築したい開発者
