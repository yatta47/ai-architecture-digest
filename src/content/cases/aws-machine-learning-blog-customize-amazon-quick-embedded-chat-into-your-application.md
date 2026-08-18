---
type: guidance
title: Amazon Quick埋め込みチャットをブランドに合わせてカスタマイズする方法
title_original: Customize Amazon Quick embedded chat into your application
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- context-engineering
components:
- Amazon Quick
- Amazon QuickSight Embedding SDK
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/customize-amazon-quick-embedded-chat-into-your-application/
published_at: '2026-08-18'
---

## 概要

Amazon Quickの埋め込みチャットをアプリケーションに統合する際、既定の見た目のままだと外部ツールが貼り付けられたような違和感が生じる。本記事はframeOptionsによるiframe制御とコンテナCSS、footerOptionsでの既定ブランディング除去、エージェントペルソナ設定によるトーン調整という2つのレイヤーでの一貫したカスタマイズ手法を、財務ダッシュボードの例で解説する。

## 設計のポイント

- iframe内部は直接スタイルできないため、frameOptionsのclassNameでiframe自体に、周囲のコンテナCSSでレイアウト全体にスタイルを分離して適用する
- footerOptions.showBrandAttributionとshowUsagePolicyをfalseにして既定のブランド表示を消し、ネイティブなUI部品に見せる
- SDKのcontentOptionsで組織専用のカスタムエージェントに固定し、コンソール側のペルソナ指示でトーン・言語スタイル・回答範囲を制御する
- withIframePlaceholderで読み込み中の白画面を防ぎ、framePermissionsでクリップボード操作など必要な権限のみ明示的に許可する

## 使いどころ

- 既存のWebアプリにAIチャットを埋め込みつつ、自社のデザインシステムやブランドガイドラインと統一感を持たせたい場合
- 業界・部門ごとに異なるトーン（例: 金融アナリスト向けの専門的な受け答え）で応答させたいチャットボットの構築
- 汎用的な回答ではなく、自社ドメインの文脈を踏まえた応答を返すエンベデッドAIアシスタントが必要な場面
