---
type: announcement
title: AIエージェントを統制するOpenShellがCNCF Sandboxへ
title_original: 'Welcoming OpenShell to the CNCF: open governance to secure agentic AI'
company: NVIDIA
industry: cross-industry
cloud:
- multi-cloud
patterns:
- guardrails
- policy-as-code
- defense-in-depth
components:
- OpenShell
- Cedar
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/11/10/welcoming-openshell-to-the-cncf-open-governance-to-secure-agentic-ai/
published_at: '2026-11-10'
---

## 概要

NVIDIAが寄贈したOpenShellはエージェントの振る舞いを監視し、ポリシーで権限境界を強制するオープンなランタイムである。ポリシー言語にCedarを採用し、エージェントの外側のインフラで強制する。

## 設計のポイント

- 統制をエージェントの外側に置く。
- Cedarでポリシーをコード化する。

## 使いどころ

- エージェントにデータやネットワークを安全に使わせたい企業
- ベンダー中立な統制層の標準化
