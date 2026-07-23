---
type: announcement
title: Slackのメンションから起動するClaude Codeエージェント連携
title_original: Claude Code and Slack
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- event-driven
components:
- Claude Code
- Slack
- Claude
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-code-and-slack
published_at: '2025-12-08'
---

## 概要

Slack上で@Claudeをメンションするだけで、その会話の文脈をもとにClaude Codeのセッションを自動起動できる新機能。バグ報告や機能要望などエンジニアリングの議論が集まるSlackから、そのままコーディング作業へシームレスに移行できる。セッションの進捗はSlackスレッドに逐次投稿され、完了後はセッションへのリンクとPR作成へのリンクが共有される。

## 設計のポイント

- Slackでのメンション内容をClaudeが解析し、コーディングタスクかどうかを自動判定してからClaude Codeセッションを起動する
- チャンネルやスレッドの直近メッセージを文脈として収集し、認証済みリポジトリの中から実行対象を自動選択する
- セッションの進行状況をSlackスレッドへステータス更新として返し、完了後はセッションへのリンクとPR作成用リンクを提示する
- 既存のClaude Slackアプリを拡張し、Claude Code on the webへタスクを中継する構成にすることで新規の統合コストを抑えている

## 使いどころ

- バグ報告がSlackに上がった直後に調査から修正まで素早く着手したい開発チーム
- チームのフィードバックを踏まえた小規模な機能実装やリファクタリングをその場で依頼したい場合
- エラー再現手順やユーザー報告などスレッド上の文脈を活かした協調的デバッグを行いたいとき
- コードレビューの指摘をそのままコーディングタスクとしてClaudeに引き継ぎたい場面
