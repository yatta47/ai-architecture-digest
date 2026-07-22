---
type: guidance
title: Claude Codeのセッション管理と100万トークンコンテキストの使い方
title_original: 'Using Claude Code: session management and 1M context'
industry: cross-industry
cloud:
- multi-cloud
patterns:
- context-engineering
- memory-consolidation
components:
- Claude Code
- /usage
- compaction
- rewind
- subagents
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/using-claude-code-session-management-and-1m-context
published_at: '2026-04-15'
---

## 概要

Claude Codeが100万トークンのコンテキストウィンドウに対応したことを踏まえ、セッション分割・compact・rewind・サブエージェント活用など、コンテキスト管理の実践方法を解説する。コンテキストが増えるほど注意が分散し古い情報が邪魔になる「コンテキストロット」現象への対処が中心テーマ。

## 設計のポイント

- コンテキストウィンドウが上限に近づくと自動的に要約（compaction）されるため、良いcompactと悪いcompactの違いを理解して使いこなす
- 1つのプロンプトごとに新規セッションを始めるか、1つのセッションを使い続けるかをタスクの性質に応じて選ぶ

## 使いどころ

- 長時間にわたる大規模リファクタリングなどでコンテキストロットを避けたい開発者
- compact/rewind/subagentsの使い分けに悩んでいるClaude Codeの日常的なヘビーユーザー
