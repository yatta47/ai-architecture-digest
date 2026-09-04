---
type: case
title: NVIDIA社内の連合Kubernetes基盤を横断するID伝搬ゲートウェイ
title_original: How to Carry User Identity Across Federated Kubernetes and AI Platforms
company: NVIDIA
industry: cross-industry
cloud:
- multi-cloud
patterns:
- identity-federation
- defense-in-depth
components:
- OpenID Connect
- Redis
- Istio
- OPA
- Kubernetes
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-carry-user-identity-across-federated-kubernetes-and-ai-platforms/
published_at: '2026-09-03'
---

## 概要

NVIDIAは複数クラスタ・複数クラウド(AWS/OCI)にまたがる社内AI/データプラットフォームで、各サービスが独自にOIDCログインを行っていたことでログインの重複やセッション不整合が発生していた課題に対し、セッション所有を中央の認証ゲートウェイに集約し各リージョンのゲートウェイは共有Redisセッションストアの検証のみを行うアーキテクチャに変更し、社内開発者プラットフォーム全体で再ログイン発生率を55%削減した。

## 設計のポイント

- セッションの所有権(発行・更新・失効)を中央のゲートウェイに集約し、各データプレーンのゲートウェイは検証だけを行うステートレスな構成にする
- 標準のOpenID Connectと最小限の/gateway/userinfo検証エンドポイント、TTL付きの共有Redisセッションストアで一貫したログアウト・トークン更新を実現する
- ゲートウェイ間はmTLSやワークロードIDで保護し、受信した信頼できないIDヘッダーは一度剥がしてから信頼済みヘッダーを注入する

## 使いどころ

- 複数クラスタ・複数クラウドにまたがる社内開発者ポータルやAIプラットフォームで、ツールごとに再ログインが発生し体験が分断されている組織
- AIアシスタントがユーザーの委任されたアイデンティティで複数クラスタのサービスを横断的に呼び出す必要がある場合
