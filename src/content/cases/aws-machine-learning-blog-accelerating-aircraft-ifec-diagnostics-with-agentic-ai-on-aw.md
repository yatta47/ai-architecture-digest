---
type: case
title: Panasonic Avionics、機内エンターテインメント設備の診断をエージェント型AIで高速化
title_original: Accelerating aircraft IFEC diagnostics with agentic AI on AWS
company: Panasonic Avionics Corporation
industry: other
cloud:
- aws
patterns:
- ai-agent
- root-cause-analysis
- document-processing
components:
- Amazon Bedrock
- Amazon SageMaker
- AWS Glue
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/accelerating-aircraft-ifec-diagnostics-with-agentic-ai-on-aws/
published_at: '2026-08-21'
---

## 概要

数千種の機材構成を持つ大規模な機内エンターテインメント/接続(IFEC)フリートで、ログ・メトリクス・チケットデータの相関分析に人手で数時間かかっていた根本原因診断を、AWS Generative AI Innovation Centerの支援でエージェント型AIシステム化し、高精度を保ちながら診断時間を大幅短縮した。

## 設計のポイント

- 既存のAWS基盤のデータレイクの上に、Bedrock・SageMaker・Glueを組み合わせたエージェント型診断層を追加する構成を採る
- 機材ごとに異なるログパターンを吸収するため、フリート全体の構成差異を前提としたデータ処理を設計する
- 属人化していた診断ノウハウをエージェントに委譲し、根本原因特定までのリードタイムを短縮する

## 使いどころ

- 多数の機材構成・拠点を抱え、障害診断が属人化しているフリート運用組織
- ログ・メトリクス・チケットなど異種データソースを横断した根本原因分析を高速化したい保守運用チーム
- 既存データレイク資産を活かしたままエージェント型AIを段階的に導入したい場合
