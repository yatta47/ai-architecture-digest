---
type: case
title: StackAIがLlamaParseで実現するエンタープライズ文書エージェントの高精度検索基盤
title_original: StackAI Uses LlamaParse to Power High-Accuracy Retrieval for its Enterprise Document Agents
company: StackAI
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
- ai-agent
components:
- LlamaParse
- AWS Textract
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/stackai-uses-llamacloud-to-power-high-accuracy-retrieval-for-its-enterprise-document-agents
published_at: '2026-07-19'
---

## 概要

カスタムAIエージェント構築プラットフォームのStackAIは、ITチケット処理から財務分析まで多様な業務でスキャンされた保険書類や決算資料など乱雑な非構造化文書を扱う必要があり、従来の基本的なPDFリーダーやAWS Textractでは精度とスケールの両立が困難だった。LlamaParseを中核の文書取り込みステップとして統合し、数千文書規模でも高精度なパースとナレッジベース構築を実現している。

## 設計のポイント

- 基本的なPDFリーダーやAWS Textractでは精度・スケールの両立が難しかった課題を、LlamaParse APIをエージェント開発基盤の中核ステップとして統合することで解決する
- パース品質とコスト・速度のトレードオフを、パイロットから数千文書規模の本番運用までワークロードに応じて動的に調整できる設計にする
- パース結果を独自のパースロジックを書かずに自社ナレッジベースアーキテクチャへ直接接続し、開発のシンプルさを維持する

## 使いどころ

- スキャン品質の低い保険書類やデータルーム文書など、乱雑な非構造化文書を大量に扱うエンタープライズ向けAIエージェント
- 小規模PoCから数千文書規模の本番ワークロードまで弾力的にスケールさせたいプラットフォームチーム
