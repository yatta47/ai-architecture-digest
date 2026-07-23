---
type: guidance
title: Claudeのスキル(SKILL.md)を作る5ステップと検証方法
title_original: 'How to create Skills: Key steps, limitations, and examples'
industry: cross-industry
cloud: []
patterns:
- context-engineering
- prompt-optimization
components:
- Claude.ai
- Claude Code
- Claude Developer Platform
- Skills API
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples
published_at: '2025-11-19'
---

## 概要

Claudeの能力を特定タスク向けに拡張する「スキル(SKILL.md)」の作り方を、要件定義からname/description/instructionsの記述、Claude.ai・Claude Code・Developer Platformへのアップロード、テストと反復改善までの5ステップで解説する記事。特にdescriptionはスキルが起動するかどうかを左右する最重要要素であり、具体的な能力・トリガー・境界を明記することが推奨されている。

## 設計のポイント

- トリガー精度を左右するdescriptionには具体的な動詞・ユースケース・非対象範囲を明記して設計する
- スキルをname(識別子)・description(起動条件)・instructions(実行手順)の3要素で構成する
- instructionsは概要・前提・実行手順・例・エラー処理・制限のような階層構造で記述し複雑なワークフローを段階分割する
- 通常系・エッジケース・対象外リクエストの3種のテストマトリクスで起動精度と出力一貫性を検証する

## 使いどころ

- PDF処理や財務分析など反復的な専門業務をエージェントに標準化させたいチーム
- Claude.ai・Claude Code・Developer Platformでカスタムスキルを構築・配布したい開発者
- スキルの誤起動や出力のばらつきを改善したい運用・プロンプトエンジニアリング担当者
