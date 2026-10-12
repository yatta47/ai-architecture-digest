---
type: case
title: Arize PhoenixとHarborでエージェントのツール説明文を検証する
title_original: How to test agent tool descriptions with Harbor and Phoenix
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- ai-agent
components:
- Arize Phoenix
- Harbor
- MCP
- PXI
- Codex
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-to-test-agent-tool-descriptions-with-harbor-and-phoenix/
published_at: '2026-10-12'
---

## 概要

HarborでタスクをプロンプトとDockerfile環境・検証器・正解のフォルダとして定義し、Phoenixでツール呼び出しのトレースを確認して、ツール説明文の変更を検証する手順。説明文を1つ変えただけでCodexの不要なスキル読み込みが51回から0回になり、ベンチのコストが11.85ドルから8.34ドルに下がった。正答率は変わらなかった。

## 設計のポイント

- 検証器は経路ではなく結果だけを確認し、同じタスク群をPXIにもMCP/CLI経由のコーディングエージェントにも使い回す。
- スコアが全て合格でも、ツール数とコストをトレースで見ることで無駄な作業を見つける。
- LLM審査員にも採点メモが必要で、審査員自体をベンチマークの一部として検証する。

## 使いどころ

- MCPやツール説明文を改善しているエージェント開発者。
- 変更前後を同一ベンチで比較する回帰評価を整えたいチーム。
