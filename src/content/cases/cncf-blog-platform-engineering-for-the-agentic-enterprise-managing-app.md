---
type: opinion
title: AIエージェントを一級市民として扱う次世代プラットフォームエンジニアリング
title_original: 'Platform Engineering for the Agentic Enterprise: Managing Applications, Resources, and AI Agents'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- policy-as-code
- guardrails
components: []
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/21/platform-engineering-for-the-agentic-enterprise-managing-applications-resources-and-ai-agents/
published_at: '2026-07-21'
---

## 概要

従来の内部開発者プラットフォーム(IDP)は人間の開発者を前提に設計されてきたが、AIエージェントがインフラ提供・デプロイ・障害調査などを自律的に行う「エージェント企業」では、プラットフォームはアプリケーションだけでなくリソースとAIエージェント自体を一級のソフトウェア資産として管理する必要があると論じる。人間とAIエージェントそれぞれに個別のID・権限範囲・監査証跡を与えつつ、同じガバナンスモデルで統制することが鍵になる。

## 設計のポイント

- ポータルを使う開発者、CLI/GitOpsを使うSRE、MCPサーバーを呼ぶAIエージェントなど、インターフェースは主体ごとに異なっても、セキュリティ統制とポリシー境界は一貫させる。
- アプリケーションだけでなく、データベースやAIモデルなどの「リソース」とAIエージェント自体をプラットフォームが管理する一級オブジェクトとして扱う。
- AIエージェントには人間と同様に固有のID・スコープ付き権限・監査ログを付与し、誰が何をしたかを追跡可能にする。

## 使いどころ

- AIエージェントに本番インフラの操作権限を与え始めている組織のプラットフォームチーム。
- 人間とエージェント混在のオペレーションで、統一されたガバナンスと監査証跡を必要とするエンタープライズ。
