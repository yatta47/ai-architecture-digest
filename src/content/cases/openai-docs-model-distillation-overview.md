---
type: guidance
title: 教師モデルの出力を使った小型モデルへの蒸留とfine-tuningデータセット設計
title_original: Model distillation
industry: cross-industry
cloud: []
patterns:
- fine-tuning
components:
- gpt-4.1
- gpt-4.1-mini
- gpt-4.1-nano
outcome:
  type: cost
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/distillation#page-top
published_at: '2025-07-21'
---

## 概要

大型モデルの出力を教師データとして小型モデルをsupervised fine-tuningする蒸留のワークフローを解説する。最小10件、実用上は50〜100件程度の高品質なデモンストレーション例から始め、JSONL形式のchat completions形式でデータセットを整備し、fine-tuning前にまずevalsを整備しておくことを推奨する。

## 設計のポイント

- 50件程度の質の高い例から始め、効果があれば件数を増やす、無ければタスクやプロンプト自体を見直すという段階的な進め方を取る。
- 学習データはできるだけ本番で想定される入出力に近い、具体的で明確な例にする。
- fine-tuningの効果を判断するため、着手前に評価（evals）の仕組みを先に用意しておく。

## 使いどころ

- 大型モデルの精度を保ちながら推論コストの低い小型モデルに置き換えたい場合。
- 関数呼び出しなど特定タスクに特化した挙動を安定させたい場合。
