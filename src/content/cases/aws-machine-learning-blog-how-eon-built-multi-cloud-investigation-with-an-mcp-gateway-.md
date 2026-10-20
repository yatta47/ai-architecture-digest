---
type: case
title: EonがMCPゲートウェイでマルチクラウド障害調査ツールを一本化
title_original: How Eon built multi-cloud investigation with an MCP Gateway on Amazon Bedrock AgentCore
company: Eon
industry: cross-industry
cloud:
- aws
- gcp
- azure
- multi-cloud
patterns:
- ai-agent
- root-cause-analysis
- unified-runtime
components:
- Amazon Bedrock AgentCore
- AgentCore Gateway
- MCP
- Grafana
- GitHub
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-eon-built-multi-cloud-investigation-with-an-mcp-gateway-on-amazon-bedrock-agentcore/
published_at: '2026-10-20'
---

## 概要

EonはツールごとのクレデンシャルとローカルMCPプロセスをやめ、認証付きの単一MCPゲートウェイに集約した。AWS・GCP・Azureをまたぐ調査ツールに開発者と自律エージェントが同じ入口で到達でき、新人の環境構築は2日から約2分になった。

## 設計のポイント

- ツールごとの認証設定・ローテーションをゲートウェイに集約し、統合の増加に伴う管理負荷を抑える。
- 開発者のローカルMCPプロセスを廃止し、人とエージェントが同一の入口と権限モデルを共有する。
- ログ・メトリクス・PRなど異種ツールを一つのセッションで横断し、インシデント調査を一箇所で完結させる。

## 使いどころ

- 複数クラウドと多数の運用ツールを持つSaaS事業者の障害調査。
- 新規エンジニアのオンボーディング時間を短縮したいプラットフォームチーム。
