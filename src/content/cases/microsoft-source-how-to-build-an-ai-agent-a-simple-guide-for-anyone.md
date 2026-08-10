---
type: guidance
title: コードを書かずにMicrosoft 365 CopilotでAIエージェントを作る5ステップ
title_original: 'How to build an AI agent: A simple guide for anyone'
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- human-in-the-loop
components:
- Microsoft 365 Copilot
- Copilot Chat
- Agent Builder
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/signal/articles/how-to-build-an-ai-agent-guide/
published_at: '2026-08-10'
---

## 概要

Microsoft 365 Copilotを使い、コーディング不要で業務用AIエージェントを構築するための5ステップガイド。課題定義→既存エージェントの確認→Agent Builderでの試作→ナレッジソース接続と出力定義→テスト・共有・拡張という流れで、チャットが応答するだけなのに対しエージェントは実際にタスクを実行できる点を強調する。

## 設計のポイント

- 技術ではなく解決したい業務課題から始め、エージェントが情報取得・タスク完了・自律行動のどこまでを担うかを先に決める
- ゼロから作る前にCopilotのAgentsストアで既存の作成済みエージェントが要件を満たさないか確認する
- メール・SharePoint・Webサイトなど参照させる情報源と出力フォーマット（レポート・表・コードなど）を明示的に定義してからチューニングする
- 実運用テストでの気づきを元にインストラクションを繰り返し調整し、曖昧な情報は推測せず人にエスカレーションさせる

## 使いどころ

- コーディング経験のない一般社員が自分の業務（週次レポート作成、共有受信箱の仕分けなど）を自動化したい場合
- 反復的な情報収集・要約タスクをまず小さく試作してから徐々に拡張したいチーム
- 曖昧な判断は人が最終確認する形でAIエージェントを安全に業務導入したい組織
