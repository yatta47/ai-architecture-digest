---
type: guidance
title: タスク適合性とルーティング戦略で選ぶAIモデル選定フレームワーク
title_original: Choose the right AI model for your workload
industry: cross-industry
cloud:
- azure
patterns:
- multi-model-routing
- llm-gateway
components: []
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/choose-ai-model
published_at: '2026-02-18'
---

## 概要

数千のAIモデルからワークロードに適したものを選ぶための判断基準（タスク適合性、コスト、コンテキスト長、セキュリティ、リージョン可用性など）を優先順位付きで整理する。単一モデルで完結させるか、コスト最適化・品質最適化・バランス型のモデルルーティング層を挟むかの設計判断も解説する。

## 設計のポイント

- タスク適合性を最優先の判断軸とし、チャット・推論・埋め込み・RAG・マルチモーダルなど目的別にモデル特性を見極める
- リクエストの複雑度や重要度に応じてコスト最適化・品質最適化・バランス型のルーティング戦略を選び、モデル選定を設計時の静的判断から実行時の動的判断へ移行する
- ルーティング対象モデル群の中で最小のコンテキストウィンドウが実効上限になる点など、ルーター導入固有の制約を事前に把握する

## 使いどころ

- リクエストの複雑さにばらつきがあり、簡単な処理は安価なモデルに、難しい処理は高性能モデルに振り分けたいワークロード
- マルチステップ推論やツール呼び出しを伴うエージェント型ワークロードで、モデルごとの推論品質とレイテンシ予測性を評価したい設計者
