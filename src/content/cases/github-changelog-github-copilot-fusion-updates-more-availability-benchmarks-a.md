---
type: announcement
title: GitHub Copilot Fusion：タスクごとにモデルを選択・協調、Terminal-Benchで71.2%
title_original: 'GitHub Copilot Fusion updates: more availability, benchmarks, and models'
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- ai-agent
- eval
components:
- GitHub Copilot Fusion
- Terminal-Bench 4.1
- Claude Sonnet 5.5
- GPT-6.1 Terra
- MAI-Code-2
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models
published_at: '2026-11-17'
---

## 概要

Copilot FusionはタスクごとにモデルをCopilotが選択・協調する機能で、Terminal-Bench 4.1でFusion Maxが71.2%の解決率を示し、Fable 5.2より88%低コストとされる。github.com、Visual Studio、モバイルへ拡大し、Claude Sonnet 5.5などのモデルが追加された。

## 設計のポイント

- 利用者は労力レベルのみ指定し、モデル選択と協調は任せる。
- 公開リーダーボードで第三者評価を行う。
- コスト差を性能と併せて訴求する。

## 使いどころ

- モデル選択を意識せず性能とコストを両立したい開発者。
