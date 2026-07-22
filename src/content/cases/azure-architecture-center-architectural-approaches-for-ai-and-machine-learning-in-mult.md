---
type: guidance
title: マルチテナントAI/MLソリューションにおけるモデル分離アーキテクチャ
title_original: Architectural approaches for AI and machine learning in multitenant solutions
industry: cross-industry
cloud:
- azure
patterns:
- llmops
- fine-tuning
- multi-tenant-ml
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/ai-machine-learning
published_at: '2026-04-29'
---

## 概要

マルチテナントAI/ML基盤の設計アプローチとして、テナント専用モデル(データ機密性が高い場合)、全テナントで共有する事前学習済みモデル、ベースモデルをテナントごとにチューニングする「チューニング済み共有モデル」の3パターンを比較。学習と推論の要件を分けて検討する必要性、テナント間のデータ・モデル分離、MLOps/GenAIOpsの運用体制構築の重要性を解説する。

## 設計のポイント

- 学習(トレーニング)と推論の要件をテナンシーモデルの観点で別々に検討する
- テナントのデータ機密性や他テナントへの汎化可能性に応じて、テナント専用モデル・共有モデル・チューニング済み共有モデルを使い分ける
- 共有モデルの学習にテナントデータを使う場合は、テナントの同意取得と識別情報の除去を徹底する

## 使いどころ

- 複数テナント向けにAI/ML機能を提供するSaaSプロバイダーがモデルの分離戦略を検討する場合
- テナントごとのデータ機密性とコスト効率のバランスを取りながらAI機能を展開したい場合
