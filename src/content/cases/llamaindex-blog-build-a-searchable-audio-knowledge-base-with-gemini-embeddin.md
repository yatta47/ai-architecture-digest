---
type: case
title: LlamaParseの音声書き起こしとGemini Embedding 2でつくる検索可能な音声メモ基盤『audio-kb』
title_original: Build a Searchable Audio Knowledge Base with Gemini Embedding 2 and LlamaParse
company: LlamaIndex
industry: cross-industry
cloud:
- gcp
patterns:
- rag
- document-processing
- realtime-transcription
components:
- LlamaParse
- Gemini Embedding 2
- SurrealDB
- LlamaAgent Workflows
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/build-a-searchable-audio-knowledge-base-with-gemini-embedding-2-and-llamaparse
published_at: '2026-07-19'
---

## 概要

LlamaIndexは音声メモをCLIから録音・アップロードし、LlamaParseで書き起こし、Gemini Embedding 2で埋め込んでSurrealDBのHNSWインデックスに保存し、意味検索できるCLIツール『audio-kb』を作成した。取り込みと検索の両方をLlamaAgent Workflowsでオーケストレーションしている。

## 設計のポイント

- 専用の音声認識モデルを自前で持たず、LlamaParseのagenticティアに書き起こしを委任することで非構造的な発話でも高品質な結果を得ている
- チャンク化と埋め込み処理をセマフォで並列数を制御しつつ非同期に実行し、APIレート制限内で高速化している
- 検索時のクエリ埋め込みには専用のクエリ埋め込みメソッドを使い分け、インデックス時と検索時で同一モデル・異なるエンコード経路を使う

## 使いどころ

- 会議メモや音声アイデアをテキスト化せず即座に検索したい個人・チームのナレッジ管理
- 音声を含むマルチモーダルなエンタープライズ検索基盤を素早く試作したい開発者
