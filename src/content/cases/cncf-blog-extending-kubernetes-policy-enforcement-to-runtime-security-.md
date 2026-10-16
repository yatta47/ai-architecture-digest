---
type: announcement
title: AIエージェント向けにKyvernoのポリシーをランタイムへ拡張
title_original: Extending Kubernetes Policy Enforcement to Runtime Security for AI Workloads
company: Nirmata
industry: cross-industry
cloud: []
patterns:
- policy-as-code
- defense-in-depth
- guardrails
- ai-agent
components:
- Kyverno
- Nirmata Runtime for Kyverno
- eBPF
- BPF-LSM
- OpenReports
- CEL
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/15/extending-kubernetes-policy-enforcement-to-runtime-security-for-ai-workloads/
published_at: '2026-10-15'
---

## 概要

Nirmata Runtime for KyvernoはeBPFとLSMでカーネル内のexec・open・network判定を行い、admission controlでは見えない実行時の挙動を制御する。AIエージェントのように実行時に挙動が決まるワークロードにも使える。

## 設計のポイント

- 制御をワークロードの下層（カーネル）に置き、侵害されたワークロードに迂回されないようにする。
- admissionと同じCELとOpenReportsを使い、ポリシー体系を一本化する。
- 既定はmonitorモードで、WouldDenyを確認してからenforceに切り替える。

## 使いどころ

- プロンプトインジェクション等に備えるエージェント基盤のセキュリティ担当。
- 既存のKyverno運用を実行時制御へ広げたい場面。
