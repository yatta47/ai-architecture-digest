---
type: guidance
title: LLMアプリのレイテンシを改善する7つの設計原則
title_original: Latency optimization
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- prompt-optimization
components: []
outcome:
  type: speed
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/latency-optimization
published_at: '2025-07-21'
---

## 概要

多数の顧客・開発者との協業から導き出された、LLM関連ユースケース全般に適用できるレイテンシ改善の7原則（トークン処理の高速化、生成トークン数の削減、入力トークン数の削減、リクエスト数の削減、並列化、ユーザー体感待ち時間の短縮、LLMに頼らない選択肢の検討）を整理したガイド。

## 設計のポイント

- 推論速度そのものだけでなく、生成・入力トークン量やリクエスト回数の削減など複数の切り口でレイテンシを捉える。
- 小さいモデルでも長めのプロンプトやfew-shot、fine-tuning/distillationを組み合わせれば大きいモデルに匹敵する精度を維持しつつ高速化できる。
- 並列化やPredicted outputsのような推論最適化機能を活用し、体感待ち時間を減らす工夫を組み合わせる。

## 使いどころ

- チャットボットなどエンドツーエンドの対話アプリでレイテンシがボトルネックになっている場合。
- 個別ワークフローの一部だけを高速化したい細粒度の最適化にも適用できる。
