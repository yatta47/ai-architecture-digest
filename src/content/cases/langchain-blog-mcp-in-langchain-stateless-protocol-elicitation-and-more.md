---
type: announcement
title: LangChainのMCPサポートがステートレス新仕様・elicitation・キャッシュに対応
title_original: 'MCP in LangChain: Stateless Protocol, Elicitation, and More!'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- ai-agent
- context-engineering
components:
- LangChain
- Model Context Protocol
- FastMCP
- LangGraph
- MCPAdapter
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/mcp-in-langchain-stateless-protocol-elicitation-and-more
published_at: '2026-09-03'
---

## 概要

LangChainがMCP（Model Context Protocol）サポートをlangchain.mcpとして本体パッケージに統合し、新しいステートレス仕様に対応したことを発表。セッションピン留めが不要になったことでツールリストのキャッシュや、LangGraphのinterruptを使ったelicitation（人間による確認）を実現している。

## 設計のポイント

- 新MCP仕様のステートレス化により、サーバーの再デプロイがセッションを破壊しなくなりスケーラブルな運用が可能になる
- サーバーが提示するTTLに基づきツールリストをクライアント側でキャッシュし、実行のたびの再取得コストを削減する
- elicitation（ツールが呼び出し元に確認を求める処理）をLangGraphのinterruptプリミティブで表現し、チェックポインタで一時停止・再開できるようにする
- ClientGroupで新旧2つのプロトコル世代のMCPサーバーを混在管理し、サーバーごとに認証方式を分離する

## 使いどころ

- 外部ツールをMCP経由でエージェントに接続する際のスケーラブルな接続管理
- 削除など破壊的操作の前に人間承認を挟みたいエージェントワークフロー
- 新旧混在するMCPサーバー群を段階的に移行しながら運用したいチーム
