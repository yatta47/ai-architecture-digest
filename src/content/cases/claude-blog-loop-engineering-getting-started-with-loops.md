---
type: guidance
title: Claude Codeのループ設計ガイド：ターン型からプロアクティブ型へ
title_original: 'Loop engineering: Getting started with loops'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- event-driven
- parallel-execution
components:
- Claude Code
- /goal
- /loop
- /schedule
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/getting-started-with-loops
published_at: '2026-06-30'
---

## 概要

Claude Codeチームが、エージェントの反復作業を「トリガー方法」「停止条件」「使うプリミティブ」で4種類(ターン型・ゴール型・時間型・プロアクティブ型)に整理し、それぞれの使いどころとトークン管理のコツを解説する記事。単純なタスクはターン型で十分だが、繰り返し作業や外部システムとの連携が必要な場面では/goalや/loop、/scheduleを使ったループ設計が有効だとしている。

## 設計のポイント

- タスクの複雑さに応じてターン型→ゴール型→時間型→プロアクティブ型の順に段階的にループの粒度を上げる
- ゴール型ループ(/goal)ではテスト通過数などの決定論的な完了基準とターン数上限を明示し、評価モデルに停止判定を委ねる
- SKILL.mdに検証手順をコード化してClaudeが自己検証できる範囲を広げ、ループの信頼性と自律性を高める
- プロアクティブループでは定型作業を小型・高速モデルに任せ、判断が必要な部分だけ高性能モデルを使う

## 使いどころ

- UIの変更をブラウザで実際に動かして検証したいような、自己検証可能なタスクの反復
- PRのCI失敗やレビューコメント対応など、外部システムの状態変化に追従したい定期チェック
- Slackのバグ報告のトリアージのように、人手を介さず継続稼働させたい定型業務ストリーム
- Lighthouseスコアなど数値化できる目標を持つ改善タスクの自動反復
