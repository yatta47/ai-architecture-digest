---
type: guidance
title: Claude Codeで『自分の未知』を洗い出しながら開発を進めるための手引き
title_original: 'A field guide to Claude Fable 5: Finding your unknowns'
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
- human-in-the-loop
- spec-driven-development
components:
- Claude Code
- Claude Fable 5
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns
published_at: '2026-07-06'
---

## 概要

Claude Fable 5を使った開発では、成果物の質が『自分の未知（unknowns）をどれだけ明確化できるか』で決まるという考察。既知/未知を4象限（既知の既知・既知の未知・未知の既知・未知の未知）に分け、実装の前・最中・後を通じて未知を発見していく反復プロセスとして、ブラインドスポットパス、ブレスト/プロトタイプ、インタビューなどの具体的パターンを紹介する。

## 設計のポイント

- プロンプトは具体的すぎても曖昧すぎても失敗するため、まず自分の立ち位置・経験・前提をClaudeに伝えてから協働を始める。
- 『ブラインドスポットパス』で未知の未知を言語化させ、見落としを実装前に洗い出す。
- ブレストやプロトタイプで『見れば分かるが書き出せない』暗黙の要件を早期に確定し、後工程での高コストな手戻りを避ける。
- 仕様の探索を実装前に前倒しし、後段の手戻りコストを下げる設計思想を採る。

## 使いどころ

- 不慣れな領域やコードベースで作業し、未知を減らしたい人
- デザインのように、良し悪しを見て初めて判断できる曖昧なタスクに取り組む場面
- Claudeを思考パートナーにして進めたいとき
