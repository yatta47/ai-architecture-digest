---
type: announcement
title: MCPを拡張したインタラクティブ連携「MCP Apps」の提供開始
title_original: Your favorite work tools are now interactive connectors inside Claude
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- MCP
- MCP Apps
- Asana
- Slack
- Figma
- Amplitude
- Box
- Canva
- Clay
- Hex
- monday.com
- Salesforce Agentforce 360
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/interactive-tools-in-claude
published_at: '2026-01-26'
---

## 概要

Claudeに『MCP Apps』という仕組みが追加され、Asana・Slack・Figma・Canvaなど主要な業務ツールがチャット内でインタラクティブに操作できる連携先として組み込まれた。MCP(Model Context Protocol)を拡張したオープン標準により、ユーザーはタブを切り替えずにチャート作成やタスク管理、デザイン編集などをその場で確認・操作できる。

## 設計のポイント

- MCPというオープンな接続規格を拡張し、任意のMCPサーバーがリッチなUIを持つインタラクティブ連携を提供できるようにする
- 実行結果を裏側で処理するだけでなく、チャット内にプレビューを表示してユーザーが内容を確認・修正してから確定できるようにする(Slack下書きプレビューなど)
- 特定ベンダーに閉じず、Claude以外のAI製品でも利用可能な共通拡張として設計する

## 使いどころ

- 複数の業務アプリを行き来せず、チャット内で一括してタスク管理やドキュメント検索を完結させたいチーム
- 生成結果を送信・実行する前に必ず人が確認したい業務(メッセージ送信、ボード更新など)
- サードパーティサービスが自社ツールをエージェント向けに接続可能にしたい開発者
