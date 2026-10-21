---
type: guidance
title: NVIDIA OpenShell参照アーキテクチャによるAIエージェントの安全な統制
title_original: How NVIDIA OpenShell Reference Architecture Secures and Governs AI Agent Workloads at Scale
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- defense-in-depth
- guardrails
- policy-as-code
- ai-agent
components:
- NVIDIA OpenShell
- NVIDIA Vera CPU
- BlueField-4
- NVIDIA Sentry
- CoreWeave
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-nvidia-openshell-reference-architecture-secures-and-governs-ai-agent-workloads-at-scale/
published_at: '2026-10-21'
---

## 概要

OpenShellはエージェントを非信頼ワークロードとして扱うオープンソースのランタイムで、Gateway・Supervisor・Sandbox・Policy Proverで統制する。Vera CPU上でCoreWeaveはサンドボックス起動3倍超、エージェントループ1.8倍の高速化を測定した。

## 設計のポイント

- 統制をエージェント自身ではなくインフラ側に置く。
- Supervisorを隔離し資格情報の仲介とアウトバウンド検査を行う。
- Policy Proverでポリシー権限が組織の上限内か形式検証する。
- ミドルウェアやインターセプタで拡張可能にしている。

## 使いどころ

- 長時間自律動作するエージェントの権限管理。
- 大量の同時エージェント環境を高密度に運用する基盤設計。
