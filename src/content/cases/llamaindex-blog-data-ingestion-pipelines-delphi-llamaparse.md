---
type: case
title: Delphiがデジタルメンター『Digital Minds』の学習データ整備にLlamaParseを採用
title_original: 'Clean Inputs, Smarter Minds: How Delphi Uses LlamaParse to Power Better Data Ingestion Pipelines'
company: Delphi
industry: media
cloud:
- aws
patterns:
- document-processing
- rag
components:
- LlamaParse
- Amazon S3
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/clean-inputs-smarter-minds-how-delphi-uses-llamacloud-to-power-better-data-ingestion-pipelines
published_at: '2026-07-19'
---

## 概要

実在の人物のAI版「デジタルマインド」を提供するDelphiは、PDF・Excel・YouTube文字起こしなど多様な形式の乱雑なコンテンツを大量に取り込む必要があり、パース失敗による引用崩れやユーザー信頼低下に悩まされていた。複数の取り込みプロバイダを比較評価した上でLlamaParseを採用し、精度とコストのバランスを取るbalancedモードでS3データレイクとナレッジグラフに接続するパイプラインを構築している。

## 設計のポイント

- PDF・Excel・YouTube文字起こしなど多様な形式の乱雑なコンテンツを、複数の取り込みプロバイダを比較評価した上でLlamaParseに統一する
- コストと精度のバランスを取るbalanced agenticモードを採用し、OCR・VLM・LLMを組み合わせて処理する
- パース結果をMarkdown-firstで出力し、引用表示やLLMへの読み込みをそのまま行えるようにする
- パース済みコンテンツをS3データレイクに格納し、クラスタリングを経て各Digital Mindのナレッジグラフに統合する

## 使いどころ

- creatorごとに異なる形式・品質のコンテンツを大量に取り込みAIペルソナを学習させたいプラットフォーム
- パース精度の低さが引用表示の破綻やユーザー信頼の低下に直結するプロダクト
