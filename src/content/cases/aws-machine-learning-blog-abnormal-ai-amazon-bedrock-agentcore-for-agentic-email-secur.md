---
type: case
title: 3段階検知パイプラインとコードインタプリタで数十億件/日のメール脅威をエージェントが判定
title_original: 'Abnormal AI: Amazon Bedrock AgentCore for agentic email security at scale'
company: Abnormal AI
industry: other
cloud:
- aws
patterns:
- ai-agent
- multi-model-routing
- guardrails
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock AgentCore Code Interpreter
- Amazon S3
- Amazon CloudWatch
- AWS CloudTrail
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/abnormal-ai-amazon-bedrock-agentcore-for-agentic-email-security-at-scale/
published_at: '2026-09-14'
---

## 概要

25%以上のFortune 500企業を守るセキュリティベンダーAbnormal AIが、Amazon Bedrock AgentCore Code Interpreterを使い、リアルタイムのメール脅威検知エージェントに「計算用スクラッチパッド」(サンドボックスでのコード実行環境)を組み込んだ事例。ヒューリスティクス(数十億件/日)→MLモデル(数百万件/日)→サンドボックス付きエージェント(数万件/日)の3段階検知パイプラインで、難しいケースのみエージェントがコードを書いて分析する。

## 設計のポイント

- LLMの意味推論だけでは計算・集計ができないため、Code Interpreterをスクラッチパッドとして併用しエージェントにデータ処理・検証能力を持たせる
- 検知を3段階(軽量分類→中間MLモデル→サンドボックス付きエージェント)にし、コストの高い深い分析は自信度の低いケースだけに絞る
- 外部ネットワークアクセスなしのサンドボックス(no egress)で再現性を確保し、プロンプトインジェクション等によるデータ持ち出しを防ぐゼロトラスト設計

## 使いどころ

- 大量トラフィックの中から少数の難しいケースだけに高コストな推論・分析を割り当てたい不正/脅威検知システム
- エージェントに数値計算やデータ可視化などLLM単体では苦手な処理をさせたいプロダクトチーム
