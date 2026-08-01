---
type: announcement
title: GitHub CopilotにおけるGeminiモデルの非推奨化と後継モデルへの移行
title_original: Gemini 2.5 Pro and Gemini 3 Flash deprecated
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- GitHub Copilot
- Gemini 2.5 Pro
- Gemini 3 Flash
- Gemini 3.1 Pro
- Gemini 3.6 Flash
outcome:
  type: reliability
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-31-gemini-2-5-pro-and-gemini-3-flash-deprecated
published_at: '2026-07-31'
---

## 概要

GitHubは2026年7月31日付でCopilot Chat/inline edits/agentモードなど全体で利用可能だったGemini 2.5 ProとGemini 3 Flashを非推奨とし、それぞれGemini 3.1 Pro (Preview)とGemini 3.6 Flashへの移行を案内した。Enterprise管理者はモデルポリシーで代替モデルを有効化する必要がある。

## 設計のポイント

- 非推奨モデルの利用は自動的に停止されるのではなく、管理者側のモデルポリシー設定で代替モデルを明示的に有効化する運用

## 使いどころ

- Copilot Enterprise/Business管理者が、モデル非推奨化に合わせてワークフローや統合を計画的に移行する場面
