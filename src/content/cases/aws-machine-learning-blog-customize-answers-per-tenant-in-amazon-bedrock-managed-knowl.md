---
type: guidance
title: Bedrock Managed Knowledge Baseでテナントごとに回答を変えるretrieval instructions
title_original: Customize answers per tenant in Amazon Bedrock Managed Knowledge Base
industry: cross-industry
cloud:
- aws
patterns:
- multi-tenant-rag
- context-engineering
components:
- Amazon Bedrock Managed Knowledge Base
- AgenticRetrieveStream
- Amazon S3
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/customize-answers-per-tenant-in-amazon-bedrock-managed-knowledge-base/
published_at: '2026-11-16'
---

## 概要

retrieval instructionsで口調・形式・検索指針・回答ポリシーを、版管理されたリソースとしてテナントごとに指定できる。共有ナレッジベースでも、メタデータフィルタと組み合わせてテナント別の回答とデータ分離を両立する。

## 設計のポイント

- persona/answerFormat/retrievalGuidance/answerPolicyの4項目で回答を制御する
- 指示は版を固定して変更を段階的にロールアウトする
- 指示は認可境界ではないため、取得範囲はメタデータフィルタや別KBで制御する
- 適用された指示をトレースで確認できる

## 使いどころ

- 多リージョン・多言語の顧客サポート
- SaaSで顧客別の口調とルールを分けたい場面
