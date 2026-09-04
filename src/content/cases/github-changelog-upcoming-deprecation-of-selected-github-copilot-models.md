---
type: announcement
title: GitHub Copilotの一部モデル非推奨化と移行
title_original: Upcoming deprecation of selected GitHub Copilot models
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
components:
- GitHub Copilot
- Gemini 3.8 Flash
- Claude Opus 5
- Kimi K3
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-03-upcoming-deprecation-of-selected-github-copilot-models
published_at: '2026-09-03'
---

## 概要

GitHub CopilotはGemini 3.5/3.6 Flash、Kimi K2.7 Code、Claude Opus 4.7を2026年10月2日付けで全モードにわたり非推奨にし、それぞれGemini 3.8 Flash、Kimi K3、Claude Opus 5への移行を促すアナウンス。管理者は移行期限前に代替モデルのモデルポリシーを有効化しておく必要がある。

## 設計のポイント

- Copilot管理者は移行期限前に代替モデルへのモデルポリシーを有効化しておく必要がある
- モデル非推奨後の除去は自動で行われ、利用側での追加対応は不要

## 使いどころ

- Copilot Enterprise/Business管理者が組織内のモデル利用を計画的に切り替えたい場合
- 非推奨モデルに依存したワークフローや自動化を事前に洗い出して移行したいチーム
