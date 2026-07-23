---
type: announcement
title: Claude Sonnet 4が100万トークンコンテキストに対応、コードベース全体の一括処理が可能に
title_original: Claude Sonnet 4 now supports 1M tokens of context
company: Anthropic
industry: cross-industry
cloud:
- aws
- gcp
patterns:
- context-engineering
components:
- Claude Sonnet 4
- Amazon Bedrock
- Google Cloud Vertex AI
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/1m-context
published_at: '2025-08-12'
---

## 概要

Claude Sonnet 4のコンテキストウィンドウが100万トークンへと5倍に拡張され、Anthropic API・Amazon Bedrock・Google Cloud Vertex AIで提供開始された。7万5千行超のコードベースや数十本の論文を1リクエストで処理できるようになった。

## 設計のポイント

- コードベース全体をソース・テスト・ドキュメントごと読み込ませ、ファイル横断の依存関係を踏まえた提案を可能にする
- 契約書や論文など大量文書間の関係性を、コンテキストを維持したまま横断分析できるようにする
- 数百回のツール呼び出しにまたがっても一貫性を保つ長時間稼働エージェントの基盤として位置づける

## 使いどころ

- 大規模コードベース全体を対象にした横断的なコード分析・改善提案を行いたい開発チーム
- 法務契約書や研究論文など大量の文書セットを横断的に統合・分析したいワークロード
