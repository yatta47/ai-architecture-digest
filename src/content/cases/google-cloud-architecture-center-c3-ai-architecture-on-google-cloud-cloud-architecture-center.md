---
type: case
title: C3 AIがGoogle Cloud上でマルチテナントAIプラットフォームを安全に提供する構成
title_original: C3 AI architecture on Google Cloud
company: C3 AI
industry: cross-industry
cloud:
- gcp
patterns:
- defense-in-depth
components:
- GKE
- Cloud SQL
- Cloud KMS
- Private Service Connect
- Cloud Storage
- VPC Service Controls
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/partners/c3-ai-architecture
published_at: '2026-07-19'
---

## 概要

エンタープライズAIプラットフォームを提供するC3 AIが、顧客ごとに専用プロジェクトとVPC Service Controlsの境界を設けてGoogle Cloud上でC3 AI Platformを展開するアーキテクチャ。Private Service Connectで顧客VPCとC3 AI側VPCをインターネットを介さずに接続し、GDPR等の規制に対応するため顧客テナント上にデプロイする代替構成も提供する。

## 設計のポイント

- 顧客ごとに専用のGoogle Cloudプロジェクトを割り当て、VPC Service Controlsでデータ流出を防ぐ境界を設ける
- Private Service Connectでインターネットを経由せず顧客VPCとC3 AI側VPCを private接続する
- Cloud KMSのCMEKでCloud SQL・Cloud Storage・GKEクラスタ内のデータを暗号化する
- データ主権要件が強い顧客向けには、C3 AI Platformを顧客自身のテナント内にデプロイする代替アーキテクチャを用意する

## 使いどころ

- 製造・金融・政府機関など規制の厳しい業界向けにマルチテナントAI SaaSを提供するベンダー
- GDPR等でデータのローカライズが求められる顧客に対応する必要があるエンタープライズAI導入
