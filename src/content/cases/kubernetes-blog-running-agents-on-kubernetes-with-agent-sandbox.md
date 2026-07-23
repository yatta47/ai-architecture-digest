---
type: announcement
title: 常駐AIエージェント向けの隔離実行環境を提供するKubernetes Agent Sandbox
title_original: Running Agents on Kubernetes with Agent Sandbox
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- unified-runtime
- confidential-computing
components:
- Kubernetes
- gVisor
- Kata Containers
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/
published_at: '2026-03-20'
---

## 概要

長時間稼働しほとんどアイドルなAIエージェントをKubernetesネイティブに扱うため、SIG Appsが新しいSandbox CRDを開発。gVisor/Kataによる強い隔離、ゼロへのスケールと高速再開、安定したホスト名を持つエージェント間通信を標準化する。

## 設計のポイント

- StatefulSet+headless Service+PVCの手組みではなく、シングルトンで状態を持つエージェント専用のCRDとして抽象化する
- SandboxWarmPoolで事前ウォームアップ済みPodのプールを維持し、コールドスタートによる会話の中断を防ぐ
- gVisorやKata Containersを使い分けられるようにし、エージェントが生成した未信頼コードの実行を強く隔離する

## 使いどころ

- 会話の合間は長時間アイドルになるが、呼び出し時は即座に応答が必要なエージェント基盤
- 複数の協調動作するエージェントに安定したネットワークIDを持たせて相互発見させたい多エージェントシステム
