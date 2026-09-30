---
type: guidance
title: MongoDB Atlas Agent EngineのエージェントトレースをArize AXへ送る評価・可観測性連携
title_original: Building production-ready AI agents with Atlas Agent Engine and Arize AX
company: Arize AI
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- llmops
components:
- MongoDB Atlas Agent Engine
- Arize AX
- OpenTelemetry
- OpenInference
- Signal
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/using-arize-ax-with-mongodb-atlas-agent-engine/
published_at: '2026-09-30'
---

## 概要

MongoDBの新プラットフォームAtlas Agent Engine上で動くエージェントのOpenTelemetryトレースを、ローンチパートナーであるArize AXへエクスポートする連携と設定手順を解説する。Arize AXではモデル呼び出し・検索・ツール呼び出し・レイテンシ・トークン使用量をスパン単位で確認し、最終出力と実行経路の双方をオンライン評価できる。失敗例はアノテーションキューを経てデータセット化され、再デプロイ前の実験で修正案を比較できる。

## 設計のポイント

- もっともらしい最終回答の裏に潜む誤った検索やツール呼び出しを捉えるため、最終出力だけでなく実行経路全体のトレースを評価対象にする。
- OpenTelemetry GenAIセマンティック規約とOpenInferenceに準拠したOTLPで送ることで、独自の計装コードなしに観測バックエンドを接続する。
- 本番トラフィックのオンライン評価で見つかった失敗をアノテーションキュー経由でデータセット化し、修正案を再デプロイ前に実験で比較する。

## 使いどころ

- Atlas Agent Engineでエージェントをプロトタイプから本番運用へ移行しようとしているチーム。
- 誤った文書の取得や不要な高価モデルの利用など、エージェントの挙動上の失敗を特定・デバッグしたい場面。
- エージェントの変更が本当に改善になったかを、本番データに基づく評価で確かめてから再デプロイしたい場面。
