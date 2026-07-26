---
type: guidance
title: ナレッジベース検索と回答生成を2段階に分けたRAG型カスタマーサポート解決策生成
title_original: 'Generative AI use case: Generate solutions for customer-support questions'
industry: cross-industry
cloud:
- gcp
patterns:
- rag
- ai-agent
components:
- GKE
- Gemini API
- Cloud Storage
- Agent Platform
outcome:
  type: quality
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/genai-customer-support
published_at: '2026-07-19'
---

## 概要

顧客からの質問に対し、まずGemini APIでナレッジベースから関連リソースを特定する「取得サービス」が動き、その結果を別の「解決策生成サービス」がGemini APIに渡して具体的な回答を生成する2段階RAGアーキテクチャ。両サービスはGKE上のコンテナとして分離デプロイされる。

## 設計のポイント

- リソース取得と解決策生成を別サービスに分離し、それぞれ独立してスケール・改善できるようにする
- Geminiにナレッジベースの関連リソースIDだけを返させてから本文を取得することで、コンテキスト長を抑えつつ精度を確保する
- ステップバイステップ手順や動画ウォークスルーなど、生成する解決策のフォーマットを問い合わせ内容に応じて変える設計にしている

## 使いどころ

- FAQやナレッジベースを保有し、問い合わせ対応の一次回答を自動生成したいサポート部門
- RAGを2段階の疎結合サービスとして構築しGKEでスケールさせたい開発チーム
