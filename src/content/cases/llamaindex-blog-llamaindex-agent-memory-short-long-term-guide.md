---
type: guidance
title: 短期・長期メモリブロックで作るLlamaIndexエージェントの記憶設計
title_original: Improved Long and Short Term Memory for LlamaIndex Agents
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- memory-consolidation
- ai-agent
components:
- LlamaIndex Memory
- StaticMemoryBlock
- FactExtractionMemoryBlock
- VectorMemoryBlock
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/improved-long-and-short-term-memory-for-llamaindex-agents
published_at: '2026-07-19'
---

## 概要

会話履歴をトークン上限内でSQLに保持する基本メモリに加え、静的情報・LLMによる事実抽出・ベクトル検索という3種の長期記憶ブロックを組み合わせられる新しいMemoryコンポーネントを紹介。短期記憶が上限に達すると自動的に長期記憶ブロックへ書き出す仕組みにより、長期にわたるユーザー文脈の保持を実現する。

## 設計のポイント

- 静的情報・抽出済み事実・ベクトル検索という性質の異なる3種の長期記憶ブロックを併用し、用途に応じて使い分ける
- 短期記憶のトークン上限到達をトリガーに長期記憶への書き出しを自動化し、開発者がフラッシュ処理を意識しなくてよい設計にする
- 全てのエージェントに記憶機構が必要なわけではないと明言し、会話履歴や永続的ユーザー情報が本質的に必要なユースケースに限定して導入する

## 使いどころ

- ユーザーの過去のやり取りや個人情報を踏まえて応答する必要があるチャットエージェント
- 長時間・複数セッションにまたがる会話文脈を保持したいカスタマーサポートボット
