---
type: guidance
title: AWS上でデータスペース基盤（Eclipse Dataspace Components）を構築する実装ガイド
title_original: 'Eclipse Dataspace Components on AWS: Data sharing fundamentals'
industry: cross-industry
cloud:
- aws
patterns:
- data-federation
- policy-as-code
components:
- Eclipse Dataspace Components (EDC)
- Amazon ECS
- Amazon Aurora
- Amazon API Gateway
- Amazon S3
- AWS Secrets Manager
- Amazon DynamoDB
- Gradle
data_sources:
- 共有データセット
- フェデレーテッドカタログ
- 検証可能クレデンシャル
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/eclipse-dataspace-components-on-aws-data-sharing-fundamentals/
published_at: '2026-07-17'
---

## 概要

IDSA標準とDataspace Protocol（DSP）に準拠したデータスペースを、Eclipse Dataspace Components（EDC）を用いてAWS上に実装するための3部構成シリーズの第1部。組織をまたいだ相互運用可能なデータ共有の理論的基盤、EDCのコアアーキテクチャ（フェデレーテッドカタログ、コネクタ、アイデンティティハブ）、および分散型のID検証（DCP/DID/検証可能クレデンシャル）の仕組みを解説する。

## 設計のポイント

EDCコネクタを制御プレーン（契約交渉）とデータプレーン（実データ転送）に分離し、SPI（契約定義）・Core（基本実装）・Extensions（AWS等への統合）の3層モジュール構成で拡張性を確保する。素の“バニラ”コネクタはAWS拡張を含まないため、version catalog・launcherモジュール・settingsファイルを使ったGradleのプラグイン型ビルドで、S3やSecrets Manager等のマネージドサービスをネイティブ統合したカスタムビルドを組み立てる。

## 使いどころ

企業や組織の境界を越えて、ポリシーと信頼に基づいた相互運用可能なデータ共有基盤（データスペース）をAWS上で標準準拠のかたちで立ち上げたいアーキテクトやプラットフォーム担当者に向く。
