---
type: announcement
title: GitHub Copilotの週次アップデート:サブエージェント管理・メモリ・移植可能なプラグイン
title_original: GitHub Copilot weekly releases — August 10
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- memory-consolidation
- multi-agent-orchestration
components:
- GitHub Copilot CLI
- GitHub Copilot app
- Agent Plugins
- Kimi K3
- MAI-Code-1.1-Flash
- Ollama
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-13-github-copilot-weekly-releases-august-10
published_at: '2026-08-14'
---

## 概要

GitHub Copilotの週次リリースまとめ。エディタ横断で使い回せるAgent Plugins 1.0の一般提供、Copilot CLIでのサブエージェント管理(/tasks)やヘッドレスモードでの計画→実行の連結、JetBrainsでのセッションをまたいだCopilotメモリやOllamaのBYOK対応など、エージェント運用まわりの機能強化が中心。

## 設計のポイント

- プラグインをツール横断で一度書けば動く形にすることで、エージェントツールごとの個別実装を避ける
- サブエージェントと実行中タスクを/tasksで一元管理し、実行中でも追加プロンプトやコマンドをキューイングできるようにする
- セッションをまたいで文脈を保持するメモリ機能により、毎回同じプロジェクト情報を伝える手間を減らす

## 使いどころ

- 複数のエージェントツール(VS Code, CLI, アプリ)を横断してプラグインを再利用したい開発チーム
- 長時間のエージェントセッションで途中経過を巻き戻したり計画と実行を分離したい利用者
- 社内で自前のLLM(Ollama)をJetBrainsのCopilotから使いたいセキュリティ重視の組織
