---
type: announcement
title: MCPサーバー・プラグイン・スキルを一元化するCopilotのCustomizeタブ
title_original: GitHub Copilot app Customize tab is generally available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- GitHub Copilot
- MCP
- Azure DevOps
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-25-github-copilot-app-customize-tab-is-generally-available
published_at: '2026-08-25'
---

## 概要

GitHub CopilotアプリのCustomizeタブがGA提供され、MCPサーバー・プラグイン・スキル・キャンバスを1つの画面から発見・導入できるようになった。Azure DevOpsのバックログをCopilotに調査・実装させるキャンバスなど、既存ツールとの連携をエージェントに橋渡しする導線を提供する。

## 設計のポイント

- MCPサーバー・プラグイン・スキル・キャンバスという異なる拡張形式を単一のCustomize画面に統合し、何を選べばよいか分からない利用者にも入口を用意する
- 厳選されたFeatured枠と種類別ブラウズを併用し、発見性とカタログの網羅性を両立させる

## 使いどころ

- 既存の社内ツールやワークフローをCopilotエージェントに接続したいチーム
- Azure DevOpsのバックログ整理などをエージェントに委任したい開発チーム
