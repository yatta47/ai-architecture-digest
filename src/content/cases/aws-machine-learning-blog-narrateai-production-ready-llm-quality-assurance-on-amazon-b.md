---
type: case
title: NarrateAIのリアルタイムLLM品質保証5手法
title_original: 'NarrateAI: production-ready LLM quality assurance on Amazon Bedrock'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- eval
- guardrails
- multi-model-routing
- parallel-execution
components:
- Amazon Bedrock
- Amazon Bedrock AgentCore
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/narrateai-production-ready-llm-quality-assurance-on-amazon-bedrock/
published_at: '2026-09-25'
---

## 概要

AWS社内の経営層向けBIアシスタントNarrateAIで、リアルタイム応答の数値精度を約99%に保つ5つの品質保証手法を解説する。適応的パイプライン、クロスアカウントのマルチモデルフェイルオーバー、ストリーミング評価、複合評価、数値検証で構成される。

## 設計のポイント

- 取得データ量で経路を分け、約90%を単一パスの高速経路、残りを並列バッチ処理に回す。
- 複数アカウント・モデルのクォータ空間にまたがってフェイルオーバーし、スロットリングを抑える。
- 段落生成と同時に評価し、数値は完全一致→意味検証の2段カスケードで幻覚を検出する。

## 使いどころ

- 数値の誤りが許されない経営向けLLMアシスタントの品質設計。
- 高同時接続でストリーミング応答の遅延を抑えたい場面。
