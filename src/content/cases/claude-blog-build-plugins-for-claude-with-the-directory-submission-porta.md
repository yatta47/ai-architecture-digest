---
type: announcement
title: Claudeディレクトリ向けプラグイン提出ポータルの公開
title_original: Build plugins for Claude with the directory submission portal
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- policy-as-code
components:
- Claude
- Claude Code
- MCP 2.0
- Claude directory
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/build-plugins-for-claude
published_at: '2026-09-25'
---

## 概要

Anthropicは、MCPコネクタやAgent Skillsをまとめたプラグインを、新しいポータルでClaudeディレクトリに提出・審査追跡・公開・分析できるようにした。提出時の自動検証と安全性スキャン、MCP 2.0のMCP AppsやEnterprise Managed Authにも対応する。

## 設計のポイント

- 単一のMCPコネクタか、MCPとスキルを束ねたバンドルのどちらかで提出する。
- 提出時に自動検証と安全性スキャンを行い、審査状況とフィードバックを確認できる。
- 公開後はインストール数や検索経由の閲覧を見て改善する。

## 使いどころ

- Claude向けの拡張を外部に配布したいサービス提供者。
- 社内ツールをMCPとスキルとして整備している開発者。
- 企業向けにOAuthを簡素化したいコネクタ開発者。
