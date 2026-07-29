---
type: guidance
title: NVIDIA NIMとLlamaIndexで構築するクエリルーティングAIエージェント
title_original: NVIDIA NIM for Agents
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
- multi-agent-orchestration
components:
- NVIDIA NIM
- LlamaIndex
- Llama 3.1 8B
- NV-EmbedQA-E5-v5
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/using-nvidia-nim-for-agent-enhanced-ai-query-engines-with-llamaindex
published_at: '2026-07-25'
---

## 概要

NVIDIA NIMマイクロサービスとLlamaIndexを組み合わせ、複雑な質問をサブクエスチョンに分解して適切なドキュメント/ツールにルーティングするエージェント強化型クエリエンジンの構築方法を解説する。

## 設計のポイント

- 複雑なユーザークエリをサブクエスチョンに分解し、各サブクエリを適切なソースドキュメント用ツールにルーティングする
- 埋め込みモデルとLLMをそれぞれ独立したNIMマイクロサービスとしてホストし、LlamaIndexの設定に差し替え可能な形で組み込む
- サブクエスチョンへの回答をエージェントが統合し、単一のLLM呼び出しでは得られない一貫した最終回答を生成する

## 使いどころ

- 年度別・カテゴリ別に分かれた大量ドキュメントに対する複雑な質問応答が必要な社内チャットボット
- 商品レビューなど複数ソースを横断して根拠を探索させたいリテールチャットボット
