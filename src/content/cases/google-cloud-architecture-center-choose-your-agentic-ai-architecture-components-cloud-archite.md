---
type: guidance
title: エージェント型AIアーキテクチャのコンポーネント選定ガイド
title_original: Choose your agentic AI architecture components
industry: cross-industry
cloud:
- gcp
patterns:
- ai-agent
- human-in-the-loop
components:
- Agent Development Kit (ADK)
- AG-UI
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components
published_at: '2026-07-19'
---

## 概要

Google Cloudは、エージェント型AIアプリケーションを構成するフロントエンド・エージェント開発フレームワーク・ツール・メモリ・実行基盤・AIモデルという各コンポーネントの選び方を整理したガイドを提供する。プロトタイプ用と本番用でフレームワークの要件が異なる点や、ADKによる開発の勘所を解説する。

## 設計のポイント

- 社内デモやPoCには同期的なリクエスト・レスポンス型のプロトタイピング用フレームワーク（Mesop、Gradioなど）、外部公開の本番アプリにはストリーミングやステートフルなメモリ管理に対応した本番フレームワークを使い分ける
- フロントエンドとエージェント間の通信にはAG-UIプロトコルを使い、エージェントの応答やUI状態更新、クライアント側アクションのトリガーを標準化する
- 決定的な問題や単一のモデル呼び出しで完結するタスク（要約・翻訳・分類など）にはエージェント化せず、非エージェント型のソリューションを選ぶ
- Google CloudではAgent Development Kit(ADK)を推奨フレームワークとし、Geminiに最適化しつつ他モデル・他ランタイムとの互換性も確保する

## 使いどころ

- エージェント型AIアプリケーションのフレームワークやランタイムを比較検討しているアーキテクト
- PoCから本番運用へエージェントアプリを移行させたい開発チーム
