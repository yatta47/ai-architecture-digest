---
type: announcement
title: Claudeコネクタ向け可観測性ダッシュボードとディレクトリ申請のアプリ内対応
title_original: Observability for developers building connectors
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- llmops
- root-cause-analysis
components:
- Model Context Protocol (MCP)
- Claude
- Claude Code
- Claude Cowork
outcome:
  type: reliability
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/observability-for-developers-building-connectors
published_at: '2026-06-08'
---

## 概要

Anthropicは、ディレクトリに公開したMCPコネクタの稼働状況を開発者が監視できるダッシュボードを追加した。アクティブユーザー数やツール呼び出し数、ヘルススコア、エラー率、レイテンシをツール単位で確認でき、Claude・Claude Code・Cowork横断での利用状況も比較できる。あわせて、MCPサーバーをディレクトリへ申請する機能もアプリ内で直接行えるようになった。

## 設計のポイント

- コネクタ単位のヘルススコアとツール別エラー内訳を提供し、障害箇所をすぐに特定できるようにしている。
- 利用状況をClaude・Claude Code・Cowork等のプロダクトサーフェス別に分解し、どの製品でコネクタが使われているかを可視化する。
- ディレクトリ申請フローをアプリ内に統合し、公開後の運用と申請プロセスを同じ管理画面で完結させている。

## 使いどころ

- サードパーティ製MCPコネクタを公開している開発者が、採用状況やランキング推移を継続的にモニタリングしたい場合。
- 接続先ツールのエラー率やレイテンシが急増した際に、どのツール呼び出しが原因かを素早く切り分けたい運用担当者。
- Team/EnterpriseプランでDirectory管理権限を持つ管理者が、複数コネクタの健全性を一元的に把握したい場合。
