---
type: guidance
title: エージェントのコストを下げるコンテキストエンジニアリング設計論
title_original: 'The Economics of Agent Optimization: Context engineering for enterprise AI agents'
industry: cross-industry
cloud:
- azure
patterns:
- context-engineering
- rag
- cost-optimization
- ai-agent
components:
- Microsoft Foundry
- Foundry IQ
- Toolboxes
- Model Context Protocol (MCP)
outcome:
  type: cost
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/the-economics-of-agent-optimization-context-engineering-for-enterprise-ai-agents/
published_at: '2026-09-02'
---

## 概要

エージェントの運用コストの多くはコンテキストウィンドウに何を積むかで決まるとし、「何を知るべきか」「何に到達できるべきか」「どう作業すべきか」の3つの観点でコンテキストを絞り込む設計指針を提示する。Foundry IQによる知識の一元管理、Toolboxesのtool searchによるツール一覧の動的絞り込み、手順をSkillとして中央管理する仕組みにより、品質を落とさずコストを下げられるとしている。

## 設計のポイント

- 知識ベースを各エージェントに埋め込まず、複数エージェントで再利用可能な共有の管理レイヤー(Foundry IQ)に切り出す
- 全ツール定義を毎ターン渡すのではなく、tool searchで必要なツールだけを動的に取得しトークン量を一定に保つ
- 業務手順をSkillとして中央管理し、更新時に全エージェントへ再デプロイなしで反映されるようにする

## 使いどころ

- 多数のエージェントを運用し、コンテキスト肥大化でコストが膨らんでいる企業
- 接続ツール数が増えて精度や応答速度が落ちているエージェント基盤
- レビュー基準や手順を複数エージェント・チーム間で一貫させたい組織
