---
type: announcement
title: LlamaIndexとKaggle、AIエージェント向け文書OCRベンチマーク「ParseBench」を公開
title_original: LlamaIndex and Kaggle launch a new document OCR leaderboard for AI agents
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
components:
- Kaggle
- LlamaParse
- HuggingFace
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-and-kaggle-launch-a-new-document-ocr-leaderboard-for-ai-agents
published_at: '2026-07-18'
---

## 概要

LlamaIndexはKaggleと提携し、保険・金融・契約書などエンタープライズ文書を対象にした文書OCR/パース評価ベンチマーク「ParseBench」のリーダーボードを公開した。表・チャート・忠実性・書式・視覚的グラウンディングの5軸で約2,000ページ・16万7000超のテストルールを用い、VLMや専用パーサー、LlamaParseなど14手法を評価する。

## 設計のポイント

- テキスト類似度ではなく、表構造・チャート数値・視覚的グラウンディング(座標特定)など下流のエージェントが実際に依存する5軸で採点する
- 既存ベンチマーク(OmniDocBenchなど)はエンタープライズ文書の割合が低いため、保険金請求・財務諸表・規制提出書類など実運用に近いデータで評価する
- KaggleのSDKを使い再現可能・検証可能な形でリーダーボードを構築し、モデル提供者やコミュニティが共同で改善できるようにする

## 使いどころ

- 文書パーサーやVLMを業務エージェントに組み込む前に、表構造や数値の正確性を客観比較したいチーム
- 保険・金融・法務など高リスク文書を扱うため、OCR精度の監査可能性(グラウンディング)が必要な組織
