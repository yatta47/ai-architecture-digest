---
type: announcement
title: 'GitHub Copilot週次リリース(9/21): 新モデルとローカルサンドボックス'
title_original: GitHub Copilot weekly releases — September 21
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- human-in-the-loop
components:
- GitHub Copilot
- Claude Opus 5.5
- GPT-6
- OpenTelemetry
- VS Code
- JetBrains
- Slack
- Microsoft Teams
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-25-github-copilot-weekly-releases-september-21
published_at: '2026-09-25'
---

## 概要

今週のCopilotはClaude Opus 5.5やGPT-6 Sol/Lunaなど新モデルの追加、Copilotアプリのローカルサンドボックス(公開プレビュー)、OpenTelemetryによる監視連携を含む。JetBrainsの低リスク自動承認やVS Codeのリモート実行なども更新された。

## 設計のポイント

- エージェントのファイル・ネットワーク・認証情報アクセスをローカルサンドボックスで制限する。
- 低リスクのツール呼び出しのみ自動承認し、高リスクは確認を求める。
- OpenTelemetryで既存の監視基盤にエージェント活動を集約する。

## 使いどころ

- コーディングエージェントを組織展開する際の安全策の検討。
- 複数モデルを用途別に使い分けたいチーム。
