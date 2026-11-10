---
type: announcement
title: Kubernetes上でエージェントを高密度に動かすAgent Substrate
title_original: 'Agent Substrate: Advancing Kubernetes for Agents at Scale'
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- unified-runtime
- inference-optimization
components:
- Agent Substrate
- NVIDIA Dynamo
- KAI Scheduler
- Kubernetes
- NVIDIA DSX AI Factory
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/agent-substrate-advancing-kubernetes-for-agents-at-scale/
published_at: '2026-11-10'
---

## 概要

Agent Substrateは多数のエージェントセッションを少数のウォームなワーカーPodに多重化し、アイドル時はメモリとファイルシステムごとチェックポイントして空きワーカーに復元する。DynamoのKVキャッシュ位置や推論待ち情報と連携し、常駐・中断・再開を決める。CNCF Sandboxに寄贈された。

## 設計のポイント

- アイドルが大半のエージェントをチェックポイントし、Pod常駐のコストとコールドスタートを回避する。
- 推論基盤(Dynamo)から時間見積りや飽和度を受け取り、セッションの常駐判断に使う。
- スケジューラ(KAI)でエージェントワーカーとGPU学習・推論を同一クラスタに配置する。

## 使いどころ

- コーディングエージェントを大規模に提供する基盤
- RL後学習の環境や短命GPUサンドボックスの運用
