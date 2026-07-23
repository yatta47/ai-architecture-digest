---
type: guidance
title: 生成AIの非決定性に対応するためのeval設計のベストプラクティス
title_original: Evals design best practices
industry: cross-industry
cloud: []
patterns:
- eval
components:
- Evals API
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/evaluation-best-practices
published_at: '2025-07-21'
---

## 概要

LLMは同じ入力でも異なる出力を返す変動性を持つため、従来のソフトウェアテストだけでは不十分であり、evalsという構造化されたテストによって精度・性能・信頼性を継続的に検証する必要があるという設計ガイド。業界ベンチマーク、ROUGEやBERTScoreのような標準指標、自社ユースケース向けの独自evalという3種類のevalsを区別して説明する。

## 設計のポイント

- 汎用ベンチマークではなく自社アプリケーション固有のevalを設計することが実運用での性能改善に直結する。
- evalスコアは単体で見るのではなく、失敗コストと成功による便益という文脈に照らして『十分な精度』を判断する。

## 使いどころ

- モデルのアップグレードや変更前に性能劣化がないか継続的に検証したいチーム。
- fine-tuningなど改善施策の効果を定量的に測る仕組みを整えたい場合。
