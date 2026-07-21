---
type: guidance
title: コーディングエージェント向け『スキル』の効果を計測するテストパイプライン
title_original: Evaluating Skills
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- context-engineering
components:
- Claude Code
- Codex
- Deep Agents CLI
- LangSmith
- Docker
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/evaluating-skills
published_at: '2026-06-30'
---

## 概要

LangChainは、Claude CodeやDeep Agents CLIなどのコーディングエージェントにLangChain/LangSmithエコシステムを使わせるための『スキル』を作成する過程で、そのスキルが実際に性能を改善しているかを検証するテストパイプラインを構築した。Dockerで再現性のあるクリーンな実行環境を用意し、スキルあり/なしでタスクを実行させて比較し、ツール呼び出しの有無やターン数などの指標をLangSmithで記録・比較している。

## 設計のポイント

- スキルの効果検証は『スキルなしで実行→スキルありで実行→比較』という対照実験として設計する
- コーディングエージェントは開始時のディレクトリ探索など初期状態に敏感なため、Dockerで再現可能なクリーン環境を用意する
- 採点しやすいよう、オープンエンドなタスクではなく既存のバグ修正のような制約されたタスクを選ぶ
- スキルが呼ばれたか/呼ばれるべきでない時に呼ばれていないか、タスク達成度、ターン数、実行時間を指標として並行に追う

## 使いどころ

- Claude CodeやCodexなど社内外のコーディングエージェント向けにスキルやプロンプト集を配布・改善したいチーム
- プロンプト追加がエージェント性能を本当に改善しているのか、勘ではなく数値で確認したい場合
- エージェントに渡すツール・指示が増えすぎて性能が落ちる問題を、progressive disclosure的なスキル設計で回避したいケース
