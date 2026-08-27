---
type: announcement
title: ClaudeのメモリをチャットとCoworkで統合し編集可能に
title_original: Claude's memory works everywhere, and you decide what's in it
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- memory-consolidation
- context-engineering
components:
- Claude
- Claude Cowork
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it
published_at: '2026-08-25'
---

## 概要

Claudeのメモリ機能がチャットとクラウド実行のClaude Cowork間で共通化され、どちらで得た文脈も他方に引き継がれるようになった。会話終了後の要約ではなく会話中に逐次トピックへ追記する方式で、保存内容はトピックごとのファイルとして閲覧・編集・削除でき、健康や信条などのセンシティブな話題はデフォルトで保存されず設定で明示的に有効化する必要がある。

## 設計のポイント

- メモリを事後要約ではなく会話中の逐次書き込みにすることで次の会話から即座に反映されるようにする
- 保存内容をトピックごとの短いファイル単位に分解し、ユーザーが直接読み書き・削除できる透明性を確保する
- センシティブな話題はデフォルトオフとし、有効化時も保存の都度通知することでプライバシーとのバランスを取る

## 使いどころ

- チャットでの雑談的なやり取りと、クラウド実行のエージェントタスクで同じ人物・プロジェクト文脈を使い回したいユーザー
- 四半期の優先事項やチーム定義など繰り返し説明が必要な背景情報を持つ利用者
