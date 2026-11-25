---
type: announcement
title: 'LlamaIndex週報: マルチエージェントのKubernetes展開とRabbitMQ連携'
title_original: LlamaIndex Newsletter 2024-07-09
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- rag
- event-driven
components:
- llama-agents
- Kubernetes
- Docker Compose
- RabbitMQ
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-07-09
published_at: '2024-07-09'
---

## 概要

llama-agents向けのKubernetesスターターキットとRabbitMQ連携、Reflection・Corrective RAGをサービス化するガイドなどを紹介する週次ニュースレター。

## 設計のポイント

- 出力検証や修正を独立サービスにして複数エージェントで共用する。
- 検索結果の関連性を生成前に確認し、不足時はWeb検索で補う。

## 使いどころ

- マルチエージェントを本番運用へ移したいチーム。
- エージェントの信頼性を高める構成を探す開発者。
