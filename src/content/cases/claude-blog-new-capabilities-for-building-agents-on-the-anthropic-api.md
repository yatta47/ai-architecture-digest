---
type: announcement
title: コード実行・MCP接続・ファイル管理・長時間キャッシュを追加したAnthropic APIのエージェント機能拡張
title_original: New capabilities for building agents on the Anthropic API
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Claude Opus 4
- Claude Sonnet 4
- MCP connector
- Files API
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/agent-capabilities-api
published_at: '2025-05-22'
---

## 概要

Anthropic APIにコード実行ツール、MCPコネクタ、Files API、最大1時間の拡張プロンプトキャッシュという4つの新機能が追加され、独自インフラを構築せずにデータ分析・外部システム連携・長時間コンテキスト維持が可能なAIエージェントを開発できるようになった。

## 設計のポイント

- サンドボックス化されたコード実行環境をAPIに統合し、Claudeを単なるコード提案者から反復的にデータ分析を行うエージェントへ拡張する
- MCPコネクタでリモートサーバーへの接続・ツール検出・認証をAPI側に肩代わりさせ、独自クライアント実装を不要にする
- プロンプトキャッシュのTTLを1時間まで延長し、長時間稼働するエージェントワークフローのコストとレイテンシを削減する

## 使いどころ

- データ可視化や統計分析をエンドツーエンドでAPI経由で完結させたい場合
- Asanaなど外部SaaSと連携しタスク管理を行うプロジェクト管理エージェントの構築
- 大量の背景知識やドキュメントを保持しながら長時間動作するエージェントアプリケーション
