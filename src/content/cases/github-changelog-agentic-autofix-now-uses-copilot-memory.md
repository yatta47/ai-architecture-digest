---
type: announcement
title: エージェント型オートフィックスがCopilot Memoryを活用
title_original: Agentic autofix now uses Copilot Memory
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- memory-consolidation
components:
- GitHub Copilot
- Copilot Memory
- agentic autofix
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-25-agentic-autofix-now-uses-copilot-memory
published_at: '2026-09-25'
---

## 概要

エージェント型オートフィックスが、Copilot Memoryを有効にした顧客で既存メモリを参照してセキュリティアラートを修正し、修正パターンをメモリとして保存するようになった。蓄積された知見はコードレビューやクラウドエージェントにも共有される。両機能ともパブリックプレビューである。

## 設計のポイント

- 修正パターンを永続メモリに保存し、次回以降の修正に再利用する。
- 機能をまたいでメモリを共有し、リポジトリ固有の安全な開発パターンを伝播させる。

## 使いどころ

- セキュリティアラートの修正を繰り返し行う開発チーム。
- リポジトリ固有の知識をAI機能間で共有したい組織。
