---
type: announcement
title: Microsoft FoundryでのGPT-6 Astra提供開始
title_original: 'GPT-6 Astra: Frontier intelligence for work, now available in Microsoft Foundry'
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- human-in-the-loop
components:
- Microsoft Foundry
- GPT-6 Astra
- Microsoft Entra
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://azure.microsoft.com/en-us/blog/gpt-6-astra-frontier-intelligence-for-work-now-available-in-microsoft-foundry/
published_at: '2026-09-04'
---

## 概要

OpenAIの新フロンティアモデルGPT-6 AstraがMicrosoft Foundry上でLimited Access Programとして提供開始され、複数ステップの推論・計画立案とコンピュータ操作(computer use)によりアプリケーション横断でタスクを実行するエージェント的な機能を企業向けに提供する。Foundryは権限管理・監査ログ・ガードレールなどのエンタープライズ統制機能を組み合わせている。

## 設計のポイント

- コンピュータ操作(computer use)は画面上の情報が不完全・誤誘導的である前提に立ち、スコープ付き認証情報・人間の承認チェックポイント・操作ログで封じ込める
- Standard Global/US Data Zoneなど複数のデプロイ形態と従量課金モデルを用意し、予約キャパシティなしで段階的に導入できるようにする
- プロンプトと出力をモデル学習に使わない方針や暗号化・RBACなどFoundry側のガバナンス機能をモデル単体の安全性と組み合わせる

## 使いどころ

- ソフトウェア開発でのバグ再現・原因調査・修正提案からレビューまでの一連の作業を効率化したいチーム
- Power BIダッシュボードの作成・比較などビジネスインテリジェンス業務を高速化したい場合
- 専用APIがない業務アプリのフォーム処理やレコード更新などをエージェントに任せつつ承認・監視の仕組みを維持したい組織
