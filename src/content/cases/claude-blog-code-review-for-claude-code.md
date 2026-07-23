---
type: announcement
title: PRごとにマルチエージェントを走らせるClaude Code Review
title_original: Bringing Code Review to Claude Code
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- eval
components:
- Claude Code
- Claude Code GitHub Action
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/code-review
published_at: '2026-03-09'
---

## 概要

PRオープン時に複数エージェントを並列起動してバグを検出・検証・重要度付けし、1件の要約コメントとインラインコメントとして返すCode Reviewを研究プレビュー公開。Anthropic社内では実質的なレビューコメントが付くPRの割合が16%から54%に向上した。

## 設計のポイント

- バグ探索エージェントを並列実行した後、別エージェントで誤検知を検証・フィルタリングしてから重要度付けする2段構成にする
- PRの規模・複雑度に応じてエージェント数とレビューの深さを動的にスケールし、小規模PRのコストを抑える
- 組織単位の月次上限・リポジトリ単位の有効化・ダッシュボードでトークン課金と利用範囲を管理者が制御できるようにする

## 使いどころ

- エンジニア一人当たりのコード生成量が急増し、人力レビューが追いつかなくなったチーム
- 大規模PRで見落とされがちな既存コードの潜在バグ（型不整合など）まで拾いたい場合
