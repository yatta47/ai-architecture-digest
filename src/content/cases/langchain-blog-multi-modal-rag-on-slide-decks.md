---
type: guidance
title: スライド資料に対するマルチモーダルRAGの設計比較と精度検証
title_original: Multi-modal RAG on slide decks
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- GPT-4V
- Chroma
- OpenCLIP
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/multi-modal-rag-template
published_at: '2026-08-25'
---

## 概要

スライド資料へのRAGを、(1)スライド画像をマルチモーダル埋め込みで直接検索する方式と、(2)GPT-4Vで生成した画像要約をテキスト埋め込みで検索するマルチベクトル方式の2通りで実装し、Datadogの決算資料を題材にした公開ベンチマークで比較した。テキスト抽出のみのRAG（正答率20%）に対し、マルチモーダル埋め込み（60%）、画像要約によるマルチベクトル検索（90%）が大きく上回った。

## 設計のポイント

- スライドをテキスト抽出せず画像のまま保持し、検索と回答生成の両方で視覚情報を活用する
- 画像要約をテキスト埋め込みで検索するマルチベクトル方式は精度が高い一方、要約の事前生成コストと複雑性が増えるトレードオフがある
- LangSmithで手法ごとの評価トレースを並べて比較し、定量スコアと個別トレースの両面から設計判断を行う

## 使いどころ

- 投資家向け決算資料や社内プレゼン資料などグラフ・表を含む文書へのQ&Aを提供したい場合
- テキスト抽出だけでは精度が出ない視覚的に複雑な資料を扱うRAGアプリを立ち上げたいチーム
