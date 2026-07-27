---
type: case
title: Booking.comが従来型MLと生成AIエージェントを一元的に観測する基盤
title_original: 'From traditional ML to AI agents: How Booking.com scales AI observability with Arize'
company: Booking.com
industry: other
cloud: []
patterns:
- llmops
- ai-agent
- eval
- root-cause-analysis
components:
- Arize
- Arize AX
- OpenTelemetry
- OpenInference
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/booking-com-ai-observability/
published_at: '2026-07-27'
---

## 概要

Booking.comは旅行プランニングアシスタントやパートナーコパイロット、ランキング、不正検知など多様なAI/MLシステムを、Arizeを基盤とした単一の観測プラットフォームで運用している。OpenTelemetryとOpenInference準拠のトレーシングでエージェントのプロンプト・検索・ツール呼び出しの全経路を可視化し、従来型MLにはドリフト検知・コホート分析・特徴量重要度を適用することで、品質劣化の早期検知と原因特定を高速化している。

## 設計のポイント

- OpenTelemetryを土台にOpenInferenceでLLM呼び出し・検索・ツール利用・ガードレールを共通の粒度でトレース化する
- トレース属性だけでなく評価結果やカスタムメトリクスにもアラートとダッシュボードを設定し品質指標と運用指標を同じ画面で監視する
- 本番トラフィックから直接データセットを作成し実データに基づく実験・改善サイクルを回す
- 従来型MLにはドリフト検知・コホート分析・特徴量重要度分析を適用しセグメント別の性能劣化を検出する

## 使いどころ

- リアルタイム/バッチ、自動化/人手介在など制約の異なる多数のAIシステムを抱える組織が観測基盤を統一したい場合
- 「何かおかしい」という違和感から具体的な原因特定と修正までを短時間で行いたいチーム
- エージェントのプロンプトから最終応答までのチェーン全体を追跡してデバッグしたい開発者
