---
type: case
title: Claude Managed Agentsで自らプロトタイピングするプロダクトマネージャーの開発フロー
title_original: Product development in the agentic era
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- parallel-execution
- memory-consolidation
- multi-agent-orchestration
components:
- Claude Code
- Claude Managed Agents
- Claude Cowork
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/product-development-in-the-agentic-era
published_at: '2026-04-29'
---

## 概要

Claude Managed Agentsのプロダクトマネージャーが、Claude Codeで事前公開版の自社API仕様に対して実際にエージェントを組んで即日プロトタイピングし、そこで見つかった課題を製品設計へフィードバックする開発フローを紹介する。オープンエンドな調査にはClaude/Claude Coworkを、明確化したタスクの自動化にはManaged Agents上に構築するカスタムエージェント(採用状況分析、開発者センチメント監視、デモ作成など)を使い分けている。

## 設計のポイント

- ドキュメントでの仕様策定にとどめず、事前公開版のAPI仕様に対して実際にエージェントを組んで動かし、見つかった課題を製品設計にフィードバックする
- 調査対象が大量にある場合は複数のエージェントに並列でリサーチをファンアウトさせ、結果を待って統合する
- 過去の実行結果を記憶させたエージェントに継続的な分析を積み上げさせ、クラウド上で実行して結果だけ確認する運用に切り替える

## 使いどころ

- 自社プロダクトを自らのエージェントで検証しながら設計をブラッシュアップしたいプロダクトマネージャー
- 定型化できるが個別対応が必要な業務(デモ作成、モニタリング等)を自動化したいチーム
