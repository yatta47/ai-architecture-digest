---
type: announcement
title: ClaudeをAzure環境でネイティブ運用できるMicrosoft Foundry連携が一般提供開始
title_original: Claude in Microsoft Foundry is now generally available
industry: cross-industry
cloud:
- azure
patterns:
- llmops
- llm-gateway
- inference-optimization
components:
- Microsoft Foundry
- Azure
- Claude Opus 4.8
- Claude Haiku 4.5
- Messages API
- NVIDIA GB300 GPU
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-in-microsoft-foundry
published_at: '2026-06-29'
---

## 概要

AnthropicはClaudeモデルをMicrosoft Foundry経由でAzure上から利用できるようにし、一般提供を開始した。既存のAzure認証・課金・ガバナンス機構をそのまま使え、データ所在地要件に対応する米国データゾーンも選択可能である。まずClaude Opus 4.8とClaude Haiku 4.5がMessages APIで提供され、プロンプトキャッシュや拡張思考などの機能も利用できる。

## 設計のポイント

- Azureの既存の認証・課金・ガバナンス機構にそのまま統合することで、エンタープライズの導入障壁を下げる
- 推論処理を行うリージョンを選択可能にし、米国データゾーンでデータ所在地要件に対応する
- Anthropicが推論基盤を運用しデータ処理者としての責任を担いつつ、Azureホスト版とAnthropicホスト版の二本立てで提供する
- Microsoft Enterprise Agreementの既存コミットメントで支払いを消化できるようにし、請求を一本化する

## 使いどころ

- 既存のAzure ID・ネットワーク・ガバナンス基盤をそのまま使ってClaudeを迅速に導入したいエンタープライズ
- データ所在地要件がある金融・公共分野などの規制業種でのAI活用
- コーディングやエージェント処理、複雑な推論などスループットが求められるワークロードをAzure上で運用したいチーム
- Microsoft Enterprise Agreementの調達枠を活用してAI投資を最適化したい企業
