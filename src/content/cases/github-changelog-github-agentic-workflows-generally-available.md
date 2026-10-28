---
type: announcement
title: Markdownで定義しActionsで動くエージェント型ワークフロー
title_original: GitHub Agentic Workflows generally available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- defense-in-depth
- ci-cd
- multi-model-routing
components:
- GitHub Agentic Workflows
- GitHub Actions
- GitHub Copilot CLI
- Actions Runner Controller
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available
published_at: '2026-10-28'
---

## 概要

GitHub Agentic Workflowsが一般提供となった。自然言語のMarkdownで定義した自動化をActions YAMLにコンパイルし、Issueトリアージ、CI失敗分析、ドキュメント更新などでコーディングエージェントを動かす。Accentureは開発速度が平均2倍超になったとしている。

## 設計のポイント

- 既存のActionsのランナーグループやポリシーをそのまま使う。
- 読み取り専用権限、サンドボックス、ファイアウォール、出力検証、脅威検知ジョブで多層防御する。
- モデルルーターとgh aw forecastでコストを制御する。

## 使いどころ

- Issueトリアージやテスト作成などを継続的に自動化したい開発組織。
- 自社の統制下でエージェントを安全に動かしたい企業。
