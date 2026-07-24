---
type: guidance
title: HealthBenchを用いた対話型推論モデルの強化学習ファインチューニング
title_original: Reinforcement Fine-Tuning for Conversational Reasoning with the OpenAI API
industry: healthcare
cloud: []
patterns:
- reinforcement-learning
- fine-tuning
- eval
components:
- GPT-4.1
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/fine-tuned_qa/reinforcement_finetuning_healthbench/
published_at: '2025-05-21'
---

## 概要

医療QAベンチマークHealthBenchの一部を題材に、追加のコンテキストを尋ねて不確実性を減らす対話推論能力をOpenAIのRFTで改善する手順を示す。医師作成のルーブリックに基づくグレーダーで応答を採点し、その報酬信号でモデルを微調整する。

## 設計のポイント

- 医師が作成した重み付きルーブリックをグレーダーとして使い、モデルベースの採点で報酬信号を生成する
- ベースモデルのベンチマーク結果を先に取得し、改善余地の大きい難しいルーブリックに絞って学習データを設計する

## 使いどころ

- 曖昧な状況で追加情報を能動的に尋ねる対話能力を強化したい医療・カスタマーサポート向けAI
- ラベル付きデータが少量でも特定の推論スキルをピンポイントで改善したいケース
