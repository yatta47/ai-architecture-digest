---
type: guidance
title: LlamaParseのSaaS・VPC・オンプレを選べる柔軟なデプロイ構成
title_original: How to flexibly deploy LlamaParse wherever your data lives
company: LlamaIndex
industry: cross-industry
cloud:
- aws
- azure
- gcp
- on-prem
patterns:
- document-processing
- multi-tenant-rag
components:
- LlamaParse
- Kubernetes
- Helm
- AWS PrivateLink
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/how-to-flexibly-deploy-llamaparse-wherever-your-data-lives
published_at: '2026-11-09'
---

## 概要

LlamaParseはSaaS、顧客VPC（BYOC）、オンプレミスの3形態で同じ解析エンジンを動かせる。推論はLlamaIndex管理と顧客管理から選べ、VPC構成ではハイブリッド運用を推奨している。

## 設計のポイント

- プラットフォームと推論基盤を分離し、文書保管は顧客環境、GPU運用はベンダー側という分担にできる
- KubernetesのHelmチャートで顧客環境にデプロイする
- エアギャップ環境では管理型推論が使えない制約を踏まえて構成を選ぶ

## 使いどころ

- 機微な文書をAWSやAzureの自社アカウント内に置きたい企業
- GPUの調達や運用を避けつつデータ所在を管理したい場面
- 完全閉域のオンプレ環境で文書AIを使いたい組織
