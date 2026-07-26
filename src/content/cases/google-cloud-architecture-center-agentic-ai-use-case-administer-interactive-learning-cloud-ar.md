---
type: guidance
title: セッション状態と長期記憶で個別最適化する対話型学習クイズエージェント
title_original: 'Agentic AI use case: Administer interactive learning'
industry: other
cloud:
- gcp
patterns:
- ai-agent
- memory-consolidation
components:
- Cloud Run
- Gemini Enterprise Agent Platform
- Gemini Enterprise Agent Platform Sessions
- Memory Bank
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/agentic-ai-interactive-learning
published_at: '2026-07-19'
---

## 概要

Google Cloudは、ユーザーの理解度を評価しながら難易度を動的に調整する対話型学習クイズエージェントのアーキテクチャを示す。セッション状態をGemini Enterprise Agent Platform Sessionsに保存し、Memory Bankで長期記憶化することで、次回以降のセッションでも個別最適化された体験を提供する。

## 設計のポイント

- クイズの進捗とスコアをセッション履歴に都度追記し、回答内容に応じて次の問題の難易度・内容を動的に調整する
- セッションデータをMemory Bankで長期記憶に変換し、過去の学習履歴を踏まえた文脈に応じた応答を将来のセッションで生成する
- クイズ開始・回答評価・次問生成といったアクションごとにツールを切り替える形でエージェントの振る舞いを構成する

## 使いどころ

- 受講者ごとに難易度を調整したい教育・研修プロダクトの開発者
- 長期的な学習履歴をもとにパーソナライズされた体験を提供したいエドテック事業者
