---
type: guidance
title: 本番DBを守りながらリアルタイム推論するSilk仮想SAN構成
title_original: AI inferencing with Silk virtual SAN
industry: cross-industry
cloud:
- azure
patterns:
- inference-optimization
- rag
- reinforcement-learning
- data-federation
components:
- Azure Machine Learning
- Azure Kubernetes Service (AKS)
- Silk DataPod virtual SAN
- Silk Echo
- Azure Boost
- Microsoft OneLake
- Azure Virtual Machines
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/ai-inferencing-on-azure-iaas
published_at: '2026-09-03'
---

## 概要

Azure IaaS上にSilk Cloud Data Platformの仮想SANを構築し、推論ワークロードは本番データベースではなくSilk Echoのクローンから読み取ることで、リアルタイムAI推論を本番のトランザクション処理から分離するアーキテクチャ。モデル・データクローン・ストレージ層を同一ゾーンに配置しAzure Boostでネットワーク/ストレージ処理をオフロードすることで、推論レイテンシを高負荷下でも予測可能に保つ。

## 設計のポイント

- 推論ワークロードは本番データベースそのものではなくSilk Echoのクローンから読み取り、本番トランザクション処理への影響を分離する
- モデル・データクローン・ストレージ層を同一ゾーンに配置してデータ移動を減らし、推論レイテンシを予測可能にする
- Azure Boostでネットワーク/ストレージ処理を専用ハードウェアにオフロードし、VMのCPUリソースを推論と本番DBに振り向ける
- 推論結果とユーザー操作をレイクハウスに記録し、検証済みデータのみで強化学習によるモデルの継続的なファインチューニングに使う

## 使いどころ

- 本番データベースの性能を犠牲にせずリアルタイム推論を行いたいミッションクリティカルな基幹システム
- 不正検知やレコメンデーションなど低レイテンシ・高スループットが要求される推論基盤を構築したい場合
