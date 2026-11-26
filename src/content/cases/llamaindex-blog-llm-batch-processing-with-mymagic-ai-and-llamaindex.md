---
type: guidance
title: S3上の大量ファイルをOSS LLMでバッチ推論する連携
title_original: LLM Batch Processing with MyMagic AI and LlamaIndex
company: MyMagic AI
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- document-processing
- cost-optimization
components:
- MyMagic AI
- LlamaIndex
- Amazon S3
- Mixtral 8x7B
- Llama
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llm-batch-processing-with-mymagic-ai-and-llamaindex
published_at: '2024-03-05'
---

## 概要

S3バケット内の大量ファイルに対し、MyMagic AIのバッチ推論APIをLlamaIndex経由で呼び出して抽出・分類・要約・埋め込みを行うゲスト記事。非同期呼び出しを前提とし、対話型のchatには未対応。

## 設計のポイント

- ファイルをセッション単位のS3フォルダに分離し、1リクエストで一括処理させる。
- 推論サービスにはIAMロールでバケットへのアクセスを委譲する。
- バッチは長時間になるため非同期エンドポイントを基本にする。

## 使いどころ

- 数百万ファイルからの情報抽出やレビュー分類を行うチーム。
- 合成学習データや埋め込みをまとめて生成したい場面。
