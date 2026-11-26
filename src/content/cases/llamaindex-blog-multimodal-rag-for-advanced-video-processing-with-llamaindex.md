---
type: guidance
title: GPT-4VとLanceDBで動画を検索するマルチモーダルRAG
title_original: Multimodal RAG for Advanced Video Processing with LlamaIndex & LanceDB
industry: cross-industry
cloud: []
patterns:
- rag
- video-intelligence
components:
- LlamaIndex
- GPT-4V
- LanceDB
- pytube
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/multimodal-rag-for-advanced-video-processing-with-llamaindex-lancedb-33be4804822e
published_at: '2024-02-17'
---

## 概要

動画をダウンロードして処理し、マルチモーダル索引とベクトルストアを作って、関連する画像と文脈を検索しGPT-4Vで回答させる手順を解説する。

## 設計のポイント

- 動画は映像フレームと音声由来のテキストに分解してから索引化する。
- 検索した画像とテキストを併せて視覚モデルに渡して推論させる。

## 使いどころ

- 講義や解説動画への質問応答を作る開発者。
- メディア・教育の動画資産を検索可能にしたいチーム。
