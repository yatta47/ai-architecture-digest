---
type: announcement
title: GitHub Copilotの一部AIモデルを段階的廃止、後継モデルへ移行を案内
title_original: Selected GitHub Copilot models deprecated
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- llmops
components:
- GitHub Copilot
- Copilot Chat
- Claude Sonnet 4.5
- Claude Sonnet 4.6
- Claude Sonnet 5
- Claude Opus 4.5
- Claude Opus 4.6
- Claude Opus 4.7
- Claude Opus 4.8
- Claude Opus 5
- Gemini 3.1 Pro
- Gemini 3.7 Flash
- Raptor Mini
- MAI-Code-1.1-Flash
- VS Code
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-31-selected-github-copilot-models-deprecated
published_at: '2026-08-31'
---

## 概要

GitHub Copilotは2026年9月1日付けでGemini 3.1 Pro、Claude Opus 4.5/4.6、Claude Sonnet 4.5/4.6、Raptor Miniなど複数モデルをChat・インライン編集・エージェントモード・コード補完から廃止し、後継の新モデルへの移行を案内した。Enterprise管理者はモデルポリシーで代替モデルを有効化する必要があり、廃止モデル自体を手動で削除する対応は不要とされている。

## 設計のポイント

- 複数のLLMベンダー（Anthropic、Google、Microsoft）のモデルを併存させ、管理者がポリシーで利用可否を切り替えられるモデルルーティング構成になっている。
- モデルの廃止時は自動的に旧モデルが無効化され、明示的な移行先モデルが提示されることで運用側の作業負荷を下げている。
- 個人向けの年間プランなど契約形態によって旧モデル（Claude Sonnet 4.6）の提供継続期間を差別化している。

## 使いどころ

- 多数のAIモデルをプロダクトに組み込み、ベンダー都合のモデル廃止に継続的に追従する必要があるSaaS運用チーム。
- Copilot Enterprise管理者が組織全体のモデルアクセスポリシーを一括管理する場面。
