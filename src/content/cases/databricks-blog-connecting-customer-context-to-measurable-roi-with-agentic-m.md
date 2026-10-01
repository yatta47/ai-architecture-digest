---
type: opinion
title: エージェント型マーケティングにおける顧客コンテキストとID解決・効果測定
title_original: Connecting customer context to measurable ROI with agentic marketing
company: Databricks
industry: retail
cloud: []
patterns:
- ai-agent
- context-engineering
- decision-execution
- guardrails
components:
- Databricks
- CustomerLake
- Acxiom Real ID
- Lovelytics
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/connecting-customer-context-measurable-roi-agentic-marketing
published_at: '2026-10-01'
---

## 概要

Databricksは、信頼できる顧客・事業・意思決定コンテキストに基づいてAIエージェントが顧客ごとの次善アクションを推奨する、エージェント型マーケティングを論じる。ID解決を継続的に維持する基盤と、意思決定ループ内でのインクリメンタリティ測定が要点で、AcxiomのReal IDエンジンをDatabricks上でネイティブ稼働させた例も紹介する。

## 設計のポイント

- エージェントに渡すコンテキストを顧客・事業・意思決定・制御(ガードレールや承認点)の4種に分けて整理する。
- ID解決は一度きりのプロジェクトでなく、デバイスや連絡先の変化に追随して継続的に維持する。
- IDエンジンをデータのある場所でネイティブに動かし、外部環境へのエクスポートを避ける。
- 測定を意思決定ループに組み込み、施策がなければどうなったかとの比較を次の判断のコンテキストに戻す。

## 使いどころ

- マーケティングと財務が投資判断の共通根拠を必要とする場面。
- 既知顧客と匿名シグナルを同一基盤で扱い、プライバシーとガバナンスを保ちたい場面。
- 多数のmartechツールに分散した顧客データの重複を減らしたい場面。
