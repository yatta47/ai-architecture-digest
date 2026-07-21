---
type: guidance
title: 説明可能性・解釈可能性・透明性を切り分けるAIガバナンス実務ガイド
title_original: 'AI transparency: governance, explainability, and data practices'
industry: cross-industry
cloud: []
patterns:
- guardrails
- responsible-ai-governance
components: []
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/ai-transparency
published_at: '2026-07-20'
---

## 概要

AIの透明性(データ・モデル挙動・意思決定過程の開示)を、個々の予測の説明可能性やモデル内部の解釈可能性と明確に区別した上で、モデルカードやデータシート、監査ログ、部門横断のガバナンス委員会による運用方法をまとめたガイド。EU AI Actなどの規制がハイリスク・汎用AIシステムに透明性文書化を法的に義務付けている点を指摘している。

## 設計のポイント

- 説明可能性を後付けの説明レイヤーではなく、モデルアーキテクチャ選定段階からの設計要件として組み込む。
- ローカル説明(個別予測)とグローバル説明(モデル全体の挙動)を両方用意し、利用者と監査者それぞれのニーズに応える。
- モデルのアーキテクチャ・バージョン履歴・学習データの来歴・説明可能性ツールの4種類のアーティファクトを、本番データと同じガバナンス体制の中央レジストリで管理する。

## 使いどころ

- 与信・採用・医療トリアージなど、誤りのコストが高いハイステークス意思決定にAIを使う組織。
- EU AI Actなど高リスクAIシステムの文書化義務に対応する必要があるコンプライアンス・法務チーム。
