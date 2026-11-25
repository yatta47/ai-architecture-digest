---
type: case
title: KubeCon基調講演でAIエージェントがドローンを実機操作するライブデモの舞台裏
title_original: '🚀 The story behind Drone 2: My KubeCon + CloudNativeCon North America 2026 keynote'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llm-gateway
- guardrails
components:
- Kubernetes
- agent-substrate
- kagent
- agentgateway
- OpenTelemetry
- Jaeger
- Keycloak
- MCP
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/11/25/%f0%9f%9a%80-the-story-behind-drone-2-my-kubecon-cloudnativecon-north-america-2026-keynote/
published_at: '2026-11-25'
---

## 概要

KubeCon NA 2026のクロージング基調講演で、AIエージェントがドローンを操作するライブデモを実施した舞台裏の記録。agent-substrateとkagentでエージェントを動かし、agentgatewayによるアクセス制御とOpenTelemetry/Jaegerによる可観測性を組み合わせた。

## 設計のポイント

- LLM・MCP・外向き通信を1つのゲートウェイ（agentgateway）に通し、レート制限・認証認可・ネットワークポリシーを集約する。
- エージェント実行をサンドボックス化し、物理デバイスを操作する際の影響範囲を限定する。
- ツール呼び出し時間やレート制限エラーをOpenTelemetryでトレースし、どこで時間を使っているかを追えるようにする。

## 使いどころ

- 物理デバイスや外部システムを操作するエージェントの安全策を設計するプラットフォームチーム。
- Kubernetes上でMCPツールの認可と可観測性を整えたい開発者。
