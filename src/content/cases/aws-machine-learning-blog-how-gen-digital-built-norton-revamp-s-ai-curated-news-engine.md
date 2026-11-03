---
type: case
title: Norton RevampのニュースエンジンをAgentCore Web Searchで最新情報に接地
title_original: How Gen Digital built Norton Revamp's AI-curated News Engine with Amazon Bedrock AgentCore Web Search
company: Gen Digital
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- rag
- context-engineering
components:
- Amazon Bedrock AgentCore Web Search
- AgentCore Gateway
- MCP
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-gen-digital-built-norton-revamps-ai-curated-news-engine-with-amazon-bedrock-agentcore-web-search/
published_at: '2026-11-03'
---

## 概要

Gen DigitalはNorton Revampで、マネージドなAgentCore Web Searchを用い、コンテンツ提案やニュースフィードを引用付きの最新Web情報に接地した。自前クローラや外部ニュースAPIを比較した上で、運用負荷とデータ流出リスクを避ける構成を選んだ。

## 設計のポイント

- 自前クローラ・外部API・静的KBを比較し、フルマネージドでAWS内に閉じる検索を採用
- MCP準拠のマネージドコネクタとしてGatewayに接続し、出典URLと公開日を返させて接地する
- 少人数でも個別化されたリアルタイムフィードを回せる

## 使いどころ

- 最新情報が価値になるコンテンツ生成・ニュース推薦
- 外部APIのベンダー管理やデータ外部送信を避けたいチーム
