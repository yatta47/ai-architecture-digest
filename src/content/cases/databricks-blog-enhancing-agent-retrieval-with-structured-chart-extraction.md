---
type: case
title: チャートを構造化JSON化してエージェントのRAG精度を上げる
title_original: Enhancing Agent Retrieval with Structured Chart Extraction
company: Databricks
industry: financial-services
cloud: []
patterns:
- rag
- document-processing
- eval
components:
- ai_parse_document
- ai_prep_search
- ai_search
- Databricks Genie
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/enhancing-agent-retrieval-structured-chart-extraction
published_at: '2026-08-27'
---

## 概要

Databricksは、エンタープライズ文書中のチャート（図表）をエージェントが正しく読み取れないという課題に対し、ai_parse_documentでチャートを構造化JSONとして抽出し検索インデックスに埋め込むパイプラインを構築した。ViDoRe V3のチャート関連問題群と独自のChart-RAGベンチマークで、キャプションのみのベースラインに比べ検索精度・回答精度の双方を改善した。

## 設計のポイント

- チャートをキャプションのみで表現する従来手法に対し、ai_parse_documentで数値・軸・系列を含む構造化JSONとして抽出しチャンクへ埋め込む
- 300MパラメータのBGE系軽量テキスト埋め込みモデルでも、構造化JSONの併用で大規模マルチモーダル埋め込みモデルに匹敵する精度を達成
- 上位検索結果には元のチャート画像も併せて渡すことで、見た目そのものに依存する質問への回答精度をさらに改善
- LLM審判（gemini-3-flash）による正誤判定と、Hit Rate@10・nDCG@10による検索品質評価を分離して計測

## 使いどころ

- 財務レポートなど図表に重要情報が集中する文書に対するRAG精度を上げたいチーム
- キャプションのみのチャート要約では細かい数値質問に答えられず困っているエンタープライズ検索チーム
