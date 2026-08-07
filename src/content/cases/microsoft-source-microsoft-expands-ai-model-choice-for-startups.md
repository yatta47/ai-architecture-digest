---
type: guidance
title: スタートアップ向けオープンモデル推論をAzureに閉じて段階的にスケールさせる構成
title_original: 'How to deploy Fireworks AI on Microsoft Foundry: a startup architecture blueprint'
industry: cross-industry
cloud:
- azure
patterns:
- multi-model-routing
- cost-optimization
- inference-optimization
components:
- Microsoft Foundry
- Fireworks AI
- Azure Cache for Redis
- Azure Key Vault
outcome:
  type: cost
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/startups/blog/how-to-deploy-fireworks-ai-on-microsoft-foundry-a-startup-architecture-blueprint/
published_at: '2026-08-06'
---

## 概要

Microsoftは、スタートアップ向けにFireworks AIをMicrosoft Foundry上でホストするオープンモデル推論のブループリントを公開した。単一モデルをAPI Managementの背後にデプロイするところから始め、Azure Cache for Redisでの推論キャッシュや複数モデルのA/Bテストへと段階的にスケールさせる、Azureに閉じた構成でモデル選定・ガバナンス・課金を単一のコントロールプレーンにまとめる設計になっている。

## 設計のポイント

- GPUクラスタを自前で持たず、Fireworksが提供する推論レイヤーとFoundryのガバナンス層を組み合わせてインフラ運用を回避する
- サーバーレスの従量課金推論から始め、キャッシュ導入・複数モデルのA/Bテスト・自前ファインチューニングへと段階的にスケールする経路を用意する
- 評価済みのプロンプトや本番トラフィックをそのままファインチューニングの学習データとして転用し、同一プラットフォーム上でBYOWとして再デプロイする

## 使いどころ

- MVPからPMFへ移行する過程でインフラ投資を抑えつつモデルを切り替えたいAIネイティブなスタートアップ
- 単一のクローズドモデルへのロックインを避け、オープンモデルでコストと差別化の両方をコントロールしたいチーム
