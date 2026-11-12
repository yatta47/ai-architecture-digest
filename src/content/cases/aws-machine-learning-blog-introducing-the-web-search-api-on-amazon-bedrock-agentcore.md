---
type: announcement
title: AgentCoreのWeb Search API：1回のAPI呼び出しでWeb検索結果を取得
title_original: Introducing the Web Search API on Amazon Bedrock AgentCore
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- rag
components:
- Amazon Bedrock AgentCore
- AWS SDK
- IAM
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-the-web-search-api-on-amazon-bedrock-agentcore/
published_at: '2026-11-11'
---

## 概要

AgentCoreにWeb Search APIが追加され、ゲートウェイやMCPなしで自分のコードから単一API呼び出しでWeb検索できる。Amazon運営のインデックスから、抜粋・タイトル・URL・公開時刻を含む順位付き結果が返り、IAM認証で利用する。

## 設計のポイント

- ゲートウェイ経由の構成を省き、直接SDK/CLIから検索を呼べる。
- IAM署名で既存の認証・認可に乗せる。
- 複数エージェントで検索ポリシーを共有するならゲートウェイ版を使い分ける。

## 使いどころ

- 最新情報が必要な回答アプリ。
- 検索結果だけをコードで使いたい開発者。
- IAM統制下でWeb検索を使いたい企業。
