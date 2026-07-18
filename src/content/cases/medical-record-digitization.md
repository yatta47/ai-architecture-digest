---
type: case
title: 医療記録デジタル化のドキュメント処理パイプライン
title_original: "Automate medical record digitization with Amazon Bedrock Data Automation"
company: Regional Health Network
industry: healthcare
cloud: [aws]
patterns: [rag, document-processing, human-in-the-loop]
data_sources: [medical-records]
components: [Amazon Bedrock, Amazon Textract, S3]
outcome: { type: productivity }
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/
published_at: 2026-07-10
---

## 概要

紙の医療記録を Amazon Textract で OCR し、Amazon Bedrock で構造化・要約するパイプライン事例。抽出結果は人手確認を挟んでから EHR に取り込む。RAG で過去記録を参照しながら、転記作業の手間を大幅に削減した。

## 設計のポイント

OCR（Textract）と生成（Bedrock）を分離し、間に人手確認を挟む三段構え。非構造データはまず機械可読化してから LLM に渡すと精度が安定する。生成結果は EHR へ取り込む前に必ず検証ステップを通し、誤りをシステムに伝播させない。

## 使いどころ

帳票・スキャンなど非構造データを LLM で構造化したいとき。医療・保険など正確性が要る領域で、OCR + LLM + 人手確認のパイプラインを組む担当。
