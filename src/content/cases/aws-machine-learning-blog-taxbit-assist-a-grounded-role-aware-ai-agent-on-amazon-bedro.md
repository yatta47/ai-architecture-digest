---
type: case
title: 権限と出典を意識する社内向けAIアシスタントの構築
title_original: 'Taxbit Assist: A grounded, role-aware AI agent on Amazon Bedrock AgentCore'
company: Taxbit
industry: financial-services
cloud:
- aws
patterns:
- rag
- ai-agent
- guardrails
- eval
components:
- Amazon Bedrock AgentCore
- AgentCore runtime
- AgentCore memory
- Strands Agents SDK
- Amazon Bedrock Guardrails
- Amazon Bedrock Knowledge Bases
- Amazon S3 Vectors
- Amazon CloudWatch
- AWS KMS
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/taxbit-assist-a-grounded-role-aware-ai-agent-on-amazon-bedrock-agentcore/
published_at: '2026-11-06'
---

## 概要

暗号資産の税務・会計プラットフォームTaxbitが、ダッシュボード内に出典付き・ロール認識型のAIアシスタントを組み込んだ事例。ガードレール、RAG、権限チェックを組み合わせ、リージョン別のデータ居住性と本番トラフィックでの品質計測も行う。

## 設計のポイント

- 利用者の身元(メール・組織・ロール)を信頼済み呼び出し元からクロージャでツールに束縛し、モデルに設定させない。
- ガードレールでPIIをマスクし、ブロック時はモデルを呼ばない。
- 地域プレフィックス付き推論プロファイルでEU/USの推論を地域内に留める。
- 固定のシステムプロンプトにキャッシュ点を置き、プロンプトキャッシュでコストと遅延を下げる。

## 使いどころ

- 規制業界で出典付きの回答とアクセス権の尊重が必須のサポート支援。
- 少人数チームでエージェント基盤の運用を管理型に任せたい場合。
- データ居住性やBYOK要件があるSaaS。
