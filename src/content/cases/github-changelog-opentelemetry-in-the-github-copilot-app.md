---
type: announcement
title: GitHub CopilotアプリでのOpenTelemetryによるエージェント活動の集中監視
title_original: OpenTelemetry in the GitHub Copilot app
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
components:
- GitHub Copilot app
- OpenTelemetry
outcome:
  type: reliability
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-22-opentelemetry-in-the-github-copilot-app
published_at: '2026-09-23'
---

## 概要

GitHub Copilotアプリがエンタープライズ管理設定でOpenTelemetryを構成でき、エージェントのセッション、モデルへのリクエスト、ツール利用のトレースを既存の監視ツールへ送れるようになった。プロンプトと応答の内容は既定で除外される。

## 設計のポイント

- managed-settings.jsonで管理者が一元的にテレメトリを有効化し、開発者ごとの設定を不要にしている。
- OTel標準で既存の監視基盤にトレースを流し、エージェント専用の監視基盤を別途立てずに済ませている。
- 内容キャプチャを既定オフにしてプライバシーに配慮している。

## 使いどころ

- エージェント挙動の想定外を調査したい管理者。
- 組織内のエージェント利用状況をセッション単位で分析したいプラットフォームチーム。
- 既存のObservability基盤にエージェントの可視化を統合したい組織。
