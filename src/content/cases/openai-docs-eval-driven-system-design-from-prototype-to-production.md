---
type: guidance
title: 評価駆動でプロトタイプから本番へ育てるレシート処理AIシステム設計
title_original: Eval Driven System Design - From Prototype to Production
industry: financial-services
cloud: []
patterns:
- eval
- document-processing
- human-in-the-loop
components: []
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/partners/eval_driven_system_design/receipt_inspection/
published_at: '2025-06-02'
---

## 概要

少数のラベル付きデータしかない状態から始めて、evalsを中心的なプロセスに据えてレシート処理の自動化システムをプロトタイプから本番品質へ育てる手順を解説するOpenAIのクックブック。ビジネスKPIとの整合を取りながら段階的にeval範囲を広げ、低信頼度の判定は人間のQAへエスカレーションする設計を示す。

## 設計のポイント

- evalsをプロジェクトの中核プロセスに据え、印象的な精度評価ではなく計測に基づいた投資判断を可能にする
- 最小構成のV0システムをまず作り、ラベル付けとeval構築を反復しながら段階的に拡張する
- 低信頼度の判定は自動処理せず人間のQAへエスカレーションし、コストと精度のバランスを取る

## 使いどころ

- ラベル付きデータが乏しい状態から自動化システムを立ち上げたいML/AIエンジニア
- 人手中心の業務プロセス（経費精算など）をLLMで置き換えたいソリューションアーキテクト
