---
type: guidance
title: Claude Codeが自らマルチエージェントの実行基盤（ハーネス）を書いて実行する「Dynamic Workflows」
title_original: 'A harness for every task: dynamic workflows in Claude Code'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- parallel-execution
- ai-agent
components:
- Claude Code
- Claude Opus 4.8
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
published_at: '2026-06-02'
---

## 概要

Claude Codeが、タスクごとにJavaScriptで書かれたカスタムのマルチエージェント実行基盤（ワークフロー）をその場で生成・実行できる新機能を解説。単一コンテキストで作業を続けるときに起きがちな「Agentic laziness」「Self-preferential bias」「Goal drift」といった失敗モードを、独立したサブエージェントへの分割によって緩和する。

## 設計のポイント

- Classify-and-act（分類して振り分け）、Fan-out-and-synthesize（分割並列実行して統合）、Adversarial verification（敵対的検証）、Generate-and-filter、Tournament、Loop until doneという再利用可能なパターンを組み合わせて構成する
- サブエージェントごとに使用モデルの強さやワークツリー分離の要否を動的に選べる
- タスクごとに専用ハーネスをその場で書くため、あらゆるケースに対応しなければならない静的ワークフローより最適化しやすい
- 中断されてもセッション再開時に途中から処理を継続できる

## 使いどころ

- 再現困難なバグ調査など、終了条件が事前に分からない探索的タスクを網羅的にやり切りたい場合
- 大量の候補（インシデント履歴・レジュメ・アイデア案など）を並列に評価・審査し、上位を絞り込みたい場合
