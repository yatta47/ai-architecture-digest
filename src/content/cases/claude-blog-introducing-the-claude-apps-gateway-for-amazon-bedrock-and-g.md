---
type: announcement
title: Claude Code利用を一元管理するセルフホスト型ゲートウェイ
title_original: Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud
company: Anthropic
industry: cross-industry
cloud:
- aws
- gcp
- on-prem
patterns:
- llm-gateway
- multi-model-routing
- policy-as-code
- cost-optimization
components:
- Claude Code
- Amazon Bedrock
- Google Cloud
- Claude API
- PostgreSQL
- Google Workspace
- Microsoft Entra ID
- Okta
- OTLP
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/introducing-the-claude-apps-gateway
published_at: '2026-06-29'
---

## 概要

AnthropicはAmazon BedrockとGoogle Cloud向けに、Claude Codeの利用を一元管理するセルフホスト型ゲートウェイを発表した。単一のステートレスコンテナとPostgreSQLで構成され、SSO認証・ポリシー適用・利用状況の可視化・コスト上限の設定を企業側のインフラ内で完結できる。開発者は既存のclaudeバイナリからそのままゲートウェイに接続でき、Claude API・Bedrock・Google Cloudへのルーティングとフェイルオーバーも設定可能。

## 設計のポイント

- ゲートウェイをステートレスな単一コンテナとして提供し、状態はPostgreSQLに集約することでデプロイと水平運用を簡素化している。
- 認証は社内IdPとのOIDC連携に委ね、短命セッションのみを発行して開発者端末に長期シークレットを置かない設計にしている。
- ポリシーはサーバー側で一元定義し、クライアントはサインイン時に取得してリクエストごとに強制適用する。
- 推論先はClaude API・Amazon Bedrock・Google Cloudから選択でき、プロバイダ間フェイルオーバーを構成できるルーティング層を分離している。

## 使いどころ

- 多数の開発者にClaude Codeを配布する企業のプラットフォーム/IT部門が、資格情報配布やオンボーディング・オフボーディングを簡略化したい場合。
- 組織・グループ・ユーザー単位で利用料の上限設定と可視化が必要なコスト管理担当者。
- セキュリティ・コンプライアンス部門が、端末への長期シークレット配置を避けつつ利用ポリシーを一元的に強制したい場合。
- AWSとGCPを併用するマルチクラウド組織で、推論経路の一貫した制御とプロバイダ間フェイルオーバーを求める場合。
