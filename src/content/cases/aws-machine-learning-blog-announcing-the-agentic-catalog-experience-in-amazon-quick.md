---
type: announcement
title: 上流データカタログのセマンティクスを継承するエージェント型BIカタログ
title_original: Announcing the Agentic Catalog Experience in Amazon Quick
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- text-to-sql
- context-engineering
components:
- Amazon Quick
- AWS Glue Data Catalog
- Databricks Unity Catalog
- Snowflake Horizon
- Collibra
- dbt
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/announcing-the-agentic-catalog-experience-in-amazon-quick/
published_at: '2026-07-31'
---

## 概要

Amazon QuickのAgentic Catalog Experienceは、Glue Data CatalogやUnity Catalogなど上流のデータカタログが持つテーブル/カラム定義や主キー・外部キー関係を、対話型のQuick Agentが発見・継承してデータセットとTopicを自動生成する機能。データキュレーターがテーブルを手作業で探索し定義を再入力する手間をなくし、Text2SQLやダッシュボードのための意味的コンテキストを一貫させる。

## 設計のポイント

- 上流カタログを唯一の真実源とし、生成したデータセットは既定でDirectQueryかつメタデータを読み取り専用にして意味的ドリフトを防ぐ
- 継承範囲をテーブル/カラム定義と主キー・外部キー関係に意図的に限定し、ノイズを避けつつ段階的に拡張できる設計にしている
- 自然言語での資産探索により、Gold/Silver/Bronze分類や品質スコアなど既存のガバナンスメタデータを検索の重み付けに活用する

## 使いどころ

- 数千テーブル規模のエンタープライズカタログから、業務ユーザー向けに必要な表だけを高速に絞り込みたい場合
- BIエンジニアやアナリストが、意味定義の重複入力や定義の食い違い（例: revenueの定義）を解消したい場合
- 上流カタログの更新にBI側の意味情報を追従させ続けたいデータガバナンス担当者
