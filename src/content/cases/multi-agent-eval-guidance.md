---
type: guidance
title: マルチエージェント評価のリファレンス設計
title_original: "Benchmarking multi-agent systems"
industry: cross-industry
cloud: [aws]
patterns: [multi-agent-orchestration, eval]
data_sources: []
components: [Amazon Bedrock, Amazon CloudWatch]
outcome: { type: quality }
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://blog.langchain.dev/
published_at: 2026-07-05
---

## 概要

複数エージェントを協調させる構成をどう評価するかを一般化したガイダンス。実行トレースを記録し、複数の評価器でスコアリングして仕様（rubric）に反映するループを推奨する。特定企業の事例ではなく、再利用できる評価ハーネスの型として提示されている。

## 設計のポイント

評価は単一スコアに頼らず、複数の評価器を束ねて多面的に見る。本番の実行トレースを記録し、そこから得た知見を仕様（rubric）へ戻すループを回すのが要。オフライン評価と本番観測を同じ rubric でつなぐことで、評価の再現性が保てる。

## 使いどころ

マルチエージェント / エージェントの評価（eval）設計に悩んでいるとき。オフライン評価と本番トレースをつなぐ仕組みを作りたい LLMOps 担当。
