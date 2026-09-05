---
type: announcement
title: GitHub Copilotの週次アップデート：モデル選択肢の拡大とエージェントセッション管理の強化
title_original: GitHub Copilot weekly releases — August 31
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- ai-agent
components:
- GitHub Copilot
- Claude Fable 5.1
- Gemini 3.8 Flash
- VS Code
- GitHub Copilot CLI
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-04-github-copilot-weekly-releases-august-31
published_at: '2026-09-04'
---

## 概要

GitHub Copilotの週次アップデートで、Claude Fable 5.1とGemini 3.8 Flashが利用可能なモデルに追加されたほか、コンテンツ除外設定がエージェント型ワークフロー全体に適用されるようになった。VS Code側ではレビュー指摘・失敗チェック・マージコンフリクトを自動解消するAgent Mergeがプレビュー公開された。

## 設計のポイント

- 複数のLLM（Claude Fable 5.1、Gemini 3.8 Flashなど）から選べるモデルピッカーを用意し、モデルをプラン管理と切り離して切り替え可能にする
- コンテンツ除外設定をCLIやアプリを含むエージェント型ワークフロー全体で一貫して適用し、機密コードを文脈から除外する
- Agent Mergeでレビュー指摘・CI失敗・マージコンフリクトの解消までを自動化し、マージ可能な状態まで持っていく

## 使いどころ

- 複数のAIコーディングモデルをタスクに応じて使い分けたい開発チーム
- IDE内で複数のエージェントセッションを並行して管理し、マージまで自動化したい場合
