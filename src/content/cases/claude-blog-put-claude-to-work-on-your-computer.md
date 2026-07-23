---
type: announcement
title: 画面操作でタスクを完了するClaudeのコンピュータ操作機能とDispatch
title_original: Put Claude to work on your computer
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- guardrails
components:
- Claude Cowork
- Claude Code
- Dispatch
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/dispatch-and-computer-use
published_at: '2026-03-23'
---

## 概要

Claude CoworkとClaude Codeに、コネクタが無いアプリでも画面をクリック・操作してタスクを完了できるコンピュータ操作機能を研究プレビュー公開。スマホから継続会話でタスクを依頼できるDispatchと組み合わせ、外出中でもPC上の作業を代行させられる。

## 設計のポイント

- コネクタがある場合はそちらを優先し、無い場合のみ画面操作にフォールバックする優先順位設計にする
- 新しいアプリへのアクセスは都度明示的な許可を求め、機微データを扱うアプリはデフォルトで対象外にする
- プロンプトインジェクションを想定し、モデル内部のアクティベーションを自動スキャンして異常操作を検知する

## 使いどころ

- API連携のないレガシーアプリやブラウザ操作を自動化したい場面
- 外出先からタスクを依頼し、帰宅後に完了した成果物だけを確認したいワークスタイル
