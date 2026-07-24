---
type: guidance
title: 蒸留とファインチューニングでコスト・レイテンシを下げるモデル最適化トラック
title_original: Model optimization
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- eval
- distillation
components:
- Evals API
- Distillation
outcome:
  type: cost
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/tracks/model-optimization/
published_at: '2025-07-11'
---

## 概要

OpenAIのモデル最適化ラーニングトラックは、精度・速度・コストの最適化レバーとしてファインチューニング(SFT/DPO/RFT/Vision FT)・蒸留・evalsの3つを整理する。蒸留は高性能モデルの挙動を小型モデルに転写し、同等の体験をより低コスト・低レイテンシで提供する手段として位置づけられる。

## 設計のポイント

- 精度改善が目的ならファインチューニング、応答速度とコストの改善が目的なら蒸留、という目的別にレバーを使い分ける。
- 蒸留はEvaluationsプロダクトと連動する組み込み機能として提供し、蒸留後の品質劣化をevalsで継続的に監視できるようにする。
- 入出力データの収集(Responses APIのデフォルト保存)→eval作成→プロンプト/RAG調整→蒸留、という最適化フローの順序を明示する。

## 使いどころ

- 大型モデルで実証済みの挙動を、コスト重視の小型モデルに移植したい場合。
- モデル選定後に精度・速度・コストのどれを次に最適化すべきか優先順位をつけたい場合。
