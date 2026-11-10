---
type: opinion
title: コーディングエージェントに委譲できるプラットフォームのガードレール設計
title_original: 'One flag, many guardrails: making a platform safe enough to delegate'
company: Akamai
industry: cross-industry
cloud:
- multi-cloud
patterns:
- guardrails
- policy-as-code
- human-in-the-loop
- defense-in-depth
components:
- GitOps
- Kubernetes
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/11/10/one-flag-many-guardrails-making-a-platform-safe-enough-to-delegate/
published_at: '2026-11-10'
---

## 概要

Akamaiの筆者は、エージェントにPRを任せられるかは、誤った変更をプラットフォームが吸収できるかの問題だと論じる。GitOpsは誤りも高速に広げるため、人でもエージェントでも同じ統制を最初から組み込むべきと述べる。

## 設計のポイント

- 統制は変更主体によらず同じルールを適用する。
- GitOpsの自動反映が誤りを増幅する点を前提にガードレールを置く。
- ポリシーをコード化して自動検証する。

## 使いどころ

- AIにインフラ変更PRを許可したいプラットフォームチーム
