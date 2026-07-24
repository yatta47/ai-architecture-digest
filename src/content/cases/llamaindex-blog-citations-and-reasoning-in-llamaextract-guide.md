---
type: guidance
title: LlamaExtractの抽出結果に引用と推論根拠を付与し検証可能にする
title_original: Get Citations and Reasoning for Extracted Data in LlamaExtract
industry: cross-industry
cloud: []
patterns:
- document-processing
- guardrails
components:
- LlamaExtract
- LlamaParse
- LlamaCloud
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/get-citations-and-reasoning-for-extracted-data-in-llamaextract
published_at: '2025-01-26'
---

## 概要

LlamaExtractに、抽出した各フィールドについて根拠となる引用元（ページ・該当テキスト）と推論理由を付与するオプション機能が追加された。SEC提出書類（NVIDIAの10-K）からのデータ抽出を例に、Pydanticスキーマ定義とExtractConfig（use_reasoning・cite_sources）で構造化抽出の検証可能性を高める方法を紹介している。

## 設計のポイント

- Pydanticモデルでフィールドごとに説明文を付与し、抽出対象と意図をLLMに明示的に伝える
- ExtractConfigのuse_reasoning/cite_sourcesを有効化し、抽出フィールドごとに引用箇所と推論理由を付与する
- 推論理由に「VERBATIM EXTRACTION（原文抽出）」「INSUFFICIENT DATA（データ不足）」といった定型ラベルを持たせ、直接引用と根拠不十分な項目を区別できるようにする

## 使いどころ

- SEC提出書類や財務報告書など、抽出結果の監査・検証が求められる金融・コンプライアンス業務
- 自動抽出結果の信頼性・追跡可能性が重要なドキュメント処理パイプライン
- 抽出したフィールドの根拠を提示して人間が検証できるエージェント型ワークフロー
