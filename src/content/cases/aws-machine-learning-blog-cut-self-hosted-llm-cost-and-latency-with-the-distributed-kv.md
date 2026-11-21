---
type: guidance
title: 分散KVキャッシュでセルフホストLLMの推論コストを下げる手順
title_original: Cut self-hosted LLM cost and latency with the distributed KV caching agent skill
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
- ai-agent
components:
- Amazon ElastiCache
- KVTrace
- Agent Toolkit for AWS
- Elastic Fabric Adapter
- Kiro
- Claude Code
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/cut-self-hosted-llm-cost-and-latency-with-the-distributed-kv-caching-agent-skill/
published_at: '2026-11-21'
---

## 概要

セルフホストLLMではサーバごとのGPUローカルキャッシュが共有されず、再開した会話でプリフィルを再計算する無駄が出る。ElastiCacheによる分散KVキャッシュで推論コストを最大40%、TTFTを最大80%削減でき、導入判断から構築、障害対応までをコーディングエージェントのスキルが案内する。

## 設計のポイント

- GPUローカルのキャッシュの外側に共有層を置き、どのサーバでもKV状態を再利用できるようにしている。
- 投資前にKVTraceで自社のモデルとトラフィックから効果を見積もり、短いプロンプトでは再計算の方が速いという切り替え点を考慮している。
- 変更前に読み取り専用APIでGPUフリートとEFAの有無を確認し、適合しなければ止まる。

## 使いどころ

- 長い会話履歴を持つ法務アシスタントやコーディングエージェントのTTFTを縮めたいとき。
- GPUの冗長な再計算を減らしてセルフホスト推論のコストを抑えたいとき。
- キャッシュ導入の費用対効果を事前に見積もりたいとき。
