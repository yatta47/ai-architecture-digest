---
type: guidance
title: OpenAI Usage API/Cost APIによる利用状況モニタリング
title_original: How to use the Usage API and Cost API to monitor your OpenAI usage
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
components:
- OpenAI Completions Usage API
- OpenAI Costs API
outcome:
  type: cost
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/completions_usage_api/
published_at: '2025-01-14'
---

## 概要

OpenAIのCompletions Usage APIとCosts APIを使い、トークン使用量やコストをモデル別・期間別に取得してpandasで集計し、matplotlibで可視化するカスタムダッシュボードの作り方を解説する。デフォルトのダッシュボードでは足りない詳細なコスト分析ニーズに応える。

## 設計のポイント

- ページネーション付きAPIから全期間のバケットデータを取得しDataFrameに集約する
- group_byやbucket_widthなどのパラメータでモデル別・時間粒度別の粒度を切り替えられる設計にする
- 可視化を積み上げ棒グラフや円グラフなど用途別に使い分ける

## 使いどころ

- 組織のLLM利用コストをモデル・プロジェクト・APIキー単位で把握したいプラットフォームチーム
- デフォルトダッシュボードでは粒度が不足する詳細なコスト分析やチャージバックが必要な場合
