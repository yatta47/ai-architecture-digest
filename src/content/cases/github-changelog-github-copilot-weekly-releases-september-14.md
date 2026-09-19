---
type: announcement
title: GitHub Copilot週次アップデート：モデル選択・コードレビュー・エージェント機能強化
title_original: GitHub Copilot weekly releases — September 14
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-model-routing
- llmops
components:
- GitHub Copilot
- GitHub Copilot CLI
- VS Code Agents
- Sentry
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-18-github-copilot-weekly-releases-september-14
published_at: '2026-09-18'
---

## 概要

GitHub Copilotの週次アップデートでは、コスト・品質・応答速度のバランスを選べるモデル自動選択の階層（efficiency/balance/intelligence）、コードレビューでの既対応コメント自動解決、Sentryのクラッシュレポートから修正PRまでをつなぐCopilotアプリのSentryキャンバス、VS CodeのAgentsウィンドウでDev Containerを使ったエージェント実行などが追加された。

## 設計のポイント

- 同一のモデル群からコスト・品質・応答速度の重み付けだけを変えた3階層（efficiency/balance/intelligence）を用意し、用途に応じてモデル自動選択を切り替えられるようにする
- クラッシュレポート（Sentry）からエージェントによる原因調査・修正・PR作成までを一つのキャンバスでつなぐ
- エージェント実行をプロジェクト固有のDev Container上で行い、依存関係やツールをローカル開発環境と揃える

## 使いどころ

- コストと応答速度のバランスをタスクごとに変えたい開発チーム
- クラッシュレポートから修正PRまでの往復を短縮したいチーム
- エージェントにプロジェクト固有のツールチェーンを使わせたい場合
