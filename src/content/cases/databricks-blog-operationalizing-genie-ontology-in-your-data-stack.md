---
type: guidance
title: AIエージェントに業務文脈を伝えるデータ基盤の育て方（Genie Ontology）
title_original: Operationalizing Genie Ontology in your data stack
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
- data-federation
components:
- Unity Catalog
- Genie
- MCP
- Delta Lake
- dbxmetagen
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/operationalizing-genie-ontology-your-data-stack
published_at: '2026-09-01'
---

## 概要

LLMは業務のドメイン知識を知らないため、Genie Ontologyは意味モデルとテーブル・クエリ・ダッシュボードから推測した文脈を組み合わせてAIエージェントに権限付きの業務文脈を渡す。物理的なデータ基盤の整備からメタデータ充実、意味レイヤー構築、資産のキュレーション、権限統治、評価改善まで6層の段階的な成熟パスをドメイン単位で進めることを推奨する。

## 設計のポイント

- 物理層はLayer 0として先に固め、実体解決とconformedディメンションで一貫したgold層を作ってからビジネス意味付けに進む
- テーブル・カラムの説明とタグ付けをLLM(dbxmetagen)で自動生成しつつ、人がレビューしてから確定させる
- 意味モデルで『頭』を明示的に定義し、Genie Ontologyに周辺文脈の『尾』を推論させる分業にする
- 一度に全ドメインを整備せず1ドメインずつ展開し、キュレーションと評価を継続的に回して精度を上げる

## 使いどころ

- 社内データに対する自然言語Q&AエージェントをGenie等で構築するデータプラットフォームチーム
- MCP経由で外部エージェントに業務コンテキストを公開したい組織
- AI回答精度向上のためメタデータ・意味モデル整備の優先順位を決めたいデータガバナンス担当
