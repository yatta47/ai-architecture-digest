---
type: case
title: Couchbase Capella iQのAmazon Bedrockによるマルチモデル推論アーキテクチャ
title_original: How Couchbase built a multi-model AI architecture for Capella iQ with Amazon Bedrock
company: Couchbase
industry: cross-industry
cloud:
- aws
patterns:
- multi-model-routing
- llmops
- disaster-recovery
- text-to-sql
components:
- Amazon Bedrock
- Anthropic Claude
- Claude Sonnet 4.5
- Amazon EKS
- Amazon VPC
- Cross-Region Inference
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-couchbase-built-a-multi-model-ai-architecture-for-capella-iq-with-amazon-bedrock/
published_at: '2026-07-20'
---

## 概要

データベース開発者アシスタントCapella iQは、クエリ生成やインデックス推奨、複数ターンの対話を単一のLLMだけで支える限界に直面し、モデルに依存しない推論アーキテクチャを必要としていた。CouchbaseはAmazon Bedrockを採用し、us-east-1とus-west-2の2リージョンにまたがるEKS上のマイクロサービスからVPCインターフェースエンドポイント経由でBedrockを呼び出し、Cross-Region Inferenceで需要急増やリージョン障害時も自動フェイルオーバーする構成を構築した。モデル選定は標準ベンチマークで評価し、Claude Sonnet 4.5を本番モデルとして採用した。

## 設計のポイント

- モデルベンダーやテナント別設定をネームスペース層の設定値として分離し、モデル切替をコード変更なしの設定変更だけで行えるようにする
- VPCインターフェースエンドポイント経由でBedrockを呼び出し、プロンプトとレスポンスをパブリックインターネットに出さずAWS内に閉じる
- Cross-Region Inferenceにより、リージョン障害やトラフィック急増時もアプリケーション側のロジックなしで自動的に利用可能なリージョンへフェイルオーバーする
- SQL++生成・インデックス推奨・複数ターン対話など主要ワークフローごとに正確性・決定性・レイテンシ・フォーマット一貫性を基準にした評価スイートでモデルを比較してから採用する

## 使いどころ

- 複数のFMプロバイダを状況に応じて切り替えたいマルチテナントSaaSプロダクト
- データレジデンシーやSOC/HIPAA/ISOなどのコンプライアンス要件を満たしながらLLM推論を提供したいエンタープライズ向けサービス
- 新しいモデル世代を継続的に評価し迅速に本番導入したいプロダクトチーム
