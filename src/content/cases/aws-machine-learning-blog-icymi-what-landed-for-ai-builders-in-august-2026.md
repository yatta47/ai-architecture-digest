---
type: announcement
title: 2026年8月のAmazon Bedrock/AgentCore/Strandsアップデートまとめ
title_original: 'ICYMI: What landed for AI builders in August 2026'
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llmops
- context-engineering
- multi-model-routing
components:
- Amazon Bedrock
- Amazon Bedrock AgentCore
- Strands Agent Harness SDK
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/icymi-what-landed-for-ai-builders-in-august-2026/
published_at: '2026-09-09'
---

## 概要

AWSは2026年8月のAmazon Bedrock・AgentCore・Strandsの主要アップデートをまとめて紹介する。GPT-5.6系モデルの百万トークンコンテキスト対応とWeb検索統合、25以上のリージョンをまたぐクロスリージョン推論、Strands Agent Harness SDKのOSS公開などが中心で、モデル単体からエージェントを取り巻くシステム全体への焦点の移行を示す。

## 設計のポイント

- モデルの能力向上だけでなく、コンテキストアクセス・アクション権限・データ処理場所・コスト統治までを含めた『モデルを取り巻くシステム』を強化する
- グローバルプロファイルと地理限定プロファイルを使い分け、スループットとデータ所在地要件を両立する
- Strandsをオープンソース化し、任意のフレームワーク・モデルでエージェントを構築・デプロイできるようにする

## 使いどころ

- 規制業界や物理システムと連携する長時間稼働のエージェントアプリケーションを構築するチーム
- 最新のBedrock/AgentCore機能を追跡し、月次で導入判断をしたいプラットフォームチーム
