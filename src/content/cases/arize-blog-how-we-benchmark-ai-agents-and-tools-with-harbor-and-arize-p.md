---
type: case
title: Harborの再現可能サンドボックスでAIエージェントとMCPを評価するArizeの方法
title_original: How we benchmark AI agents and tools with Harbor and Arize Phoenix
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
- llmops
components:
- Harbor
- Arize Phoenix
- Docker
- MCP
- Claude Code
- Codex
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/ai-agent-benchmarking-harbor-arize-phoenix/
published_at: '2026-10-05'
---

## 概要

Arizeは、モックだらけで本番と乖離した単発のエージェント評価をやめ、Harborで実アプリとデータを入れたサンドボックスを試行ごとに作り直す方式へ移行した。検証器で成功を判定し、結果をPhoenixの実験とトレースに記録する。

## 設計のポイント

- 試行ごとに新しいサンドボックスを使い、状態をリセットして再現性を確保する。
- 本番に近い実エージェントエンドポイントと事前投入データで、ツール結果の扱いまで検証する。
- 同じタスクと検証器を、自社エージェント、MCPサーバー、CLIで使い回す。
- ターン数やツール呼び出し数もトレースで測り、正確さと効率を両方見る。

## 使いどころ

- 自社エージェントを本番前にオフラインで回帰評価したいチーム。
- MCPサーバーやスキル、CLIを提供し、エージェントが使いこなせるか確認したい開発者。
