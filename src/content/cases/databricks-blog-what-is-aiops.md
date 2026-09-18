---
type: guidance
title: AIOpsとは何か：可観測性とアクションの間をAIで埋める
title_original: What is AIOps?
industry: cross-industry
cloud: []
patterns:
- root-cause-analysis
- human-in-the-loop
components: []
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/what-is-aiops
published_at: '2026-09-17'
---

## 概要

2017年にGartnerが提唱したAIOpsは、マイクロサービス・マルチクラウド・エージェント駆動システムがオンコール担当者が読み切れない量の運用シグナルを生成するようになった2026年の環境で改めて重要になっている。AIOpsはログ・トレース・イベント・ネットワークトポロジーからAIで異常検知・イベント相関・根本原因特定を行い、可観測性とDevOpsを置き換えるのではなく、リスクの高いアクションには人による監督を残しながら意思決定を高速化する位置づけにある。

## 設計のポイント

- 可観測性が『何が起きているか』を示すのに対し、AIOpsはそのシグナルのノイズを減らし関連イベントを結びつけて『次に何をすべきか』の判断を助けるという役割分担を明確にする
- リスクの高い自動アクションについては人間の判断を残すヒューマンインザループを維持し、完全自律化を目指さない
- 手動でのオンコール確認が追いつかない量のログ・トレース・イベントを前提に、異常検知と根本原因特定を自動化してMTTRを短縮する

## 使いどころ

- 分散マイクロサービス・マルチクラウド環境でアラート疲れが起きているSRE/プラットフォームチーム
- リスクの高い自動修復には人の承認を残しつつMTTRを短縮したい運用チーム
