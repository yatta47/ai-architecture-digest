---
type: announcement
title: Anthropic APIにWeb検索ツールを追加、リアルタイム情報でエージェントを強化
title_original: Introducing web search on the Anthropic API
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
components:
- Claude 3.7 Sonnet
- Claude 3.5 Sonnet
- Claude 3.5 Haiku
- Claude Code
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/web-search-api
published_at: '2025-05-07'
---

## 概要

Anthropic APIにWeb検索ツールが追加され、Claudeが必要に応じて自律的に検索クエリを生成し最新情報を出典付きで回答へ組み込めるようになった。ドメインの許可/ブロックリストなど組織レベルの管理機能も備え、Claude CodeやPoe、Adaptiveなどの製品ですでに活用されている。

## 設計のポイント

- モデル自身が検索要否を判断し、結果を踏まえて段階的にクエリを改善するエージェント的な多段検索を可能にする
- 検索対象ドメインの許可/ブロックリストを組織単位で設定できるようにし、情報源の信頼性を統制する
- すべての検索結果に出典を明示し、回答の検証可能性を担保する

## 使いどころ

- 株価や規制動向など時々刻々変化する情報を扱う金融・法務分野のエージェント
- 最新のAPIドキュメントやライブラリ情報を参照しながらコーディングを支援するツール
