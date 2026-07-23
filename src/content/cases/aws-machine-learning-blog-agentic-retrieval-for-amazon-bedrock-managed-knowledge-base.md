---
type: guidance
title: Bedrock Knowledge Basesのエージェント型検索で多意図質問に対応する
title_original: Agentic retrieval for Amazon Bedrock Managed Knowledge Base
industry: cross-industry
cloud:
- aws
patterns:
- rag
- ai-agent
components:
- Amazon Bedrock Managed Knowledge Bases
- AgenticRetrieveStream API
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/agentic-retrieval-for-amazon-bedrock-managed-knowledge-base/
published_at: '2026-07-23'
---

## 概要

Amazon Bedrock Managed Knowledge Basesの新しいAgenticRetrieveStream APIは、単発のベクトル検索では対応できない複数意図・比較・探索型の質問に対して、基盤モデルが質問を分解し反復的に検索・十分性判定を行うプランニングループを提供する。トレースイベントで各ステップを可視化しつつ、既定で根拠付き回答を生成する。

## 設計のポイント

- 単一クエリベクトルでは複数意図をブレンドしてしまう問題に対し、質問を分解してサブクエリごとに検索する
- maxAgentIterationで反復回数の上限を制御し、単一KBは3回、複数KB/比較質問は4〜5回を目安にする
- 十分性判定をプランニングステップに組み込み、証拠が揃った時点で早期に停止できるようにする
- 最終結果イベントでのみ重複排除を行い、各ステップのトレースは個別に保持して検証可能にする

## 使いどころ

- 複数の時期・カテゴリを比較する分析クエリに答える必要があるナレッジベースQA
- 単発検索では網羅できないマルチパートな質問が多い社内ドキュメント検索
- 自前でRetrieve APIをループさせるカスタムエージェントを運用しているチームの置き換え先
