---
type: guidance
title: モデル・コンテキスト・ハーネスの3層で見るエージェント信頼性
title_original: You chose the best model. Why is your agent still failing?
industry: cross-industry
cloud: []
patterns:
- context-engineering
- eval
- ai-agent
components:
- Atlan Context Agents
- Atlan Context Engineering Studio
outcome:
  type: reliability
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/why-is-your-agent-still-failing-context-harness-evaluation/
published_at: '2026-08-12'
---

## 概要

ArizeとAtlanは、信頼できるエンタープライズAIシステムはモデル(推論)・コンテキスト層(ビジネス定義やポリシー)・ハーネス(検索・ツール・メモリ・権限・引き継ぎ)の3層で構成され、評価は全層を横断すべきだと論じる。強いモデルでも古いコンテキストを与えられると『自信を持って的外れ』な答えを返すため、コンテキストをコードと同じライフサイクルで継続的に構築・検証・ガバナンスする必要があるとする。

## 設計のポイント

- モデル・コンテキスト層・ハーネスの3層でエージェントアーキテクチャを捉え、評価を全層に横断させて障害箇所を切り分けられるようにした。
- コンテキストを一度書いて終わりにせず、ビルド・テスト・レビュー・承認・デプロイ・学習というコードと同じライフサイクルで継続的に管理する仕組みにした。
- 定義や信頼シグナルに所有者・バージョン・承認履歴を付与し、モデルドリフトやデータドリフトと同様にコンテキストドリフトも監視対象にした。

## 使いどころ

- 精度の高いモデルを選んだのにエージェントの出力が不安定・的外れになる原因を切り分けたいチーム。
- 複数のエージェントに一貫したビジネス定義・権限・承認フローを持たせたいエンタープライズのプラットフォーム担当者。
- モデルベンチマークだけでは測れない、自社の実運用データに対するエージェント信頼性を評価したいエンジニア。
