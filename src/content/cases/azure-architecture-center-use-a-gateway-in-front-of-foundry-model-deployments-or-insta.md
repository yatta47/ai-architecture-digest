---
type: guidance
title: 複数のAIモデルデプロイ/インスタンスをまとめるゲートウェイアーキテクチャ
title_original: Use a gateway in front of multiple model deployments or instances
industry: cross-industry
cloud:
- azure
patterns:
- llm-gateway
- multi-model-routing
components:
- Azure API Management
- Microsoft Foundry
- Azure RBAC
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/azure-openai-gateway-multi-backend
published_at: '2026-05-21'
---

## 概要

Azure Architecture CenterによるMicrosoft Foundryなど複数モデルデプロイ/インスタンスの前段にゲートウェイを配置する設計ガイド。単一インスタンス内の複数モデルデプロイから複数リージョン・複数サブスクリプションにまたがる複数インスタンスまで4つのトポロジを整理し、それぞれでゲートウェイによる集中ルーティング、認証情報の終端、クォータ管理、利用状況トラッキングの要否を解説する。ゲートウェイはブルーグリーンロールアウトやテナント単位のモデル振り分けなど、クライアントコードを変更せずにモデル切り替えを行うための抽象化層として機能する。

## 設計のポイント

- クライアントが直接モデルインスタンスを指定せず、ゲートウェイがルーティングを担うことでモデル切り替えをサーバー側だけで完結できる。
- ゲートウェイでクレデンシャルを終端し、そこからAzure RBACでバックエンドに接続することで最小権限アクセスを実現する。
- ゲートウェイをモデルホストと同一リージョンに配置し、バックエンドへの経路をゲートウェイ経由に限定してネットワークを制御する。
- クライアントのHTTPリクエスト情報を使ってモデルデプロイへのルーティングやクォータ制御を行い、チャージバック/ショーバックにも活用する。

## 使いどころ

- 汎用モデル・高性能モデル・ファインチューニング版など複数モデルを1つの窓口で使い分けたいとき。
- モデルのバージョンアップやブルーグリーンロールアウトをクライアントの再デプロイなしで行いたいとき。
- マルチテナントSaaSでテナントごとにモデルデプロイとレート制限/クォータを分離したいとき。
- クライアントコードを直接コントロールできない、またはクライアント設定変更のリスクが高い場合のモデル切り替え。
