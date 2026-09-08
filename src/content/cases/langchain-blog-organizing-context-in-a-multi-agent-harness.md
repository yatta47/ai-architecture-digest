---
type: guidance
title: マルチエージェントハーネスにおけるサブエージェントのコンテキスト設計
title_original: Organizing Context in a Multi-Agent Harness
company: LangChain
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- context-engineering
components:
- deepagents
- LangChain
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/organizing-context-in-a-multi-agent-harness
published_at: '2026-09-08'
---

## 概要

LangChainのdeepagentsに、サブエージェントがスーパーバイザーからどこまでコンテキストを引き継ぐかを指定する「context mode」（isolated/fork）を導入した。作業継続型のワーカーはフォークして調査済みコンテキストを再利用し、独立評価が必要なレビュアーはisolatedで新規コンテキストのみを与えるという使い分けを解説する。

## 設計のポイント

- フォーク型サブエージェントはプロンプトキャッシュを活かせるため、既に集めたコンテキストの再調査を避けコストと速度を改善する
- 作業を継続するワーカーはfork、既存の判断から独立して評価すべきレビュアーはisolatedというロール別の使い分けが基本方針
- 並列実行するリサーチャー等は各自の質問だけで完結するためisolatedとし、スーパーバイザー履歴の重複コピーを避ける

## 使いどころ

- 診断済みの原因を引き継いで修正実装とテストを行わせたいコーディングエージェント
- スーパーバイザーの診断に引きずられず独立してdiffをレビューさせたい場合
