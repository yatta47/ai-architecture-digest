---
type: announcement
title: LlamaParseによるRFP自動生成とマルチエージェント接客システムの週刊アップデート
title_original: LlamaIndex Newsletter 2024-10-29
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- multi-agent-orchestration
- document-processing
- human-in-the-loop
components:
- LlamaParse
- LlamaIndex.TS
- NVIDIA NIM
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-10-29
published_at: '2026-07-29'
---

## 概要

LlamaIndexの週刊ニュースレターでは、LlamaParseを使った非構造化データのインデックス化によるRFP回答生成のワークフロー、基本エージェントから人間介在(human-in-the-loop)を経てマルチエージェントのオーケストレーションへ発展させる接客システム構築ガイド、RAGから高度なナレッジアシスタントへの動画シリーズなどを紹介している。あわせてVercel AI SDKへのLlamaIndex.TS統合や、NVIDIA NIMを使ったAI営業アシスタントの事例、ハッカソン作品Gift Genieなどコミュニティの取り組みも取り上げている。

## 設計のポイント

- LlamaParseで非構造化文書をパース・インデックス化し、その上でRFP生成のような複雑なエージェントワークフローを構築する。
- 接客・カスタマーサービス系エージェントは、単一エージェント→ツール利用→重要操作への人間介在(human-in-the-loop)→複数エージェントのオーケストレーションという段階的な拡張パスで設計する。
- LlamaIndex.TSをVercel AI SDKのアダプタとして組み込み、LLM応答をフロントエンドへストリーミングしやすくする。

## 使いどころ

- 大量の非構造化文書からRFP回答など定型ドキュメントを自動生成したい企業。
- 重要な操作にだけ人間の承認を挟みつつ段階的に自動化したいカスタマーサービス構築チーム。
- 営業担当者にリアルタイムで正確な情報を提供するAIアシスタントを構築したい営業組織。
