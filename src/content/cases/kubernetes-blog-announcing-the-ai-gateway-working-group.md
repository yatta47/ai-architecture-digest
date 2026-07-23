---
type: announcement
title: AIトラフィック向けゲートウェイ標準を策定するKubernetes AI Gateway Working Group発足
title_original: Announcing the AI Gateway Working Group
industry: cross-industry
cloud:
- multi-cloud
patterns:
- llm-gateway
- guardrails
- rag
components:
- Gateway API
- OpenAI
- Vertex AI
- Amazon Bedrock
- Model Context Protocol
outcome:
  type: risk-compliance
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/03/09/announcing-ai-gateway-wg/
published_at: '2026-03-09'
---

## 概要

Kubernetes上でAI推論トラフィックを扱うためのゲートウェイ標準を策定する新ワーキンググループが発足。トークン単位のレート制限やペイロード検査によるプロンプトインジェクション対策、外部AIサービスへの安全なegressルーティングなどを標準化する。

## 設計のポイント

- Gateway API仕様を土台に、AI特有の拡張（ペイロード検査・トークン単位のレート制限）をプラガブルに積み上げる設計にする
- クラスタ外の外部AIサービス（OpenAI・Vertex AI・Bedrockなど）への認証・トークン注入・リージョン制御をegress gatewayで一元化する
- セマンティックルーティングやキャッシュによる推論コスト削減、RAG統合をペイロード処理パイプラインの標準機能として定義する

## 使いどころ

- 複数クラウドのAI推論サービスへのフェイルオーバーやリージョンコンプライアンスを一元管理したいプラットフォームチーム
- プロンプトインジェクションやAPI乱用からKubernetes上のAI推論エンドポイントを守りたい運用者
