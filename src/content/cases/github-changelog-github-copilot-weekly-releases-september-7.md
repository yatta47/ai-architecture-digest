---
type: announcement
title: Copilotがモデル適応型ルーティングとJira連携を追加する週次アップデート
title_original: GitHub Copilot weekly releases — September 7
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- ai-agent
components:
- GitHub Copilot
- Project HydraFusion
- GitHub Copilot CLI
- Visual Studio Code
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-10-github-copilot-weekly-releases-september-7
published_at: '2026-09-10'
---

## 概要

GitHub CopilotにJira連携、Copilot CLIでのモデル自動ルーティング(Project HydraFusion)、VS Codeでの定期エージェントタスクや音声モードなどが追加された週次リリース。HydraFusionはローカル・クラウド・複合モデル間でタスクごとに性能・コスト・レイテンシのバランスを取るセマンティックルーティングを行う。

## 設計のポイント

- タスクごとにローカル/クラウド/複合モデルへ自動振り分けするセマンティックルーティングで性能とコストのバランスを取る
- 定期実行エージェントタスク(automations)を導入し、人手のトリガーなしに継続的なエージェント運用を可能にする

## 使いどころ

- 外部ツール(Jira等)の課題をそのままAIエージェントの調査・実装フローに取り込みたい開発チーム
- モデル選定のコストとレイテンシを都度手動で調整したくない開発者
