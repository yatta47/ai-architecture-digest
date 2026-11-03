---
type: announcement
title: OpenKruise Agents v0.6.0：エージェントサンドボックスのネットワーク制御とオートスケール
title_original: 'OpenKruise Agents v0.6.0: Leaping Ahead in Agent Sandbox Security and Automation'
company: OpenKruise
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- defense-in-depth
- cost-optimization
components:
- OpenKruise Agents
- Kubernetes
- Envoy
- Istio
- E2B
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/11/03/openkruise-agents-v0-6-0-leaping-ahead-in-agent-sandbox-security-and-automation/
published_at: '2026-11-03'
---

## 概要

KubernetesでAgent Sandboxを大規模運用するOpenKruise Agents v0.6.0が、L4/L7のネットワーク制御とMCPツール単位ACL、認証情報注入、ウォームプールの自動スケール、アイドル時の自動一時停止/再開を追加した。データプレーンを持つ構成へ進化している。

## 設計のポイント

- サンドボックスの出口通信をポリシー駆動のL7で制御し、MCPツール単位でACLを掛ける
- 認証情報はKubernetes Secretからプロキシが注入しエージェントコードに持たせない
- ウォームプールと自動一時停止/再開でアイドルのCPUを削減する

## 使いどころ

- コード実行エージェントを自社基盤で多数動かす基盤チーム
- サンドボックスのセキュリティと費用を両立したい運用者
