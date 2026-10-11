---
type: announcement
title: Copilotの週次更新：エージェントのローカルサンドボックスが一般提供
title_original: GitHub Copilot weekly releases — October 5
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- defense-in-depth
- multi-model-routing
components:
- GitHub Copilot
- Copilot CLI
- VS Code
- Ollama
- Claude Haiku 5.5
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-09-github-copilot-weekly-releases-october-5
published_at: '2026-10-09'
---

## 概要

Copilotの週次リリースまとめ。ファイル・ネットワーク・認証情報へのエージェントのアクセスを制限するローカルサンドボックスが一般提供となり、Claude Haiku 5.5の提供やCLIでのOllamaローカルモデル検出も加わった。

## 設計のポイント

- エージェントの権限をファイル・ネットワーク・認証情報の単位でサンドボックスにより制限する。
- クラウドモデルとローカルのOllamaモデルを同じ/modelの選択肢に並べ、ワークフローを変えず切り替えられる。
- 複数のエージェントセッションを並べて比較し、不要なworktreeを整理できる。

## 使いどころ

- エージェントに自律実行させる際の被害範囲を限定したい開発組織。
- 機密コードでローカルモデルを併用したいチーム。
- 複数エージェントの並行作業を管理する開発者。
