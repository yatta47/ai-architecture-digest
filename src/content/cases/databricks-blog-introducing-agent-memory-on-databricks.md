---
type: announcement
title: Databricks Agent Memoryがベータ提供開始
title_original: Introducing Agent Memory on Databricks
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- context-engineering
- memory-consolidation
- ai-agent
components:
- Agent Bricks
- Lakebase
- Unity Gateway
- MCP
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/introducing-agent-memory-databricks
published_at: '2026-10-20'
---

## 概要

Agent Bricks上のAgent Memoryがベータ提供された。MemCurrentアーキテクチャに基づき、自動ログ/ロードのプラグイン、オンデマンドのツール、バックグラウンド統合のドリーミングの3経路をLakebaseで低遅延に提供する。

## 設計のポイント

- メモリアクセスを、プラグイン・ツール・オフライン統合の3経路に分けて役割を明確にする。
- メモリ保存にLakebaseを使い、信頼性と低遅延を確保する。
- ステートレスなエージェントが同じ文脈を毎回再導出するコストを避ける。

## 使いどころ

- 日常的に使うエージェントで、修正内容や嗜好を引き継ぎたいチーム。
- メモリ自作に伴う保存先・合成・取得の設計を省きたい開発者。
