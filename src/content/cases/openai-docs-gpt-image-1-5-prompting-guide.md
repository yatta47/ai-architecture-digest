---
type: guidance
title: GPT-image-1.5のプロンプト設計ガイド
title_original: Gpt-image-1.5 Prompting Guide
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
components:
- gpt-image-1.5
- OpenAI API
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/multimodal/image-gen-1.5-prompting_guide
published_at: '2025-12-16'
---

## 概要

OpenAIの新しい画像生成モデルgpt-image-1.5について、写実性・編集性・テキスト描画精度を高めるためのプロンプト設計パターンを解説するガイド。構図・具体性・制約の明示・複数画像参照・段階的な反復修正など、実運用のユースケースから得られたベストプラクティスをまとめている。インフォグラフィック生成や画像内テキストの多言語ローカライズなど具体的な適用例も示す。

## 設計のポイント

- プロンプトは背景/シーン→被写体→詳細→制約の順に構造化し、用途（広告・UIモック・インフォグラフィック等）を明示して仕上がりの水準を制御する
- レイテンシ重視の用途ではquality="low"から試し、要件を満たすか評価してから必要に応じて引き上げる
- 編集時は「変更する箇所」と「保持する箇所」を明示し、反復のたびに保持リストを繰り返してドリフトを防ぐ
- 画像内テキストは引用符やALL CAPSで明示し、フォントや配置などのタイポグラフィ詳細を制約として指定する

## 使いどころ

- 広告・UIモック・インフォグラフィックなど用途に応じた画像を安定生成したい開発者
- 既存デザインのレイアウトを保ったまま文言だけ他言語に差し替えたいローカライズ担当者
- 写実的な人物・情景を自然に見せたいクリエイティブ制作ワークフロー
