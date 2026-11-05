---
type: case
title: NVIDIA社内のDGX SuperPOD運用を担う複数エージェント
title_original: How NVIDIA Uses AI Agents to Streamline AI Factory Operations
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- multi-agent-orchestration
- root-cause-analysis
- ai-agent
- human-in-the-loop
components:
- NVIDIA NemoClaw
- NVIDIA OpenShell
- NVIDIA Nemotron
- MCP
- Grafana
- Kubernetes
- NVIDIA DGX SuperPOD
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-nvidia-uses-ai-agents-to-streamline-ai-factory-operations/
published_at: '2026-11-04'
---

## 概要

NVIDIAが社内のDGX SuperPOD運用向けに作ったAI Factory Operations Agentの紹介。ジョブ復旧、ハードウェア、可観測性、Kubernetesなどの専門サブエージェントがMCP経由で連携し、計算・ネットワーク・ハード・スケジューラをまたいで原因を突き合わせて、チャットで推奨を示す。ローカルのNemotronで完全オンプレ稼働する。

## 設計のポイント

- エージェントの責務境界を明確にし、MCPツールの定義を厳密にする。
- まず読み取り専用で調査させて信頼を築き、推論の根拠を示してSREが確認してから動けるようにする。
- 層をまたぐ相関で、個別ツールでは見逃す原因を見つける。
- マルチテナントではエージェント・ツール・サンドボックス・Kubernetes権限を分け、OpenShellのカーネルレベル制限で隔離する。

## 使いどころ

- GPUクラスタの障害切り分けに時間を取られるSRE
- 機密性からオンプレでエージェントを動かしたい組織
