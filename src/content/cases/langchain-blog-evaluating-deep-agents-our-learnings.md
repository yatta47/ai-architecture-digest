---
type: case
title: Deep Agentsハーネス上の4つのアプリを評価して見えたテストパターン
title_original: 'Evaluating Deep Agents: Our Learnings'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
- memory-consolidation
components:
- LangSmith
- Deep Agents
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/evaluating-deep-agents-our-learnings
published_at: '2026-06-15'
---

## 概要

LangChainはDeep Agentsハーネス上でCLIコーディングエージェント・LangSmithアシスタント・パーソナルメールアシスタント・ノーコードのAgent Builderという4種類のアプリを出荷する中で、それぞれに応じた評価パターンを整理した。各データポイントごとに専用のテストロジックが必要になること、単一ステップ評価・フルターン評価・複数ターン評価をどう使い分けるかをまとめている。

## 設計のポイント

- 全データポイントを同一の評価器でスコアするのではなく、各テストケースごとに軌跡(trajectory)や状態への個別アサーションを書く
- エージェントを1ステップだけ実行して直後の意思決定を検証する単一ステップ評価は、トークンを節約しつつ特定シナリオの判断ミスを素早く検出できる
- フルターン評価でエージェントの最終状態やトラジェクトリ全体の妥当性を、複数ターン評価で現実的な複数回のやり取りを検証する
- 再現可能でクリーンなテスト環境を用意し、LangSmithのPytest/Vitest統合でトレースと結果を実験として自動記録する

## 使いどころ

- 長期的なタスクやファイルシステムへの記憶更新を伴うDeep Agentsを評価したいチーム
- エージェントの最終応答だけでなく、途中の意思決定やツール呼び出しまでテストしたいチーム
