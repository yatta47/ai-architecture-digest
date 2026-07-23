---
type: guidance
title: 自律的にコードベースを操作するagentic codingの仕組み
title_original: Introduction to agentic coding
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Claude Code
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/introduction-to-agentic-coding
published_at: '2025-10-30'
---

## 概要

コード補完から会話型AI、そして自律的にマルチステップの開発タスクを実行するagentic codingへという進化を解説する記事。Claude Codeがプロジェクト全体の文脈を読み取り、計画・実装・検証を自律的に繰り返す仕組みを紹介する。

## 設計のポイント

- ゴールを起点にコンテキスト収集→計画→実装→検証を自律的に繰り返すループにする
- 静的な計画ではなく、収集した情報に応じて適応的に計画を更新する
- 人間はプラン確認と変更承認に専念し、反復デバッグはエージェントに任せる

## 使いどころ

- 複数ファイルにまたがるリファクタリングを行いたい開発チーム
- 新しいコードベースの構造をすばやく理解したい開発者
- 定型的なテスト作成や境界の明確なタスクを自動化したいエンジニア
