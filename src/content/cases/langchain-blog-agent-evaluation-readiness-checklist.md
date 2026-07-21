---
type: guidance
title: エージェント評価基盤を作る前に確認すべきチェックリスト
title_original: Agent Evaluation Readiness Checklist
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
- llmops
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/agent-evaluation-readiness-checklist
published_at: '2026-06-30'
---

## 概要

本記事は前回の『Agent observability powers agent evaluation』の実践編として、エージェント評価を構築・運用する前に確認すべき項目をチェックリスト形式でまとめている。自動化に着手する前に実際のトレースを20〜50件手動でレビューすること、capability evalとregression evalを区別すること、失敗原因を分類できるまでエラー分析に時間をかけることなどを推奨し、評価はまずTrace単位（1ターン全体）から始めるべきだと説く。

## 設計のポイント

- 評価インフラを作る前に、実トレースを20〜50件手動でレビューして失敗パターンを把握する
- 『何ができるか』を測るcapability evalと『既存機能が壊れていないか』を測るregression evalを明確に分離して運用する
- エラー分析に評価工数の6〜8割を割き、失敗をプロンプト起因・ツール設計起因・モデル限界などに分類してから対策を決める
- 評価はまずTrace単位（最終応答・トラジェクトリ・状態変化の3軸）の全ターン評価から始め、必要に応じてRun単位・Thread単位を追加する

## 使いどころ

- これからエージェント評価基盤をゼロから構築しようとしているチームの立ち上げ時のチェックリストとして
- 評価の自動化を急ぐあまり、実際の失敗パターンを把握しないまま指標を作ってしまっている組織の見直し材料として
- 会話履歴を持つマルチターンエージェントの評価を、どの粒度から手を付けるべきか迷っている場合
