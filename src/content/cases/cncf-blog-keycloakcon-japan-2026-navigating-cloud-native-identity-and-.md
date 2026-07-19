---
type: announcement
title: KeycloakCon Japan 2026、AIエージェント時代のID管理がテーマに
title_original: 'KeycloakCon Japan 2026: Navigating Cloud Native Identity and the AI Frontier'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llm-gateway
- guardrails
components:
- Keycloak
- Model Context Protocol
- SPIRE
- Sigstore
- Istio
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/14/keycloakcon-japan-2026-navigating-cloud-native-identity-and-the-ai-frontier/
published_at: '2026-07-14'
---

## 概要

横浜開催のKubeCon+CloudNativeCon Japan 2026に併設されるKeycloakConの案内記事。AIエージェントがMCP経由で他システムを操作する際の「Confused Deputy」問題、ID連鎖(ID-JAG)、Kubernetes上でのキーレスなAIエージェントID(SPIRE/DPoP)など、AI時代のアイデンティティガバナンスが中心テーマとなる。

## 設計のポイント

- OAuth 2.0のトークン委任・トークン交換・fine-grainedスコープ制御で、MCPサーバー横断の権限委譲を既存のKeycloak機能だけで実現する。
- SPIRE(JWT-SVID)とDPoPを組み合わせ、静的な資格情報ファイルもKeycloakクライアントの手動作成も不要なキーレスなエージェントIDを実現する。
- KeycloakをSigstoreのOIDCプロバイダとして組み込み、ビルド署名を検証済みIDに暗号学的に紐付ける。

## 使いどころ

- 自律型AIエージェントにMCP経由で権限委譲する仕組みを設計したいプラットフォームチーム。
- 大規模組織でKeycloakベースのアイデンティティ基盤を運用しAIエージェント対応を検討する担当者。
