---
type: guidance
title: Oracle Cloud上にAI-Qブループリントをデプロイする本番向けマルチエージェント基盤
title_original: Deploy a Production-Ready NVIDIA AI-Q Blueprint on Oracle Cloud Infrastructure
industry: cross-industry
cloud:
- oci
patterns:
- multi-agent-orchestration
- rag
- ai-agent
components:
- NVIDIA AI-Q Blueprint
- LangChain Deep Agents
- NVIDIA NeMo Agent Toolkit
- Oracle Kubernetes Engine
- Terraform
- Helm
- PostgreSQL
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/deploy-a-production-ready-nvidia-ai-q-blueprint-on-oracle-cloud-infrastructure/
published_at: '2026-07-09'
---

## 概要

NVIDIA AI-Q BlueprintはLangChain Deep AgentsとNeMo Agent Toolkit上に構築された長期稼働エージェントのオープンソースリファレンスで、意図ルータが高速な簡易調査エージェントと計画・調査サブエージェントを持つDeep Agentへリクエストを振り分ける。本記事はTerraformでOCIインフラを、HelmでOKE上のワークロードを構築し、約20〜25分でAI-Qエンドポイントを本番相当に立ち上げる手順を示す。

## 設計のポイント

- 意図ルータでShallow Research(高速・限定ツール)とDeep Agent(計画+調査サブエージェント+ファイルシステム共有)を切り替える
- インフラ(Terraform)とアプリケーション(Helm)を分離し、terraform destroy一発で環境を完全撤去できる再現性を持たせる
- モデル・ツール・RAGバックエンド・サブエージェント・評価器はYAML設定またはNeMo Agent Toolkitのプラグイン機構で差し替え可能にする

## 使いどころ

- 自社のOCIテナンシ内で引用付きの調査レポート生成エージェントを自己ホストしたいプラットフォームエンジニア
- Kubernetes/Terraform/Helmに慣れたチームがラップトップではなくクラウド上でマルチエージェント基盤を検証したい場合
