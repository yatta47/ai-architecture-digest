---
type: guidance
title: Arize AXのリモート評価にJevを組み込む手順
title_original: How to build a remote evaluator in Arize AX with Jev
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- inference-optimization
- cost-optimization
components:
- Arize AX
- Jev
- FastAPI
- OpenInference
- OpenAI
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/jev-remote-evaluator/
published_at: '2026-09-24'
---

## 概要

Arize AXのリモートエバリュエータとしてFastAPIサービスを立て、TypeSafeのJevで「応答がユーザーの要求を解決したか」をyes/no確率として採点する手順を示す。LLM評価の費用を抑え、確率の低い結果だけをLLMジャッジに回す運用を提案している。

## 設計のポイント

- Jevは文章を生成せず確率のみ返すため、閾値で振り分けて曖昧な結果だけLLMジャッジに送る。
- 評価基準は真偽それぞれの条件で明文化し、判断に必要な文脈を渡す。
- AX側はHTTPSエンドポイントの入出力契約(label/score)だけを満たせばよい。

## 使いどころ

- トレース数に応じて増えるLLM評価費用を抑えたいチーム。
- エージェント応答の解決可否を大量に自動採点したい場面。
