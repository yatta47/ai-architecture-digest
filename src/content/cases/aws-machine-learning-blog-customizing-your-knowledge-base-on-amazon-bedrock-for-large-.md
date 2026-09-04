---
type: case
title: AmazonTextract前処理で精度を上げる請求書RAG
title_original: Customizing your knowledge base on Amazon Bedrock for large and complex documents using Amazon Textract
industry: cross-industry
cloud:
- aws
patterns:
- rag
- document-processing
components:
- Amazon Bedrock
- Amazon Textract
- Amazon OpenSearch Serverless
- AWS Lambda
- Amazon S3
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/customizing-your-knowledge-base-on-amazon-bedrock-for-large-and-complex-documents-using-amazon-textract/
published_at: '2026-09-04'
---

## 概要

大量の公共料金請求書(PDF/DOCX/画像など複数フォーマット)を素のままRAGに投入すると情報欠落やハルシネーションが発生した課題に対し、Amazon TextractでOCR抽出・クレンジング・タグ付けを行ってからAmazon Bedrockのナレッジベースに取り込むことで、正確な顧客対応を可能にした事例。

## 設計のポイント

- 生の請求書PDFを直接RAGに入れず、Amazon Textractで事前に構造化テキストへ変換してから取り込むことで抽出漏れとハルシネーションを抑える
- S3へのアップロードをトリガーにLambdaでTextractジョブを起動し、処理済みデータを別フォルダへ保存する非同期パイプラインを構成する
- 抽出後のデータをクレンジング・エンリッチしてノイズを除去し、関連情報のみをナレッジベースに投入する

## 使いどころ

- 複数フォーマットの複雑な請求書や契約書を扱うカスタマーサポートチームがRAGの回答精度を上げたい場合
- 表や画像を含む多ページドキュメントからLLMが情報を取りこぼす・幻覚を起こす問題を解消したい場合
