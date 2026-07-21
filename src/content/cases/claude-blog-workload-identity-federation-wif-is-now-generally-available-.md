---
type: announcement
title: Claude PlatformのWorkload Identity Federationで静的APIキーを廃止
title_original: Secure access to the Claude Platform with Workload Identity Federation
industry: cross-industry
cloud:
- multi-cloud
patterns:
- defense-in-depth
components:
- Claude Platform
- Claude Console
- Admin API
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/workload-identity-federation
published_at: '2026-06-17'
---

## 概要

Claude PlatformにWorkload Identity Federation(WIF)がGAとなり、AWS IAMやGCP/Kubernetesサービスアカウント、Azureマネージドアイデンティティ、GitHub Actions等のOIDC準拠IDで、静的APIキーなしに短命トークンで認証できるようになった。ワークロードごとにservice accountを発行し、ロールと監査ログを個別に持たせる。

## 設計のポイント

- 静的APIキーの代わりにOIDC発行の短命トークンを使い、漏洩やローテーション漏れのリスクを構造的に除去する
- ワークロードごとにservice accountを分離し、ロールと監査ログを個別に持たせる
- APIキーとWIFを並行運用できるようにし、ワークロード単位で段階的に移行する

## 使いどころ

- 複数チーム・ワークロードでAPIキーを共有運用しており、監査証跡や最小権限が求められる組織
- GitHub Actions等のCI/CDからAIプラットフォームへ安全にアクセスしたいケース
