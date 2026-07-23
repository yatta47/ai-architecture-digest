---
type: guidance
title: ChatKitでウィジェット付きエージェントUIを組む4つのシナリオ別サンプル
title_original: openai-chatkit-advanced-samples
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- ChatKit
- ChatKit.js
- FastAPI
- React
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-chatkit-advanced-samples
published_at: '2025-10-06'
---

## 概要

OpenAIのChatKit Python SDKとChatKit.jsを組み合わせ、FastAPIバックエンドとReactフロントエンドでシナリオ別のエージェントUIを構築するサンプル集。猫の世話、航空カスタマーサポート、記事検索、路線図プランナーの4例を通じ、サーバー/クライアントのツール呼び出し・ウィジェットアクション・進捗通知・ページ認識応答といった実装パターンをカバーする。

## 設計のポイント

- サーバーツールでアプリ固有データを取得しつつ、クライアントツールでUI上の選択状態（地図の選択駅など）をエージェント入力に還元する双方向設計
- ウィジェットアクションはクライアント側とサーバー側の両方でハンドリング可能にし、状態更新後にウィジェットを再ストリームして最新化する
- 顧客プロファイルなど文脈情報をリクエストのたびにプロンプトへ付加し、エージェントが毎回状態を把握できるようにする
- 検索や地図取得など時間のかかる処理中はProgressUpdateEventをストリームし、UIに『検索中…』を表示してユーザー体験を保つ

## 使いどころ

- チャットUIにインタラクティブなウィジェットや進捗表示を組み込みたい開発者の実装リファレンス
- 航空会社のカスタマーサポートなど、状態を持つ業務エージェントを設計するチーム
- ページ内容やクライアント側の選択状態をエージェントの文脈に取り込みたいケース
