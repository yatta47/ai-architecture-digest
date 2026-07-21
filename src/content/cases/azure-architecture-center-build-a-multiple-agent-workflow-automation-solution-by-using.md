---
type: guidance
title: Microsoft Agent Frameworkで組む複数エージェントによる業務ワークフロー自動化基盤
title_original: Build a multiple-agent workflow automation solution by using Microsoft Agent Framework
industry: cross-industry
cloud:
- azure
patterns:
- multi-agent-orchestration
- ai-agent
- ci-cd
components:
- Microsoft Agent Framework
- Azure Container Apps
- Microsoft Foundry
- Azure Cosmos DB
- Azure Container Registry
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/idea/multiple-agent-workflow-automation
published_at: '2026-06-12'
---

## 概要

Container Apps上でホストする中央APIオーケストレータが、Microsoft Foundry上のGPT-4.1モデルと連携して複数の専門AIエージェントにタスクを分解・委譲し、計画から実行・検証までを協調させる業務自動化アーキテクチャ。過去・現在の計画やエージェントの意思決定履歴はAzure Cosmos DBに永続化し、GitHubからのビルドをContainer Registryにバージョン管理して継続的にデプロイする。

## 設計のポイント

- central APIオーケストレータでタスクを要素分解し、単一の汎用エージェントではなく複数の専門エージェントに委譲する構成にする
- エージェントの計画・実行結果・意思決定履歴をCosmos DBに永続化し、将来の学習や参照に使えるようにする
- GitHubトリガーのCI/CDでコンテナイメージをビルド・バージョン管理し、ロールバック可能な形でエージェント基盤をデプロイする
- コード主導のカスタムオーケストレーション（最大限の制御）と、マネージドなFoundry Agent Service（運用負荷軽減）をトレードオフとして比較検討する

## 使いどころ

- 組織内の多段階業務プロセスを複数の専門エージェントの協調で自動化したい企業
- エージェント基盤にもCI/CDやバージョン管理など通常のソフトウェア開発プラクティスを適用したいプラットフォームチーム
