---
type: opinion
title: AIハーネスにおけるモデル中立性はクラウド中立性以上に重要という論考
title_original: Why Model Neutrality Matters More Than Cloud Neutrality
company: LangChain
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- llm-gateway
- ai-agent
components:
- Claude Agent SDK
- OpenAI Agents API
- Vertex AI Agent Builder
- LangChain Deep Agents
- Terraform
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/model-neutrality
published_at: '2026-06-05'
---

## 概要

LangChainのブログ記事は、クラウド時代に起きたベンダーロックインの教訓が、次はモデル層でも繰り返されようとしていると論じる。Claude Agent SDKやOpenAI Agents API、Vertex AI Agent Builderのように各AIラボがハーネス(オーケストレーション層)を囲い込もうとしており、トークン自体はコモディティ化が進んでいるためロックインの主戦場がハーネス層に移っていると指摘する。解決策として、オープンソースでマルチモデル対応、モデルごとの特性を活かしつつ乗り換えの自由を保証する「中立なハーネス」の必要性を主張している。

## 設計のポイント

- 各AIラボが提供するエージェントSDK(Claude Agent SDK等)は自社モデルを前提にした設計であり、競合モデルを同等に扱うインセンティブがないと指摘し、ハーネス選定時にベンダー中立性を評価基準に加えるべきとする。
- 1回のエージェント実行の中でもコーディングはClaude、画像生成はGPTのようにタスクごとに最適なモデルへ動的にルーティングし、レート制限時のフェイルオーバーやコスト最適化のためのダウングレードも同一ハーネス内で行う設計を提案している。
- 中立なハーネスの条件として、オープンソースであること、主要モデルをすべて第一級でサポートすること、モデルごとの得意分野やプロンプト作法の違いを「プロファイル」として扱い画一化しないことを挙げている。

## 使いどころ

- 特定ラボのエージェントSDKに業務ロジックを深く組み込む前に、将来のモデル乗り換えコストを見積もりたいアーキテクト。
- コーディングはClaude、マルチモーダル処理はGPTのように、タスクごとに最適なモデルを使い分けたいプロダクションエージェントの開発チーム。
- オープンウェイトモデル(Mistral、DeepSeek、Qwen等)の自社ホスティングも選択肢に含めて、クローズドモデルと組み合わせたい企業。
