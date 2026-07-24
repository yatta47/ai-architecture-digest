---
type: guidance
title: 基盤モデルのライフサイクル管理を前提としたAIワークロード設計
title_original: Design to support foundation model life cycles
industry: cross-industry
cloud:
- azure
patterns:
- llmops
components:
- Azure OpenAI
- Microsoft Foundry
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/manage-foundation-models-lifecycle
published_at: '2025-05-17'
---

## 概要

基盤モデルをコードライブラリと同様のバージョン付き依存関係として捉え、マイナー更新から世代交代までの更新スコープごとの影響とメリットを整理する。MaaS/MaaP/セルフホストというデプロイ戦略ごとに異なるモデル廃止・退役の挙動を踏まえ、ワークロードを設計する重要性を説く。

## 設計のポイント

- 基盤モデルをコード依存関係と同様にバージョン管理し、廃止・退役スケジュールに備えた設計を行う
- MaaS/MaaP/セルフホストというデプロイ戦略ごとにモデル退役時の挙動が異なることを理解し、それぞれに応じた移行計画を立てる
- オーケストレーション層で複数バージョンのモデルを並行運用できるようにし、安全な移行経路を確保する

## 使いどころ

- Azure OpenAIなどMaaS上で運用しているサービスが、モデル廃止によるHTTPエラーで停止するのを防ぎたい場合
- 新しい世代のモデルへ計画的に移行するためのガバナンスプロセスを整備したいAI基盤運用チーム
