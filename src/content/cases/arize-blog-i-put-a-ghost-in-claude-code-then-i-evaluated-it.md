---
type: case
title: Claude Codeのmodをトレースし評価するハロウィンmod
title_original: I put a ghost in Claude Code. Then I evaluated it
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- guardrails
- llmops
components:
- Claude Code
- Arize AX
- Arize Phoenix
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/i-put-a-ghost-in-claude-code-then-i-evaluated-it/
published_at: '2026-10-27'
---

## 概要

Claude Codeのmod（イベントを書き換えるTypeScript関数）として、各ターンを評価し危険コマンドを止めるハロウィンmodを作り、Arize AXでトレース・評価した。modはエージェントの入出力と権限を変えるため効果を測る必要があることを示す。

## 設計のポイント

- modは非サンドボックスで動くので、導入前に権限を確認する。
- エージェントのハーネス層の変更もトレースして評価対象にする。
- 危険コマンド遮断をmod内でguardrailとして実装する。

## 使いどころ

- コーディングエージェントを拡張するチーム。
- ハーネス変更の効果を観測したい場合。
