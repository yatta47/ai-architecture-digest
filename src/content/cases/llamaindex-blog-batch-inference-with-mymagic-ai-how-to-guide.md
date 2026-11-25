---
type: guidance
title: MyMagic AIのバッチ推論とLlamaIndexで大量文書を非同期処理する
title_original: Batch inference with MyMagic AI and LlamaIndex
company: MyMagic AI
industry: cross-industry
cloud:
- aws
- gcp
patterns:
- inference-optimization
- rag
- cost-optimization
components:
- MyMagic AI
- LlamaIndex
- Amazon S3
- Google Cloud Storage
- Llama 3
- Mixtral
- Ollama
- BGE
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/batch-inference-with-mymagic-ai-and-llamaindex
published_at: '2024-05-22'
---

## 概要

S3/GCS上の大量ファイルを1回のAPI呼び出しで処理するバッチ推論をLlamaIndexから使う方法の紹介。出力はRAGパイプラインに取り込んで検索できる。

## 設計のポイント

- 即時性が不要な抽出・分類・要約・埋め込みはバッチ推論に寄せ、非同期APIで扱う。
- セッション用フォルダで対象ファイルを分離する。
- バッチの出力を後段のRAG索引に投入し、オフライン処理と対話検索を分ける。

## 使いどころ

- 数百万件規模の文書やレビューをまとめて処理したいチーム。
- 学習データ生成を低コストで行いたい開発者。
