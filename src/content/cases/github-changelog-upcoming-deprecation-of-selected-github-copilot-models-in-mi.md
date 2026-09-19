---
type: announcement
title: GitHub Copilotの一部モデルを10月に廃止、代替モデルへの移行を案内
title_original: Upcoming deprecation of selected GitHub Copilot models in mid-October
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
- multi-model-routing
components:
- GitHub Copilot
- Gemini 3.7 Flash
- GPT-5.5
- GPT-5.4
- Grok 4.5
outcome:
  type: reliability
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-18-upcoming-deprecation-of-selected-github-copilot-models-in-mid-october
published_at: '2026-09-18'
---

## 概要

GitHubは2026年10月19日付で、Gemini 3.7 Flash、GPT-5.5、GPT-5.4、GPT-5.4 mini、GPT-5 mini、Grok 4.5をGitHub Copilotの全機能から廃止すると発表した。デフォルトのモデル有効化設定では、それぞれの後継モデル（GPT-5.6 Sol/Luna、Gemini 3.8 Flash、Grok 4.6など）が自動的に有効化される。

## 設計のポイント

- 廃止対象モデルごとに1対1の推奨代替モデルを明示し、移行判断のコストを下げる
- グローバルデフォルトが有効な組織には後継モデルを自動的に有効化し、明示的な作業なしに移行できるようにする

## 使いどころ

- 特定モデルを名指しでワークフローや統合に組み込んでいる組織が移行計画を立てる場合
