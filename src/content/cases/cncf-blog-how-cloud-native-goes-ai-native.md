---
type: opinion
title: AIエージェントが生成するインフラとクラウドネイティブの標準をどう両立させるか
title_original: How Cloud Native Goes AI-Native
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- policy-as-code
- guardrails
components:
- Kubernetes
- Prometheus
- OpenTelemetry
- Istio
- OPA
- Supabase
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/09/09/how-cloud-native-goes-ai-native/
published_at: '2026-09-09'
---

## 概要

AIエージェントによる「vibe coding」はデモの完成までは高速だが、行レベルセキュリティの欠如や本番DB削除事故など、クラウドネイティブが20年かけて積み上げた本番運用の知見（mTLS・最小権限・オートスケーリング・可観測性）を軽視しがちだと指摘する。著者は、エージェントにとって安価で扱いやすい宣言的インターフェースやポリシーエンジンを整備し、人間同様にエージェントも「本番の型」に従わせるべきだと論じる。

## 設計のポイント

- エージェントは「コンテキストを最も消費しない選択肢」を本番適格性より優先するため、安全側のデフォルトをエージェントにとっても最も低コストな選択肢にする必要がある。
- 宣言的インターフェースとポリシーエンジンで、悪いマニフェストをデプロイ前に機械的に拒否する仕組みを用意する。
- 人間の規律を保ってきたreconciliationループ（Kubernetesのようなオペレーターパターン）を、エージェントの行動を律する仕組みとしても使う。

## 使いどころ

- AIコーディングエージェントが生成したインフラ構成を本番投入する前にガードレールを設けたいプラットフォームチーム。
- vibe codingで作られたプロトタイプを、セキュリティ・可観測性を落とさずに本番運用へ引き上げたい場合。
