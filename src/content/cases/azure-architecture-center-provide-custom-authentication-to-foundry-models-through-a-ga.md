---
type: guidance
title: ゲートウェイ経由でAzure OpenAI/Foundry Modelsへの認証を一元化する4パターン
title_original: Provide custom authentication to Foundry Models through a gateway
industry: cross-industry
cloud:
- azure
patterns:
- llm-gateway
- defense-in-depth
components:
- Azure OpenAI
- Microsoft Foundry
- Azure API Management
- Microsoft Entra ID
- Azure Key Vault
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/azure-openai-gateway-custom-authentication
published_at: '2026-07-02'
---

## 概要

Azure OpenAI（Foundry Models）を外部IDプロバイダーや証明書、複数クライアント／複数インスタンスといった複雑な認証要件で利用する際に、Azure API Managementなどのゲートウェイを前段に置いて認証を一元化する設計パターン集。ゲートウェイがOAuthトークン検証やクライアント証明書検証を代行し、Azure OpenAIへの接続にはゲートウェイ自身のマネージドIDを使うことでキー管理の負荷とリスクを排除する。

## 設計のポイント

- ゲートウェイでOAuth/JWTを検証してから、ゲートウェイ自身のマネージドIDでAzure OpenAIに接続することで、クライアントにAPIキーを一切配布せずRBACを最小権限に保つ。
- クライアント証明書認証はゲートウェイ側に一元化し、ルートCAをAzure Key Vaultで管理することで、証明書失効・検証ロジックを各クライアントに実装させない。
- 単一アプリケーションのみがAzure OpenAIにアクセスするシンプルな構成では、ゲートウェイを挟まずアプリ自身にRBACを付与する方が運用コストが低い。

## 使いどころ

- Azureにホストされていない、または外部OIDCプロバイダー（Okta/Auth0等）で認証するクライアントアプリからAzure OpenAIへ安全にアクセスさせたい場合。
- 複数のクライアントアプリが同一のAzure OpenAIインスタンスを共有し、クライアントごとの個別キー管理を避けたい場合。
- マシン間通信やIoTデバイスなど、証明書ベースの認証がコンプライアンス上必須なシナリオ。
