---
type: guidance
title: 表・画像混在ドキュメント向けRAGを実現するマルチベクトルリトリーバー
title_original: Multi-Vector Retriever for RAG on tables, text, and images
company: LangChain
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- LangChain Multi-Vector Retriever
- Unstructured
- Chroma
- LLaVA
- GPT4-V
- Ollama
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/semi-structured-multi-modal-rag
published_at: '2026-08-25'
---

## 概要

LangChainは、テキスト・表・画像が混在する文書に対するRAGを実現するクックブック3本を公開した。検索に使う要約（サマリー埋め込み）と、LLMへの回答生成に渡す元コンテンツ（生の表や画像）を分離するマルチベクトルリトリーバーの考え方を、単純なテキストだけでなく表や画像にも適用し、マルチモーダルLLMと組み合わせた3種類のRAG構成、およびローカル完結可能な構成を示す。

## 設計のポイント

- 検索用の表現（要約）と生成用の表現（元の表・画像・全文）を分離し、検索精度と生成時の情報の完全性を両立させる
- Unstructuredのようなレイアウト認識パーサーでPDFを表/画像/テキスト要素に分解してから、それぞれを要約してベクトル化する
- マルチモーダル埋め込みを使う方式、画像要約をテキスト埋め込みする方式、画像要約＋元画像参照を併用する方式の3パターンから、利用可能なマルチモーダルLLMの有無に応じて選ぶ
- LLaVA・Chroma・Ollamaの組み合わせでパイプライン全体をコンシューマーPC上でローカル実行でき、プライバシー要件にも対応できる

## 使いどころ

- 表を含むPDFレポートに対して、ナイーブなチャンク分割では表が壊れてしまう問題を回避したいチーム
- グラフや図表を含む文書に対するマルチモーダルQAを構築したいチーム
- 外部APIに文書を送れない、フルローカルRAGが必要なプライバシー制約の強い組織
