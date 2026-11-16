---
type: case
title: 製薬の製造文書を扱う、Neptune+OpenSearchのGraphRAGエージェント
title_original: Novo Nordisk modernizes manufacturing process documents with Amazon Bedrock AgentCore
company: Novo Nordisk
industry: healthcare
cloud:
- aws
patterns:
- rag
- ai-agent
- document-processing
- human-in-the-loop
components:
- Amazon Bedrock AgentCore
- Amazon Neptune
- Amazon OpenSearch Serverless
- Strands Agents SDK
- Anthropic Claude
- Amazon Bedrock Data Automation
- AWS Step Functions
- AWS Lambda
- AWS CDK
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/novo-nordisk-modernizes-manufacturing-process-documents-with-amazon-bedrock-agentcore/
published_at: '2026-11-16'
---

## 概要

Novo Nordiskは、規制下の製造管理文書を対象に、知識グラフとハイブリッド検索を組み合わせたGraphRAGエージェントを構築した。曖昧な質問は検索前に確認し、承認済み文書に根拠づけた引用付き回答を返す。SMEの作業が数時間〜数日から数分になったとする。

## 設計のポイント

- グラフ(Neptune)と検索(OpenSearch)を分離し、文書番号でクエリ時に橋渡しする
- 文書の版・ライフサイクル状態・適用範囲(拠点/製品/設備)をグラフの構造として扱う
- ガイドモードでスコープが曖昧なら検索前にグラフに基づく確認質問を行う
- 該当情報が無いときはその旨を明示し、承認済み出典への引用を必須にする

## 使いどころ

- 規制産業でバージョンと適用範囲が重要な文書QA
- 複数ホップの参照関係や変更影響を調べたい文書管理
