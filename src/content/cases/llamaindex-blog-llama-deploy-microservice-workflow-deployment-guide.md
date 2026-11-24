---
type: announcement
title: 'llama-deploy: LlamaIndex Workflowsをマイクロサービスとして配備'
title_original: 'Introducing llama-deploy: A Microservice-based Way to Deploy LlamaIndex Workflows'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- event-driven
- ai-agent
components:
- llama-deploy
- LlamaIndex Workflows
- llama-agents
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-llama-deploy-a-microservice-based-way-to-deploy-llamaindex-workflows
published_at: '2024-09-05'
---

## 概要

llama-deployは、llama-indexのWorkflowsを少ないコードでスケール可能なマイクロサービスとして起動する仕組み。すべて非同期で、各サービスが独立してスケールし、中央のコントロールプレーンがメッセージキューと状態・サービス登録を管理する。

## 設計のポイント

- エージェントや処理を独立したマイクロサービスにし、個別にスケールできる。
- メッセージキューとコントロールプレーンに通信と状態管理を集約している。
- イベント駆動のWorkflowsと配備方式を組み合わせ、開発と本番の差を小さくしている。

## 使いどころ

- マルチエージェントを本番運用し、耐障害性や拡張性が必要なチーム。
- ローカルで作ったワークフローをそのままサービス化したい場合。
