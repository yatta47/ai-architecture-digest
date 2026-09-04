---
type: case
title: カタログ中心のエージェント型データガバナンス基盤
title_original: 'Governance Beyond Security: Knowledge, Context, and Ontology on the Lakehouse'
industry: healthcare
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Databricks Unity Catalog
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/governance-beyond-security-knowledge-context-ontology-lakehouse
published_at: '2026-09-03'
---

## 概要

医療データにおけるガバナンス(分類タグ・非識別化ポリシー・データ契約・モデルカード・リネージュ)をコンプライアンスの後付け作業ではなくAIの基盤となる意味論(オントロジー)そのものとして捉え直し、Unity Catalogに構造化メタデータとして格納することで、ビルドエージェントと分析エージェントがそのメタデータを実行時の指示として動くカタログ中心のエージェント型アーキテクチャを構築した。

## 設計のポイント

- 分類タグ・モデルカード・データ契約・リネージュなどのガバナンス成果物を意味論の原材料として捉え、カタログをエージェントが実行時に読む唯一の情報源にする
- De-ID(非識別化)とテストのエージェントを最初に実行し、最もリスクが高くマニュアル負荷が重い作業を先に自動化して早期に効果を出す
- ガバナンスをデータガバナンス・AI/MLガバナンス・データリテラシー・データマネジメント・オントロジーの5本柱として一つのレンズで扱い、監査を後付けでなく成果物として自動的に得られるようにする

## 使いどころ

- PHIなど機微データを扱う医療機関で、本番データを統制境界の外に出さずにAIエージェントを開発・運用したい場合
- ガバナンス作業を単なる監査対応で終わらせず、LLM/RAGのコンテキストとして再利用してコストを下げたい組織
