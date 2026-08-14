---
type: announcement
title: GitHub CopilotにxAIのGrok 4.6が追加、エージェント型コーディングに対応
title_original: Grok 4.6 is now available in GitHub Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- ai-agent
components:
- GitHub Copilot
- Grok 4.6
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-14-grok-4-6-is-now-available-in-github-copilot
published_at: '2026-08-14'
---

## 概要

xAIの推論モデルGrok 4.6が、VS CodeやCopilot CLIなど各種エディタのモデルピッカーからGitHub Copilotで利用可能になった。長期の推論とツール利用が必要なエージェント型コーディングタスクで強い結果を示すとされ、従量課金のプロバイダー標準価格で提供される。

## 設計のポイント

- Enterprise/BusinessプランはCopilot設定でGrok 4.6ポリシーを個別に有効化する必要があり、デフォルトはオフ
- 複数モデルをモデルピッカーで切り替え可能にすることで、タスク特性に応じたモデル選択を利用者に委ねている

## 使いどころ

- 長時間・多ステップの推論とツール呼び出しが必要なエージェント型コーディングを行う開発者
- 既存のClaudeやGPT系モデルと使い分けてタスクごとに最適なモデルを試したいチーム
