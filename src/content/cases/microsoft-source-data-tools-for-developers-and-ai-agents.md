---
type: announcement
title: Cosmos DB拡張機能がCopilotエージェントにスキーマ把握・クエリ実行ツールを提供
title_original: 'Azure Cosmos DB in the agentic era: data tools for developers and AI agents'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- human-in-the-loop
- llm-gateway
components:
- Azure Cosmos DB
- GitHub Copilot
- Azure Cosmos DB Shell
- MCP
- Azure Cosmos DB Emulator
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-in-the-agentic-era-data-tools-for-developers-and-ai-agents/
published_at: '2026-08-19'
---

## 概要

Azure Cosmos DB拡張機能（VS Code）に、GitHub Copilotがクエリエディタのコンテキストを把握し、コンテナのスキーマをサンプリングしてから正確なクエリを生成・実行できるツール群と、Cosmos DB固有のノウハウを与えるエージェントスキルを追加した。スキーマサンプリングやクエリ実行の前には必ず開発者の同意を求め、データアクセスとRU消費の主導権を人間側に残す設計になっている。

## 設計のポイント

- プロパティ名を推測させず、実データのコンテナスキーマを事前サンプリングしてからクエリを生成させることで幻覚を防ぐ
- 「ツール（実行手段）」と「スキル（ドメイン知識）」を分離し、汎用モデルにCosmos DB特有のクエリ最適化ノウハウを外挿する
- スキーマ読み取りやクエリ実行など課金・データアクセスを伴う操作は都度明示的な同意を要求し、機械的な作業と人間判断の境界を明確にする

## 使いどころ

- データベースの実装詳細を都度説明せずにコーディングエージェントへ問い合わせたい開発者
- Cosmos DBのクエリコスト（RU）やパーティション設計を意識した安全なエージェント運用を設計したいチーム
- 既存の権限体系（Entra ID・マネージドID等）を保ったままAIエージェントにDBアクセスを許可したい組織
