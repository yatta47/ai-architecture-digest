---
type: guidance
title: CLAUDE.md・ルール・スキル・フック・サブエージェントをいつ使い分けるか、Claude Codeの指示設計フレームワーク
title_original: 'Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents'
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
components:
- Claude Code
- CLAUDE.md
- Skills
- Hooks
- Subagents
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
published_at: '2026-06-18'
---

## 概要

Claude Codeの振る舞いをカスタマイズする7つの方法（CLAUDE.md、ルール、スキル、サブエージェント、フック、出力スタイル、システムプロンプト追記）を、いつ読み込まれるか・圧縮（compaction）後にどうなるか・コンテキストコストの3軸で比較し、使い分けの判断基準を示す。特にCLAUDE.mdは常時読み込まれてトークンコストが高いため200行以内に抑え、チーム固有の規約はパス限定ルールへ、手順書はスキルへと切り出すことを推奨している。

## 設計のポイント

- 常時ロードされ圧縮後も再注入されるCLAUDE.mdやルールは高コストなので、ハードな制約や規約はパス限定ルールに、手順的な作業はスキルに逃がしてコンテキストコストを下げる。
- サブエージェントは呼び出されるまでメインコンテキストのコストがゼロで、最終的な要約だけが本セッションに返るため、並列作業や隔離したいサイドタスクに向く。
- フックはライフサイクルイベントで発火し圧縮の影響を受けないため、リンター実行や完了時のSlack通知など決定的な自動化に向いている。

## 使いどころ

- 共有リポジトリのCLAUDE.mdが肥大化し、無関係なチームの規約まで毎セッション読み込まれてトークンを浪費している組織。
- 手順書とハード制約、チーム規約が混在していて、どの仕組みに何を書くべきか判断基準が欲しいエンジニアリングリード。
- モノレポで複数チームが同じCLAUDE.mdに追記し続け、誰も削除できずに膨張している状況を整理したいチーム。
