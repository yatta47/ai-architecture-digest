---
type: opinion
title: エージェントは自分の権限を判断できない問題とツール層での検査
title_original: 'AI agent permissions: Why agents don’t know what you’re allowed to do'
company: Arize
industry: cross-industry
cloud: []
patterns:
- guardrails
- human-in-the-loop
- eval
components:
- Arize AX
- Arize Phoenix
- Claude Code
outcome:
  type: risk-compliance
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/ai-agent-permissions/
published_at: '2026-10-15'
---

## 概要

Arizeは、会話中の主張だけではモデルが権限を確認できず、正当な作業を拒否したり偽の権威を受け入れたりすると論じる。対策としてツール層での権限チェックとトレースによる観測を挙げ、Claude Codeのauto modeの検知結果にも触れる。

## 設計のポイント

- 権限の検証をモデルの判断に任せず、ツール呼び出し側で強制する
- 破壊的操作の既定を安全側にしつつ、正当な利用者向けの許可経路を用意する
- トレースで権限判断を事後に検証する

## 使いどころ

- コマンド実行などの強い権限を持つエージェントを運用する開発者
