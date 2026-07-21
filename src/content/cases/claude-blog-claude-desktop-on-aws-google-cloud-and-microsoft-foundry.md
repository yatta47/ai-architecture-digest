---
type: announcement
title: Claude DesktopがAWS/Google Cloud/Microsoft Foundry上でChat・Cowork・Codeを統合提供、Hanwha Solutionsが自社LLM Gatewayで全世界展開
title_original: The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry
company: Hanwha Solutions
industry: cross-industry
cloud:
- aws
- gcp
- azure
patterns:
- llm-gateway
- unified-runtime
components:
- Claude Desktop
- Claude Cowork
- Claude Code
- Microsoft Entra ID
- IAM Identity Center
- Workforce Identity Federation
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry
published_at: '2026-06-22'
---

## 概要

AWS・Google Cloud・Microsoft Foundry経由でClaude Desktopを利用する組織向けに、これまでCoworkとCodeのみだった提供範囲をChatも含めた全機能へ拡張し、推論を自社クラウド環境内に留めたまま組織全体へSSO・MDMポリシーテンプレート・オフラインインストーラで展開できるようにした。Hanwha Solutionsは自社のLLM Gatewayを使い、追加のベンダー契約や大がかりなインフラ構築なしに世界中の数百人規模のユーザーへ迅速に展開したと語っている。

## 設計のポイント

- Chat・Claude Cowork・Claude Codeそれぞれに独立したポリシーキーを持たせ、非技術部門にはChat/Cowork、エンジニアリングにはCodeというように段階的に権限を広げられるようにする。
- IAM Identity Center・Workforce Identity Federation・Microsoft Entra IDなど既存のIdPにサインインを統合し、エンドユーザー端末にクラウド認証情報を配置しない設計にする。
- モデルガードによってGovCloudを含むすべての経路でルーティング先がClaudeであることを保証し、設定ミスがあってもルーティング先が意図せず変わらないようにする。

## 使いどころ

- 自社クラウド環境をすでに持ち、追加のベンダー契約なしにエンタープライズ全体へAIデスクトップアプリを展開したいIT部門。
- GCC High/DoD相当のレジデンシー要件があり、推論を自環境内に留める必要がある規制業界の組織。
- 非技術部門にはチャット、エンジニアリングにはコーディングエージェントというように、部門ごとに段階的にAI活用を広げたい企業。
