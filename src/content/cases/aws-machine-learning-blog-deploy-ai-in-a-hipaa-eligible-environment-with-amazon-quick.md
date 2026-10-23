---
type: guidance
title: 'HIPAA対応環境でのAmazon Quick利用: PHIを扱うエージェントのガバナンス'
title_original: Deploy AI in a HIPAA-eligible environment with Amazon Quick
company: AWS
industry: healthcare
cloud:
- aws
patterns:
- guardrails
- defense-in-depth
- ai-agent
components:
- Amazon Quick
- MCP
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploy-ai-in-a-hipaa-eligible-environment-with-amazon-quick/
published_at: '2026-10-22'
---

## 概要

PHIを扱うエージェント型ワークスペースAmazon QuickをHIPAA対応環境で使う際の考え方を整理する。決定論的ガードレール、行動の監査証跡、ACLを考慮した検索、エージェントが実行できる操作の制御といったガバナンス機能を説明する。

## 設計のポイント

- エージェントが読み書きできる範囲を、権限と接続コネクタの許可で制限する。
- チャットとフィードバックのログで、エージェントの行動を事後に追える。
- ACLを考慮した検索で、構造化・非構造化データの双方で権限外データを返さない。

## 使いどころ

- 医療保険・医療機関でエージェントを導入するコンプライアンス担当。
- PHIを扱う業務にエージェントを広げるときの統制設計。
