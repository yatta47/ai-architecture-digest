---
type: guidance
title: Claudeによるレスポンシブレイアウト生成とリファクタリング
title_original: Build responsive web layouts
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Claude Code
- Claude.ai
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/build-responsive-web-layouts
published_at: '2025-10-10'
---

## 概要

メディアクエリの手動記述やデバイス実機テストに頼っていたレスポンシブデザインの検証を、Claudeによる生成とClaude Codeによる既存スタイルシートのリファクタリングで効率化する手法を解説する記事。

## 設計のポイント

- Claude.aiでレイアウト要件から動作するHTML/CSSのたたき台を素早く生成する
- Claude Codeに既存コードベース全体のビューポート依存問題を検出・修正させる
- ブレークポイントをデバイス分類ではなくコンテンツが崩れる実際の幅に合わせて決める

## 使いどころ

- レスポンシブ対応の手戻りを減らしたいフロントエンド開発者
- 大規模コードベースのレスポンシブ実装を横断的にリファクタリングしたいチーム
- デバイス実機テストにかかる工数を削減したい開発チーム
