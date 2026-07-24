---
type: guidance
title: Evals→プロンプト設計→ファインチューニングを回すモデル最適化フライホイール
title_original: Model optimization guide
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- fine-tuning
- prompt-optimization
components:
- Evals API
- Fine-tuning API
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/model-optimization
published_at: '2025-07-18'
---

## 概要

LLMの出力は非決定的でモデルスナップショットごとに挙動が変わるため、OpenAIは評価(Evals)・プロンプトエンジニアリング・ファインチューニングを1つのフィードバックループとして回すモデル最適化ワークフローを提示する。ベースラインとなるevalsを先に書き、プロンプト改善とファインチューニング用データの両方に反映させる。

## 設計のポイント

- プロンプトを書く前にevalsを先に定義し、BDD(振る舞い駆動開発)のように期待する出力を先に固定してから実装に着手する。
- 文脈情報の提供・明確な指示・Few-shot例の3点をプロンプト改善の基本セットとし、モデルごとに効くプロンプト手法が異なる前提で検証する。
- ファインチューニングは新規知識を教える手段ではなく、出力形式や振る舞いを最適化する手段と位置づけ、知識注入にはRAGを使う。

## 使いどころ

- 本番投入前にLLMアプリの品質を継続的に測定・改善する仕組みを整えたいチーム。
- 同じプロンプトでモデルを乗り換えた際の挙動差を定量的に追いたい場合。
