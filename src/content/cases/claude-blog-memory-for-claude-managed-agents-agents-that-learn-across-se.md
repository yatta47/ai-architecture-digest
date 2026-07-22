---
type: announcement
title: Claude Managed Agentsのセッション横断メモリ機能
title_original: Built-in memory for Claude Managed Agents
industry: cross-industry
cloud:
- multi-cloud
patterns:
- memory-consolidation
- ai-agent
components:
- Claude Managed Agents
- Claude Platform
- Claude Console
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-managed-agents-memory
published_at: '2026-04-23'
---

## 概要

Claude Managed Agentsにファイルベースのメモリ層がパブリックベータで追加され、エージェントがセッションをまたいで学習内容を蓄積できるようになった。スコープ付き権限・監査ログ・ロールバックを備え、Netflixはセッション間の文脈引き継ぎ、Rakutenは初回エラーを97%削減、Wisedocsは書類検証を30%高速化するなど、各社が独自のメモリ基盤構築を代替する用途で活用している。

## 設計のポイント

- メモリをファイルとしてファイルシステム上にマウントし、既存のbash/コード実行ツールから読み書きできるようにする
- 組織全体向けは読み取り専用、ユーザー単位は読み書き可というようにストアごとにスコープと権限を分ける
- 変更はすべて監査ログに記録し、どのエージェント・セッション由来かを追跡してロールバックや redact を可能にする

## 使いどころ

- 長時間・反復実行するエージェントが過去セッションの気づきや人間からの修正を引き継ぎたい場合
- 独自の検索/記憶インフラを構築せず、繰り返し発生する問題パターンを学習させたいドキュメント処理パイプライン
- 複数エージェントが同じ知識ストアを並行利用しつつ、書き込み競合を避けたいマルチエージェント運用
