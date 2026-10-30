---
type: guidance
title: GovCloud上のBedrock経由でChatGPTデスクトップアプリ(Codex)を閉域運用する構成
title_original: Configure the ChatGPT desktop app with Amazon Bedrock in AWS GovCloud (US)
company: OpenAI
industry: public-sector
cloud:
- aws
patterns:
- ai-agent
- guardrails
- policy-as-code
- defense-in-depth
components:
- Amazon Bedrock
- Amazon Bedrock Mantle
- AWS IAM
- AWS IAM Identity Center
- ChatGPT desktop app
- Codex
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/configure-the-chatgpt-desktop-app-with-amazon-bedrock-in-aws-govcloud-us/
published_at: '2026-10-30'
---

## 概要

ChatGPTデスクトップアプリ(Codex)のモデル推論をAWS GovCloud (US-West)のAmazon Bedrock Mantleへ向けるための設定手順を解説した記事。APIモード認証、管理者制御のrequirements.toml、名前付きプロファイル、ネットワーク制限を組み合わせ、承認済みエンドポイント以外への通信を遮断する。

## 設計のポイント

- 管理者が制御するrequirements.tomlでサンドボックスモードや承認ポリシー、Web検索モードをユーザーが上書きできない形で制限する。
- 認証はBedrock APIキーまたはAWS SDK認証チェーン(SSO含む)とし、シークレットをTOMLに置かず、認証情報キャッシュをエージェントの書き込みから保護する。
- 通信先を承認済みBedrockエンドポイントのみに絞り、ブラウザ・コンピュータ操作など外部接続を伴う機能を無効化する。

## 使いどころ

- 政府機関などGovCloudのIAM・リージョン統制下でコーディングエージェントを使いたい組織。
- 導入前にセキュリティチームが検証・文書化できる閉じた構成を作りたい場面。
