---
type: case
title: Brexにおけるagentic codingの全社導入と生産性向上
title_original: How Brex improves code quality and productivity with Claude Code
company: Brex
industry: financial-services
cloud: []
patterns:
- ai-agent
- text-to-sql
components:
- Claude Code
- MCP
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-brex-improves-code-quality-and-productivity-with-claude-code
published_at: '2025-10-30'
---

## 概要

金融プラットフォームBrexが全社的にClaude Codeを導入し、非エンジニアを含む多職種がコード変更やツール開発を行えるようにした事例。text-to-SQLインターフェース「Brex Explorer」やCLAUDE.mdによる構造化されたコンテキスト管理などの実践を紹介する。

## 設計のポイント

- ディレクトリ単位にCLAUDE.mdを整備しドメイン固有の文脈を蓄積する
- MCPサーバー経由でtext-to-SQLインターフェースを構築し非エンジニアにデータアクセスを開放する
- ドキュメント陳腐化を検知するCI/CDチェックを組み込み、常に最新のコンテキストを保つ

## 使いどころ

- 非エンジニア職種にもコード変更権限を広げたい組織
- 複雑なモノレポの知識をオンボーディングに活用したいエンジニアリング組織
- SQLを書けない担当者にもデータ照会を開放したいデータ分析チーム
