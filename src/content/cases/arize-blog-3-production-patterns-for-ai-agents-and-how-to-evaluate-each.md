---
type: guidance
title: 本番AIエージェントの3類型とハーネス・評価設計の指針
title_original: 3 production patterns for AI agents and how to evaluate each one
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- eval
- llmops
components:
- Mastra
outcome:
  type: reliability
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/3-production-patterns-ai-agents-how-to-evaluate-each-one/
published_at: '2026-07-10'
---

## 概要

MastraのCEO Sam Bhagwatの講演をもとに、本番AIエージェントを「カスタマー向け」「社内エンタープライズ」「開発者プラットフォーム」の3パターンに分類し、それぞれで異なるハーネス・評価計画・ロールアウト戦略が必要になることを解説する。カスタマー向けはモデル選定よりコンテキストエンジニアリングが鍵となり、推論コストと精度不足という2つの落とし穴に注意が必要だとする。

## 設計のポイント

- 顧客向け・社内エンタープライズ・開発者プラットフォームの3パターンでハーネスと評価計画とロールアウト戦略を変える
- カスタマー向けエージェントはモデル切り替えより、アカウントデータやポリシー文書へのアクセスなどコンテキストエンジニアリングを優先する
- 本番投入前は1〜5%の段階的ロールアウトから始め、本番トレースで見つかった失敗からeval網羅性を広げる
- 社内エンタープライズは1つの高頻度ワークフローに絞ってプロトタイプし、ハーネスが固まってから標準化する

## 使いどころ

- プロトタイプから本番移行する際に自分たちがどのパターンに該当するか判断したいチーム
- カスタマー向けAIアシスタントで推論コスト急増や精度不足のリスクに事前対応したいプロダクトチーム
- 断片化した社内システムをまたぐエンタープライズ検索や業務自動化を構築するops/platformチーム
- 複数チームが使う共通のエージェント基盤(認証・トレーシング・デプロイ)を提供したいプラットフォームエンジニアリング組織
