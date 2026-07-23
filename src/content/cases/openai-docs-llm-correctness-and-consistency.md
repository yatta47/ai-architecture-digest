---
type: guidance
title: プロンプトエンジニアリング・RAG・Fine-tuningを使い分けるLLM精度最適化のメンタルモデル
title_original: Optimizing LLM Accuracy
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
- rag
- fine-tuning
components: []
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/optimizing-llm-accuracy
published_at: '2025-07-21'
---

## 概要

LLMの精度最適化を『プロンプトエンジニアリング→RAG→fine-tuning』という単純な一直線のフローとして捉えるのではなく、それぞれが異なる課題を解決するレバーであるとして、自社ユースケースにおける失敗コストと成功便益を踏まえてどこまでの精度が本番投入に『十分』かを判断するためのメンタルモデルを提示する。

## 設計のポイント

- 3つの最適化手法を順番に試すのではなく、それぞれが解決する課題（知識不足・記憶漏れ・文体逸脱など）を見極めて選ぶ。
- 精度の目標水準は一律ではなく、誤りが発生した際のコスト（人手修正か顧客への金銭的損害かなど）から逆算して設定する。

## 使いどころ

- 精度改善の打ち手を検討する際に、何から手をつけるべきか迷っているチーム。
- 『どこまでの精度で本番投入してよいか』の意思決定基準を明文化したい場合。
