---
type: guidance
title: GPT-5.6ファミリー(Sol/Terra/Luna)のモデル選定ガイド
title_original: Models
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
components:
- GPT-5.6 Sol
- GPT-5.6 Terra
- GPT-5.6 Luna
outcome:
  type: cost
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/models
published_at: '2025-08-03'
---

## 概要

複雑な推論・コーディング向けの最上位モデルGPT-5.6 Sol、知能とコストのバランス型Terra、大量処理向け低コストのLunaという3階層のモデルラインナップと、それぞれの価格・コンテキスト長・対応ツールを整理したモデル選定ページ。

## 設計のポイント

- 複雑さ・レイテンシ許容度・コスト制約に応じてSol/Terra/Lunaを使い分けるという単純な意思決定フレームを提示する
- 全モデルで推論強度(none〜max)を調整可能にし、同一モデル内でもコスト・品質のトレードオフを細かく制御できるようにする

## 使いどころ

- タスクの複雑度に応じてモデルコストを最適化したいプラットフォームチーム
- 新規にOpenAI APIを導入する際にどのモデルから始めるべきか判断したい開発者
