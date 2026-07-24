---
type: announcement
title: 開発者コンソールでのプロンプト評価機能
title_original: Evaluate prompts in the developer console
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- eval
- prompt-optimization
components:
- Anthropic Console
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/evaluate-prompts
published_at: '2024-07-09'
---

## 概要

Anthropic Console上でプロンプトの生成・テスト・評価を一貫して行える機能を追加。自動テストケース生成や複数プロンプトの出力を並べて比較する機能により、本番投入前にプロンプト品質への確信を持てるようにする。

## 設計のポイント

- タスク説明からClaude自身にテストケースの入力変数を自動生成させ、手作業でのテストデータ作成を省く
- 複数バージョンのプロンプトを同一テストスイートに対して実行し出力を並べて比較できるようにする

## 使いどころ

- スプレッドシートやコードで手動管理していたプロンプトテストを一元化したいチーム
- プロンプトの改善サイクルを高速に回したい開発者
