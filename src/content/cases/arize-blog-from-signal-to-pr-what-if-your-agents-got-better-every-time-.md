---
type: announcement
title: 本番トレースから障害の根本原因を分析し修正PRまで自動生成するArizeのSignal
title_original: 'From Signal to PR: What if your agents got better every time they failed?'
company: Arize
industry: cross-industry
cloud: []
patterns:
- root-cause-analysis
- ai-agent
- ci-cd
- eval
components:
- Arize AX
- Signal
- Agent Studio
outcome:
  type: reliability
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/from-signal-to-pr/
published_at: '2026-07-29'
---

## 概要

ArizeはArize AXに組み込まれたマネージドエージェント「Signal」を発表した。Signalは本番のエージェントトレースを継続的にレビューして再発する失敗パターンをランク付けされたIssueにまとめ、根本原因分析と修正案を提示し、リポジトリ接続があれば修正PRの作成まで行う。エンジニアの承認を前提に、テレメトリを人間が読むだけの情報から自律的に改善提案へつなげる自己改善ループを目指す。

## 設計のポイント

- 本番トレースを継続的に監視し、類似する失敗を自動でグルーピングしてランク付けされたIssueとして提示する
- 各Issueに根拠となるエビデンス・根本原因分析・修正案を紐付け、リポジトリアクセスがあれば修正PR作成まで自動化する
- Investigate→Propose→Review→Ship→Observeという改善ループを設計し、最終判断は常に人間のエンジニアが行う
- 継続スイープ・スケジュール実行・運用イベント起点など、投資対効果に応じて調査のトリガーを選べるようにする

## 使いどころ

- 本番エージェントの障害調査と原因特定に多くの時間を費やしているSRE/運用チーム
- 障害の根本原因分析から修正PR作成までを自動化し対応時間(MTTR)を短縮したいチーム
- トレースと評価データを継続的な品質改善のフィードバックループに活用したいプロダクトチーム
