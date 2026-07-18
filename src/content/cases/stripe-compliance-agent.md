---
type: case
title: Stripeの金融コンプライアンスAI Agent
title_original: "How Stripe built a compliance review agent on Amazon Bedrock"
company: Stripe
industry: financial-services
cloud: [aws]
patterns: [ai-agent, rag, human-in-the-loop]
data_sources: [policy-documents, transaction-data]
components: [Amazon Bedrock, OpenSearch, ECS]
outcome: { type: productivity }
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/
published_at: 2026-07-18
---

## 概要

Stripe が社内のコンプライアンス審査を支援する AI エージェントを構築した事例。ポリシー文書と取引データを OpenSearch に索引し、Amazon Bedrock 上の LLM が RAG で根拠を引きながら審査ドラフトを生成する。最終判断は必ず人間のレビュー（human-in-the-loop）に戻す設計で、審査担当の生産性を高めた。

## 設計のポイント

RAG の出力をそのまま採用せず、人間レビューを最終ゲートに固定するのが肝。エージェントは「下書き係」に徹し、意思決定は人間に残すという責任分界を明確にしている。審査ドラフトに根拠リンク（引用元のポリシー・取引）を添えることで、後から追える監査証跡を自然に残せる。

## 使いどころ

規制産業で LLM を審査・監査ワークフローに組み込みたいとき。RAG に human-in-the-loop を必須で挟む構成や、監査証跡の残し方を検討している SRE / プラットフォーム担当。
