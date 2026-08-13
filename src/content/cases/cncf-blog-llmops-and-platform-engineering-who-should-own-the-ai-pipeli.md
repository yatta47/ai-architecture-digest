---
type: opinion
title: LLMOpsパイプラインは誰が所有すべきか——プラットフォームエンジニアリングとの統合論
title_original: 'LLMOps and platform engineering: Who should own the AI pipeline?'
industry: cross-industry
cloud: []
patterns:
- llmops
- policy-as-code
components:
- Backstage
- Crossplane
- Kratix
- KubeVela
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/13/llmops-and-platform-engineering-who-should-own-the-ai-pipeline/
published_at: '2026-08-13'
---

## 概要

LLMOpsをDevOps・MLOpsと並ぶ第三の並行スタックにしてしまう「シャドーLLMOps」のリスクを指摘し、モデルのファインチューニングやベクトルDB、プロンプトレジストリ、推論エンドポイントをプラットフォームエンジニアリングが提供する一つのケーパビリティ層として統治すべきだと論じる。ガバナンスAPI、リクエスト時のポリシー適用、監査証跡の仕組みを具体的に提案する。

## 設計のポイント

- LLMOpsを独立王国にせず、既存のセルフサービスAPI（golden path）の一部としてプロンプト・モデル・推論エンドポイントを提供する
- コスト上限やデータレジデンシー、モデルアクセス制御をリクエスト時点でポリシーとして強制し、後追いのコスト超過を防ぐ
- PIIに触れる・自律的に意思決定するモデル変更には人間承認を必須にし、変更理由の監査証跡を残す

## 使いどころ

- DevOps・MLOps・LLMOpsが並行スタック化してガバナンスが効かなくなりつつあるプラットフォームチーム
- RAGパイプラインやベクトルストアが野良で乱立する「シャドーAI」を防ぎたい組織
