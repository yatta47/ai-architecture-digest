---
type: case
title: 実PRレビュー履歴からコードレビューエージェントを評価するReviewBench
title_original: Evaluating code review agents with ReviewBench
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
- llmops
components:
- LangSmith
- Harbor
- Deep Agents
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/evaluating-code-review-agents-with-reviewbench
published_at: '2026-07-31'
---

## 概要

LangChainは社内LangSmithリポジトリの実PRレビューコメントを基に、コードレビューエージェントを評価するベンチマーク「ReviewBench」を構築。LLM-as-judgeによるカバレッジ/精度採点で、レビュー戦略を明示的にプロンプトすることでスコアが大きく改善することを確認した。

## 設計のポイント

- 生のレビューコメントをそのまま正解ラベルにせず、LLMによる一次フィルタと人手レビューで検証可能な具体的指摘のみに絞り込む
- タスクをHarbor形式で標準化し、凍結したPRコンテキストとローカルGitHubスタブで再現可能な評価環境を用意する
- 採点はカバレッジ(既知の問題を発見できたか)と精度(指摘内容が正しいか)をF1で均等に重み付けする
- モデル比較だけでなくハーネス(プロンプト戦略)の比較も行い、レビュー戦略の違いが性能に与える影響を分離して検証する

## 使いどころ

- 社内のコーディング規約や暗黙の契約を踏まえたコードレビューエージェントの精度を測定したいチーム
- LLM-as-judgeによる自動評価パイプラインを自社のPR履歴から構築したい開発者
- モデル選定だけでなくプロンプト/ハーネス設計の改善余地を検証したいエージェント開発者
