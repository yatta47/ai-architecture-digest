---
type: case
title: 自然言語からクラウド資産クエリを生成するOrcaのDiscovery AI
title_original: Natural language security queries at Orca Security using Amazon Bedrock
company: Orca Security
industry: cross-industry
cloud:
- aws
patterns:
- rag
- multi-model-routing
- text-to-sql
components:
- Amazon Bedrock
- AWS IAM
- AWS CloudTrail
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/natural-language-security-queries-at-orca-security-using-amazon-bedrock/
published_at: '2026-10-13'
---

## 概要

Orca SecurityはSonarクエリ言語への自然言語インターフェースDiscovery AIを、RAGとスキーマ認識型クエリ構築を組み合わせた9段階パイプラインとしてBedrock上に構築した。全スキーマを1プロンプトに入れる初期案からクエリコスト90%減・入力トークン93%減・レイテンシ75%減(60秒→15秒)を達成した。

## 設計のポイント

- 900超のモデル定義を全部プロンプトに載せず、RAGで必要なスキーマだけを取り出して入力トークンを削減している。
- 決定論的なQuick Matcherで構造化入力(IPやCVE等)を先に処理し、LLM呼び出しを減らしている。
- パイプラインの各段階に適したBedrockモデルを割り当て、コスト・速度・精度を段ごとに最適化している。
- モデル非依存の構成にし、新モデルへ再設計なしで差し替えられるようにしている。

## 使いどころ

- 独自クエリ言語やスキーマが巨大なSaaSに自然言語検索を付けたいチームに有効。
- 全文脈投入型PoCを本番のコスト/遅延要件に合わせて分解する場面の参考になる。
