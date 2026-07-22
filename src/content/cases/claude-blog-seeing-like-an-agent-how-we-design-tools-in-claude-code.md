---
type: guidance
title: エージェントの視点でツールを設計する：Claude Codeの知見
title_original: 'Seeing like an agent: how we design tools in Claude Code'
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- context-engineering
- human-in-the-loop
components:
- Claude Code
- AskUserQuestion
- bash
- code execution
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/seeing-like-an-agent
published_at: '2026-04-10'
---

## 概要

Claude Codeチームがエージェント向けツールをどう設計・検証・改良してきたかを、モデルの視点に立って考えるという方法論とともに解説する。ユーザーへの質問（elicitation）を改善するAskUserQuestionツールを例に、最初にExitPlanToolを流用した失敗から現在の形に至った試行錯誤を紹介している。

## 設計のポイント

- 汎用ツール（bashやコード実行）と専用ツールのどちらを与えるかを、モデル自身の得意・不得意に合わせて選ぶ
- モデルの出力を観察し実験を重ねることで「エージェントの視点で見る」感覚を養い、ツールの過不足を判断する

## 使いどころ

- 自作のエージェントハーネスでツール設計に悩んでいる開発者
- ユーザーへの確認（elicitation）のUXを改善したいエージェントプロダクトのチーム
