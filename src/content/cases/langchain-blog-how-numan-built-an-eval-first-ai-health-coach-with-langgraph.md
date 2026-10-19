---
type: case
title: Numanの健康コーチ「Nu」を評価基準から作る評価優先の開発
title_original: How Numan built an eval-first AI health coach with LangGraph and LangSmith
company: Numan
industry: healthcare
cloud:
- multi-cloud
patterns:
- eval
- guardrails
- ai-agent
- llmops
components:
- LangGraph
- LangSmith
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-numan-built-an-eval-first-ai-health-coach-with-langgraph-and-langsmith
published_at: '2026-10-19'
---

## 概要

英国のデジタルヘルス企業Numanは、診断や処方に踏み込まないAIヘルスコーチNuをLangGraphで構築した。単発の固定フィクスチャや台本付きの複数ターン評価では会話の安全性を測れないと分かり、評価基準そのものの設計を中心に据えた。

## 設計のポイント

- 全データセットを平均した1つのスコアは、少数の悪い返答を隠すため使わない。
- 固定の期待出力による単発評価は、コーチングの会話的な進行を誤って失敗と判定することがある。
- 台本の患者発話は直前のNuの返答を無視し、想定外の返答が出た時点で会話が成立しなくなる。
- 規制領域の境界を守れているかを会話全体の文脈で評価する。

## 使いどころ

- 医療や金融など規制領域で、助言の境界を守る会話エージェントを作る場面。
- LLMジャッジの単発評価で品質を測りきれないチーム。
- 会話型エージェントの評価データセットを設計する場面。
