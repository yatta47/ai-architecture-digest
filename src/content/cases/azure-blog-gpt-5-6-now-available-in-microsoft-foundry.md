---
type: announcement
title: GPT-5.6ファミリーとホスト型エージェントランタイムのMicrosoft Foundry一般提供開始
title_original: GPT-5.6 now available in Microsoft Foundry
industry: cross-industry
cloud:
- azure
patterns:
- multi-model-routing
- unified-runtime
- ai-agent
- llmops
components:
- GPT-5.6 Sol
- GPT-5.6 Terra
- GPT-5.6 Luna
- Microsoft Foundry
- Foundry Agent Service
- Foundry Toolkit for VS Code
- Microsoft Agent Framework
- GitHub Copilot SDK
- Claude Agent SDK
- Azure Virtual Network
- Microsoft 365 Copilot
- Microsoft Teams
outcome:
  type: productivity
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/gpt-5-6-now-available-in-microsoft-foundry/
published_at: '2026-07-09'
---

## 概要

Microsoft FoundryでOpenAIのGPT-5.6シリーズ（Sol/Terra/Luna）が一般提供となり、用途別のコスト・性能特性に応じてモデルを選べるようになった。あわせてAPACデータゾーンとFoundry Agent Serviceのホスト型エージェント（VNet統合などエンタープライズ機能付き）も一般提供され、複数フレームワークで構築したエージェントを単一の本番ランタイムで運用しMicrosoft 365やTeamsへ配信できる。これにより企業は実験段階から本番運用まで、ばらばらなツールを組み合わせずに一つのプラットフォーム上で進められるとしている。

## 設計のポイント

- 用途ごとに推論力・速度・コストが異なる複数モデル（Sol/Terra/Luna）を用意し、ワークロードに応じて使い分けられるようにする
- グローバル/データゾーン/リージョンの複数デプロイ形態を用意し、コンプライアンスやデータ主権要件に応じて配置を選べるようにする
- エージェントの実行フレームワークを問わず単一のホスト型ランタイム（Foundry Agent Service）に集約し、VNet統合などの分離を標準で提供する
- モデル選択・エージェント実行基盤・配信チャネル（Microsoft 365/Teams）を単一プラットフォームに統合し、実験から本番移行のギャップを埋める

## 使いどころ

- 複数のOpenAIモデルをコストと性能で使い分けたい企業のエージェント開発チーム
- APACなど地域内でのデータ処理を求められる規制業種（金融機関など）
- GitHub Copilot SDKやLangGraphなど異なるフレームワークで作ったエージェントを単一基盤で本番運用したいチーム
- 社内エージェントをMicrosoft 365 CopilotやTeams経由でエンドユーザーに配信したい組織
