---
type: case
title: 連合型マルチエージェントで実現するヘルスケアナビゲーションAI「Dot」
title_original: How Included Health Built Federated Agents for Healthcare Navigation with Deep Agents and LangGraph
company: Included Health
industry: healthcare
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
- human-in-the-loop
- context-engineering
components:
- LangGraph
- Deep Agents
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-included-health-built-federated-agents-for-healthcare-navigation-with-deep-agents-and-langgraph
published_at: '2026-09-17'
---

## 概要

ヘルスケアナビゲーション企業Included Healthは、AIガイド「Dot」をLangGraphとDeep Agentsによる連合型マルチエージェント構成で構築した。中央のDotスーパーグラフが会話をルーティングしつつ、予約・専門医探し・行動健康など領域別サブワークフローに委譲し、Deep Agentsの共有ファイルシステムでトーンや会話コンテキストをチーム横断で一貫させている。臨床チームによるレビューで臨床ルーティングの一致率を95%以上に維持するフィードバックループも備える。

## 設計のポイント

- 各プロダクトチームが個別のサブワークフローを所有しつつ、共有プラットフォームプロンプトで声のトーンを統一する
- 会話をハンドオフする際は要約とファイルパスの両方を渡し、メンバーが繰り返し説明せずに済むようにする
- 保険適用可否などの共通機能をプラットフォーム・サブエージェント化し、全エージェントが継承できるようにする
- スキルを段階的開示のレジストリとして管理し、モデルが必要なスキルファイルのみを読み込む

## 使いどころ

- 固定的な意思決定木では対応しきれない、文脈依存の医療相談を扱いたいヘルスケアナビゲーション事業者
- 複数チームが個別に所有するサブシステムでも一貫した体験を保ちたいマルチエージェント運用
- 胸痛のような緊急性の高い訴えを初手で検知し適切に誘導する必要がある会話設計
- 人間のケアチームによる継続的なレビューでルーティング精度を維持したい規制産業
