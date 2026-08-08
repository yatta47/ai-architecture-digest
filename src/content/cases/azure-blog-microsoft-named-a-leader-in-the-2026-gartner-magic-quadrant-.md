---
type: case
title: GitHub Copilotによるエージェント型コードモダナイゼーションの二層アーキテクチャ
title_original: Microsoft named a Leader in the 2026 Gartner Magic Quadrant for AI-Augmented Code Modernization Tools
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
- ci-cd
components:
- GitHub Copilot
- Azure Copilot
- Modernize CLI
- Azure App Service
- Azure Container Apps
- Azure Kubernetes Service
- Microsoft Foundry
- Microsoft IQ
outcome:
  type: speed
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/microsoft-named-a-leader-in-the-2026-gartner-magic-quadrant-for-ai-augmented-code-modernization-tools/
published_at: '2026-08-06'
---

## 概要

MicrosoftはGartnerのAI活用コードモダナイゼーションツール部門でLeaderに選出され、その中核であるGitHub Copilotモダナイゼーションのアーキテクチャを紹介している。Modernize CLI上のモダナイゼーションエージェントが多数のアプリケーションを横断してアセスメント・計画・フレームワークアップグレードを自動化し、IDE内のGitHub Copilotがその計画に沿ってランタイム更新や依存関係移行、IaC生成、デプロイを実行する二層構成になっている。SAP Labsの事例ではJavaモダナイゼーションの所要時間が数日から数時間に短縮された。

## 設計のポイント

- 全社横断の計画立案（Modernize CLI上のエージェント）と個別アプリでの実行（IDE内のGitHub Copilot）を分離し、大規模ポートフォリオでも一貫した計画を保てるようにした。
- マネージドID・Key Vault・Blob/Fileストレージなど頻出移行パターンを定型タスク化し、さらに自社固有の移行パターンをカスタムスキルとして再利用可能にした。
- ビルド検証・単体テスト移行・アップグレード後のCVEスキャンと修正をエージェントのワークフローに組み込み、モダナイゼーション後ではなく過程の一部としてセキュリティを担保した。
- 推奨内容の透明性とレビュー可能性を保ち、既存のテスト・パイプラインで検証しながら人が最終判断を下す設計を維持した。

## 使いどころ

- レガシーな.NET Framework・Javaアプリケーションを多数抱え、モダナイゼーションを個別対応ではなく再現可能なプラクティスとして横展開したいプラットフォームチーム。
- モダナイゼーションを数か月がかりの大規模プロジェクトではなく、数日〜数週間で完了させたいエンタープライズ。
- AIに定型作業を任せつつも、変更のレビューやテスト検証には人の判断を残したい組織。
