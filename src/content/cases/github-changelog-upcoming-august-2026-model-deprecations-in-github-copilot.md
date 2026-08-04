---
type: announcement
title: GitHub Copilot、主要LLMモデル群を2026年9月に一斉廃止し後継モデルへ移行
title_original: Upcoming August 2026 model deprecations in GitHub Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- llmops
components:
- GitHub Copilot
- Copilot Chat
- Copilot Enterprise
- Gemini 3.1 Pro
- Gemini 3.6 Flash
- Claude Opus 4.5
- Claude Opus 4.6
- Claude Opus 4.7
- Claude Opus 4.8
- Claude Opus 5
- Claude Sonnet 4.5
- Claude Sonnet 4.6
- Claude Sonnet 5
- Raptor Mini
- MAI-Code-1-Flash
outcome:
  type: reliability
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-31-upcoming-august-2026-model-deprecations-in-github-copilot
published_at: '2026-07-31'
---

## 概要

GitHubはCopilot ChatやInline Edits、Agentモード、コード補完など全機能にわたり、Gemini 3.1 ProやClaude Opus 4.5/4.6、Claude Sonnet 4.5などのモデルを2026年9月1日付で廃止すると発表した。個人向け年間プランの一部ユーザーを除き、各モデルには後継モデル(Claude Sonnet 5やClaude Opus 5など)への移行が案内されている。管理者はCopilot設定のモデルポリシーで代替モデルを有効化する必要がある。

## 設計のポイント

- 廃止モデルごとに明確な後継モデルをマッピングして提示し、移行先選定の意思決定コストを下げる
- 契約プラン(年間個人プラン等)によって廃止適用範囲を例外扱いし、既存ユーザー体験への急激な影響を緩和する
- Enterprise管理者向けにモデルポリシーの有効化とモデルセレクターでの可視化という運用手順を明示する
- 廃止後は特別な削除作業を不要とし、モデル提供終了に伴う運用負荷を最小化する

## 使いどころ

- Copilot Enterpriseの管理者が組織全体のモデルポリシーを事前に見直し、廃止前に代替モデルへのアクセスを有効化する場面
- Copilot Chatや各種エージェントモードを業務ワークフローに組み込んでいるチームが、モデル切り替えによる互換性影響を事前に評価する場面
- 複数のLLMベンダー(Anthropic/Google/Microsoft等)のモデルを併用するプラットフォームで、モデルのライフサイクル管理方針を設計する場面
