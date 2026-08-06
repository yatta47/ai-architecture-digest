---
type: case
title: クラウド上のエージェントがユーザーのローカルExcelを直接操作するMCPブリッジ
title_original: How we built an MCP bridge to give our AgentCore-hosted AI agent access to local MCP tools
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- mcp-tool-bridging
components:
- Amazon Bedrock AgentCore
- Model Context Protocol
- Strands Agents
- WebSocket
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-we-built-an-mcp-bridge-to-give-our-agentcore-hosted-ai-agent-access-to-local-mcp-tools/
published_at: '2026-08-05'
---

## 概要

AWS社内では、年間4万1000件超の会話実績を持つ財務向けAIアシスタントで、クラウド上のAgentCoreホスト型エージェントからユーザーのローカルPC上のファイルをMCP経由で直接操作する仕組みを運用している。本記事はその簡略版として、WebSocketとブラウザのネイティブメッセージングでリモートMCPクライアントとローカルMCPサーバーを橋渡しするMCPブリッジの構成を再現している。

## 設計のポイント

- リモートMCPクライアント（クラウド上のエージェント）とローカルMCPサーバー（ユーザーPC上のツール）の間を、ブラウザ拡張機能を中継役にしたWebSocket＋ネイティブメッセージングでトンネリングする
- 各ホップでJSON envelopeを1層ずつ剥がしていく設計にし、AgentCoreランタイム・拡張機能・ブリッジ・MCPサーバーの責務を明確に分離する
- 認証情報はユーザーのローカルAWS認証情報からSigV4署名付きの一時WebSocket URLを生成する形にとどめ、ブラウザや通信経路に長期認証情報を持たせない
- リクエストIDとasyncio.Futureで応答を相関させることで、複数のツール呼び出しを同時並行で待ち合わせられるようにする

## 使いどころ

- Excelやローカルファイルを主戦場にする財務・分析担当者が、中央集約型のAIエージェントからそれらのファイルを直接扱いたい場合として
- MCPサーバーがユーザー端末側にしか存在せず、エージェント本体はクラウドで一元管理したいアーキテクチャとして
- 自前のモデル・ツールサーバーで『クラウドエージェント×ローカルツール』体験を自己ホストしたい場合として
