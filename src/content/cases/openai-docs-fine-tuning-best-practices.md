---
type: guidance
title: OpenAIファインチューニングの品質改善ベストプラクティス
title_original: Fine-tuning best practices
industry: cross-industry
cloud: []
patterns:
- fine-tuning
components: []
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/fine-tuning-best-practices#page-top
published_at: '2025-07-21'
---

## 概要

ファインチューニングの結果が思わしくない場合に見直すべきポイントとして、訓練データの質(バランス・一貫性・アノテーター間の合意度)と量、エポック数・学習率・バッチサイズなどのハイパーパラメータ調整の指針をまとめる。OpenAIはファインチューニングプラットフォームの提供を終了しつつあり、新規ユーザーは利用できない。

## 設計のポイント

- データを半分にしてファインチューニングした場合との品質差を見ることでデータ追加の効果を見積もる
- 単一の理想的な完了がある分類・抽出タスクではエポック数を増やし、多様な良い回答があるタスクでは減らす
- 推論時と同じプロンプト・指示をすべての訓練例に含めることで、少数の訓練例でも汎化しやすくする
- weightキーで特定のassistantメッセージを学習対象から除外し、マルチターン会話の一部だけを学習させられる

## 使いどころ

- 分類・エンティティ抽出など明確な正解があるタスクのモデル特化
- 既存のファインチューニング済みモデルの精度が伸び悩んでいる場合の改善検討
