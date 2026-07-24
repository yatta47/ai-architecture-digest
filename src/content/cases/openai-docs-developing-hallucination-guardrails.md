---
type: guidance
title: ハルシネーション検知ガードレールの構築
title_original: Developing Hallucination Guardrails
industry: cross-industry
cloud: []
patterns:
- guardrails
- eval
components:
- GPT-4o
- OpenAI API
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/developing_hallucination_guardrails/
published_at: '2024-05-29'
---

## 概要

LLM出力のハルシネーションを検知する出力ガードレールを構築する手順を解説するレシピ。カスタマーサポートエージェントを題材に、評価用データセットの構築、ハルシネーション判定基準の定義、few-shotプロンプトによるガードレール精度の改善までを扱う。

## 設計のポイント

- GPT-4oでポリシーや想定応答を合成データとして生成し、強力な評価データセットを構築する
- 精度・再現率などの指標でガードレールの性能を定量評価し、few-shot例で継続的に改善する

## 使いどころ

- ポリシー逸脱や事実誤認を検知したいカスタマーサポート自動応答システム
- LLMの出力を本番投入前に品質保証したいAIアプリケーション開発チーム
