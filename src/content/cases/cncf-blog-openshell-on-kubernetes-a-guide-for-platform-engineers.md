---
type: guidance
title: KubernetesでAIエージェントを安全に動かすOpenShell
title_original: 'OpenShell on Kubernetes: a guide for platform engineers'
company: Nirmata
industry: cross-industry
cloud:
- on-prem
patterns:
- defense-in-depth
- policy-as-code
- ai-agent
components:
- OpenShell
- Agent Sandbox
- Kyverno
- Cilium
- Kubernetes
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/11/04/openshell-on-kubernetes-a-guide-for-platform-engineers/
published_at: '2026-11-04'
---

## 概要

NVIDIA発のCNCF SandboxプロジェクトOpenShellを、Kubernetes上でAgent Sandbox経由で動かす手引き。ファイルシステム・プロセス・ネットワーク・認証情報の4種の制御をYAMLで宣言し、バイナリやHTTPメソッド単位の許可をKyvernoのアドミッション検査と組み合わせる。

## 設計のポイント

- 信頼できる監督プロセスを外に置き、エージェントをサンドボックスに隔離する。
- APIキーはプレースホルダだけ見せ、許可された宛先でのみ実キーに置換する。
- NetworkPolicyでは足りないバイナリ・メソッド単位の制御を、実行中の更新も含めて行う。
- 既存のPod/Serviceなど標準リソースで運用する。

## 使いどころ

- 信頼できないコードを実行するエージェントを社内Kubernetesで運用するプラットフォームチーム。
- エージェントの外向き通信を細かく制限したいとき。
