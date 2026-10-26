---
type: guidance
title: KubernetesでAIエージェントを隔離実行するkagentとAgent Substrate
title_original: Isolation, security, scale
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- defense-in-depth
- guardrails
- multi-agent-orchestration
components:
- kagent
- Agent Substrate
- Kubernetes
- gVisor
- microVM
- Helm
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/26/isolation-security-scale/
published_at: '2026-10-26'
---

## 概要

通常のコンテナによるサンドボックスは出入りが開放的で、エージェントの実行には不十分である。Agent SubstrateのWorker(Pod)とActorにgVisorとmicroVMの二段の隔離を持たせ、kagentを宣言的なランタイムとして使う構成を、導入手順とともに解説する。

## 設計のポイント

- gVisor(ユーザー空間カーネル)による隔離とmicroVMによるハードウェア隔離を使い分け、信頼できないエージェントコードをホストから切り離す。
- AIゲートウェイでポリシーを強制し、エージェントの通信先を制御する。
- エージェントのスナップショットで中断箇所から再開でき、マルチテナントのルーティングも境界で分離する。
- AgentTemplateをゴールデンイメージとして、エージェントを宣言的に作成する。

## 使いどころ

- 信頼できないコードやツール呼び出しを行うエージェントを共有クラスタで動かすプラットフォームチーム。
- マルチテナントでエージェントを提供し、爆発半径を抑えたい場面。
- LangGraphやADKで作った自作エージェントをKubernetes上で統制して動かしたいチーム。
