---
type: announcement
title: 2026年9月のBedrock/AgentCore/Strands更新まとめ
title_original: 'ICYMI: What landed for AI builders in September 2026'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-model-routing
- rag
components:
- Amazon Bedrock
- Amazon Bedrock AgentCore
- Strands
- Amazon Bedrock Managed Knowledge Base
- AWS IAM
- AWS CloudTrail
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/icymi-what-landed-for-ai-builders-in-september-2026/
published_at: '2026-10-09'
---

## 概要

2026年9月のAmazon Bedrock、AgentCore、Strandsの更新をまとめた記事。OpenAI/Claude/Kimi/Grokなどモデル選択肢の拡大、AgentCoreランタイムの低コールドスタート化、Strandsの軽量ハーネス、ナレッジベースの自動同期とコネクタ追加が主な内容。

## 設計のポイント

- モデル・ランタイム・ツールの各層で選択肢を持たせ、用途ごとにモデルを使い分ける前提で設計している。
- エージェントの実行基盤はサーバーレスでアイドル時ゼロスケール、ハードウェア分離セッションとし、使用量課金にする。
- 小型の判断専用モデル(Strands Decider 2B)でツール選択やルーティングをローカルに低遅延で行う。
- ナレッジベースは定期同期とネイティブコネクタで、独自の取り込みパイプラインを持たずに鮮度を保つ。

## 使いどころ

- Bedrock上でエンタープライズのIAM/CloudTrail統制を維持したままエージェントを構築したいチーム。
- コスト・遅延・精度のバランスでモデルを選び分けたい基盤担当者。
- 社内文書(SharePoint/Confluence等)をRAGに取り込み続けたい情シス。
