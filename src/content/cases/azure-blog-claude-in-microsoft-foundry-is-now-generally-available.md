---
type: announcement
title: Microsoft FoundryでのClaude一般提供によるエンタープライズAIエージェント基盤
title_original: Claude in Microsoft Foundry is now generally available
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- multi-model-routing
- llm-gateway
- guardrails
components:
- Claude
- Microsoft Foundry
- Foundry Agent Service
- Foundry Control Plane
- Microsoft Entra ID
- NVIDIA Blackwell Ultra
- Microsoft IQ
outcome:
  type: productivity
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/claude-in-microsoft-foundry-is-now-generally-available/
published_at: '2026-06-29'
---

## 概要

Anthropic のClaudeモデルがMicrosoft Foundry上で一般提供(GA)となり、企業は既存のAzureアカウントの認証・課金・ネットワーキング・ガバナンスの仕組みをそのまま使ってClaudeを利用できるようになった。Foundry Agent ServiceがClaudeを推論コアとして多段階のプランニングやツール呼び出しを統括し、Foundry Control Planeによる継続的な評価やゼロデータ保持オプションでエンタープライズ要件に対応する。Bolt、NVIDIA、Momentic、Everstarなどの企業がすでに本番システムでこの構成を利用していると紹介されている。

## 設計のポイント

- 既存のAzureアカウントの認証・課金・ネットワーキング・ガバナンスをそのまま使ってClaudeを利用できるようにし、インフラ調達の負担を減らす
- Foundry Agent ServiceがClaudeを推論コアとして多段階のプランニング・ツール呼び出し・タスク実行を統括する
- モデルルーターが問い合わせを最適なClaudeモデルへ自動振り分けし、コストを最大50%削減しつつ満足度を高める
- Foundry Control Planeが継続的に応答を評価し、ルール違反の出力をユーザーに届く前にブロックするガードレールを提供する

## 使いどころ

- 既存のAzureガバナンス・調達プロセスの中でフロンティアモデルを使いたいエンタープライズ
- データレジデンシー要件があり、ゼロデータ保持など高い機密性が求められるワークロード
- コーディング支援・業務プロセス自動化・リサーチアシスタントなど本番運用のエージェントアプリケーションを構築するチーム
