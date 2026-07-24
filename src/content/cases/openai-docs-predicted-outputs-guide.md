---
type: guidance
title: 変更差分が小さい再生成にPredicted Outputsでレイテンシを削減する
title_original: Predicted Outputs guide
industry: cross-industry
cloud: []
patterns:
- inference-optimization
components:
- Chat Completions API
- gpt-4.1
outcome:
  type: speed
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/predicted-outputs
published_at: '2025-07-18'
---

## 概要

Predicted Outputsは、コード修正など出力の大半が既知のテキストとほぼ同じになる再生成タスクにおいて、予測テキストをpredictionパラメータとして渡すことでChat Completions APIのレイテンシを削減する機能。採用/却下されたトークン数がusageに含まれ、却下分は通常の生成と同様に課金される。

## 設計のポイント

- ファイル全体を書き直すタスクでは、変更前のテキストをそのままpredictionとして渡すことで大部分の出力を先読みし、レイテンシを短縮する。
- acceptedとrejectedのprediction tokenをusageで区別し、rejected分もコストが発生する点を踏まえてコスト対効果を評価する。
- ストリーミングと組み合わせるとレイテンシ削減効果がさらに大きくなるため、対話的なコード編集UIとの相性が良い。

## 使いどころ

- AIによるコード自動修正・リファクタリング機能で応答速度を改善したい場合。
- 既存ドキュメントの一部だけを書き換える生成タスクでコストとレイテンシのバランスを取りたい場合。
