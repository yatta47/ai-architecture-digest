---
type: case
title: Agentforceの推論とレンダリングを分離する決定論的UI保証
title_original: How Agentforce Achieves 100% Deterministic Rendering for AI Agent UX
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- reasoning-computation-separation
- ai-agent
components:
- Salesforce Agentforce
- Agentforce Connections
outcome:
  type: reliability
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-agentforce-achieves-100-deterministic-rendering-for-ai-agent-ux/
published_at: '2026-09-03'
---

## 概要

Salesforce Agentforceは、LLMの確率的な推論を保ちながら必須フォームや規制開示など特定の重要なUIを100%決定論的にレンダリングするため、Agentforce Connectionsレイヤーで推論とレンダリング判断を分離し、render:ディレクティブでLLMにコンポーネント選択をさせず事前設定したレスポンスフォーマットを強制する仕組みを構築した。

## 設計のポイント

- LLMをより決定論的にするのではなく、決定論的である必要のあるレンダリング判断そのものをLLMの意思決定プロセスから切り離す
- render:ディレクティブでアクションごとにレスポンスフォーマットを事前定義し、該当アクション実行時はLLMのコンポーネント選択を経由させない
- 複数アクションが逐次実行される中で決定論的レンダリング対象のアクションを特定し、承認・完了後の正しいタイミングでコンポーネントを描画する順序制御を実装する

## 使いどころ

- 規制開示や必須フォームなど表示されないと業務が失敗する重要なUI要素を持つAIエージェント体験を本番導入したい場合
- Salesforce純正・サードパーティ・ヘッドレスなど複数チャネルで同じ決定論的レンダリングの保証を提供したいプラットフォームチーム
