---
type: case
title: スーパーバイザー型マルチエージェントからDeep Agentsへ、ApolloのGTM AIアシスタント刷新
title_original: How Apollo Rebuilt Its AI Assistant on Deep Agents to Power the Full GTM Loop
company: Apollo
industry: cross-industry
cloud:
- gcp
patterns:
- ai-agent
- multi-agent-orchestration
- llmops
- eval
components:
- Deep Agents
- LangGraph
- LangSmith
- Claude Agent SDK
- MCP
- Apollo CLI
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-apollo-rebuilt-its-ai-assistant-on-deep-agents-to-power-the-full-gtm-loop
published_at: '2026-07-21'
---

## 概要

GTMプラットフォームのApolloは、リード発見から結果測定までを1つのチャット型アシスタントで完結させるため、LangGraphベースのスーパーバイザー型マルチエージェントからDeep Agentsによるスキル選択型のフラットなアーキテクチャへ移行した。モデル中立性を理由にAnthropicのClaude Agent SDKではなくDeep Agentsを採用し、LangSmithを軸とした6層の評価フレームワーク「AI Watchtower」で品質を継続監視している。結果として確認プロンプトの削減とレイテンシ改善に加え、新規ユースケースの開発期間が80〜85%短縮された。

## 設計のポイント

- 固定的なスーパーバイザー/サブエージェントのグラフ構造をやめ、ユーザーの目標に応じて動的にスキルを選択・実行するフラットなDeep Agentsアーキテクチャへ移行し、新ユースケース追加のたびにグラフ配線を書き換える必要をなくした。
- 特定ベンダーに縛られるClaude Agent SDKではなく、モデル中立なDeep Agentsを選定し、将来的なLLMベンダー切り替えの余地を残した。
- 事前ルーブリック評価・E2Eゴールデンシナリオ・本番トレース・集計インサイト・週次サマリー・ユーザーのフィードバックからなる6層評価体制(AI Watchtower)をLangSmith上に構築し、品質劣化を多段階で検知できるようにした。
- アシスタントのロジックをUIから切り離し、同一エージェントを製品内チャットに加えてAPI・MCPサーバー・専用CLIからもヘッドレスに利用できるようにした。

## 使いどころ

- 多数のモジュールにまたがる操作を、自然言語での目標指定だけで一気通貫に実行させたいSaaS/GTMプラットフォーム。
- 新しいユースケースごとにオーケストレーショングラフを書き換えるコストを減らし、開発サイクルを高速化したいマルチエージェント開発チーム。
- 本番運用中のマルチエージェントシステムで、障害箇所をログの突き合わせなしにトレースベースで即座に特定したいチーム。
- 同一のAIアシスタントをUI・API・MCP・CLIなど複数のチャネルへ重複実装なしに展開したいプロダクトチーム。
