---
type: case
title: エージェント型IDPで未知の帳票形式を自己学習する文書処理
title_original: Build self-improving document processing using Amazon Bedrock AgentCore
industry: cross-industry
cloud:
- aws
patterns:
- document-processing
- multi-agent-orchestration
- ai-agent
components:
- Amazon Bedrock AgentCore
- Strands Agents
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-self-improving-document-processing-using-amazon-bedrock-agentcore/
published_at: '2026-10-14'
---

## 概要

請求書や注文書などレイアウトが取引先ごとに異なる文書を、8つの専門エージェントが2つのグラフワークフローで分類・抽出・検証・学習する構成を示す。新形式でも手動テンプレート設定が不要で、学習した内容を再利用して以降は再学習なしで抽出に進める。

## 設計のポイント

- 静的テンプレートではなく、エージェントが文書ごとに抽出指示を生成して検証し、結果をナレッジとして蓄積する
- 専門エージェントをグラフワークフローで編排し、分類・抽出・検証・学習を分離する
- 人手修正を学習として取り込み、同種文書の繰り返しエラーを減らす

## 使いどころ

- 多数の取引先から請求書を受け取る経理部門
- 保険金請求やローン申込など様式が多様な文書の処理基盤
