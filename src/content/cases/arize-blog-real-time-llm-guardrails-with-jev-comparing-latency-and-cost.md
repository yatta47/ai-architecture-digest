---
type: case
title: エージェントの入力・応答・ツール呼び出しを守るJevとLLM判定のガードレール比較
title_original: 'Real-time LLM guardrails with Jev: comparing latency and cost'
company: Arize
industry: cross-industry
cloud: []
patterns:
- guardrails
- eval
- ai-agent
- llm-gateway
components:
- Jev
- TypeSafe System One
- GPT-5.4 nano
- Arize AX
outcome:
  type: risk-compliance
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/llm-guardrails-jev/
published_at: '2026-09-23'
---

## 概要

ディーラー向けチャットボットのデモで、専用の判定モデルJevと汎用LLMジャッジ(GPT-5.4 nano)を使ったガードレールのレイテンシとコストを比較した。入力メッセージ、返信案、ツール引数の3境界と、価格下限を見る決定的ルールを組み合わせた構成を示す。

## 設計のポイント

- 入力、返信、ツール引数の各境界に別々のガードレールを置き、モデル判定と決定的ルールを併用している。
- 1ドル販売のような不正な提案は、ツールが記録する前にブロックしている。
- 汎用LLMジャッジ、ファインチューニング小型モデル、専用判定モデルの選択をレイテンシとコスト予算で比べている。

## 使いどころ

- 顧客対応エージェントに契約や価格の誤約束を防ぐ仕組みが要るチーム。
- ガードレールのレイテンシとコスト予算を設計する担当者。
- ツール実行を伴うエージェントの安全確認を後付けしたい場面。
