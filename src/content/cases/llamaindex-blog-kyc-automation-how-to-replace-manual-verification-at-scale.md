---
type: guidance
title: 手動KYCを置き換えるKYC自動化の5段階アーキテクチャ
title_original: 'KYC Automation: How to Replace Manual Verification at Scale'
industry: financial-services
cloud: []
patterns:
- document-processing
- ai-agent
components: []
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/kyc-automation
published_at: '2026-07-18'
---

## 概要

文書収集・本人確認とデータ抽出・制裁リスト照合・リスクスコアリング・継続モニタリングという5段階でKYCを自動化するアーキテクチャを解説。レイアウト理解型の文書取り込みと、例外ケースのみ人手に回す設計で、手動KYCに比べコストと処理時間を大幅に削減できるとする。

## 設計のポイント

- 文書取り込みからモニタリングまでを5段階のパイプラインとして明確に分離する
- 標準ケースは自動処理し例外のみ人手レビューに回すことでアナリスト工数を例外対応に集中させる
- すべての判断をタイムスタンプ付き監査証跡として残し規制対応の説明責任を担保する

## 使いどころ

- 新規口座開設のオンボーディングを高速化したい銀行・フィンテック
- 制裁リスト照合をリアルタイム化したいコンプライアンス部門
