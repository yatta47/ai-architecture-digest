---
type: guidance
title: AWSリソースの依存関係発見からカオス実験生成までをAIエージェントが自動化するレジリエンスフレームワーク
title_original: Architecting AI-powered resilience framework on AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- chaos-engineering
- ci-cd
- disaster-recovery
components:
- AWS Resilience Hub
- AWS Fault Injection Service
- Amazon Bedrock AgentCore
- AWS Systems Manager
- AWS Config
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/architecting-ai-powered-resilience-framework-on-aws/
published_at: '2026-06-22'
---

## 概要

AWS Resilience Hub、AWS Fault Injection Service、Amazon Bedrock AgentCore、AWS Systems Managerを組み合わせ、数週間かかっていたインフラ依存関係の把握とカオス実験の設計を数時間に短縮する5層のAIレジリエンスフレームワークを解説する。AgentCore上でホストされたAIエージェントがCloudFormationテンプレートやコードリポジトリ、実行時挙動を解析して隠れた依存関係を特定し、アーキテクチャに合わせた実験を自動生成、CI/CDパイプラインに継続的に組み込む。

## 設計のポイント

- AWS Config が追跡する差分のみを再解析することで、初回の依存関係マッピング後は変更分だけを処理し、常に最新のアーキテクチャマップを低コストで維持する。
- 専門のカオスエンジニアリング人材がいなくても、AIエージェントが実アーキテクチャに合わせた実験テンプレートを生成することで専門知識の壁を下げる。
- レジリエンス検証を一度きりのプロジェクトではなくCI/CDパイプラインに組み込み、リグレッションを本番到達前に検知する継続的な検証ループにする。

## 使いどころ

- デプロイのたびにドキュメントが陳腐化し、単一障害点が未検証のまま本番に残ってしまう分散システムを運用するSRE/DevOpsチーム。
- カオスエンジニアリングの専門知識を持つ人材が社内におらず、レジリエンステストの導入を諦めていた組織。
- MTTRやRTO/RPOの改善を数値目標として掲げ、障害対応能力の成熟度を高めたいクラウドアーキテクトチーム。
