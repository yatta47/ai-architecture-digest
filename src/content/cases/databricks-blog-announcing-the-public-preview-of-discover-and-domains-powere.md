---
type: announcement
title: Unity Catalogのドメインでデータ・AI資産を整理し、Genieエージェントの検索を業務文脈で絞り込む
title_original: Announcing the Public Preview of Discover and Domains, powered by Unity Catalog
company: Databricks
industry: cross-industry
cloud: []
patterns:
- context-engineering
- rag
- ai-agent
components:
- Unity Catalog
- Unity Catalog Semantics
- Genie One
- Genie Code
- Genie Ontology
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/announcing-public-preview-discover-and-domains-powered-unity-catalog
published_at: '2026-07-21'
---

## 概要

Databricksは、Unity Catalog上でデータ・AI資産を部門や事業ユニットなどの業務単位「Domain/Subdomain」で整理し、社内マーケットプレイスとして閲覧・検索できるDiscoverページをパブリックプレビューとして発表した。認定済み資産やAIによるレコメンドで人が信頼できる資産に辿り着きやすくすると同時に、そのドメイン構造をGenie OntologyやUnity Catalog Semanticsに連携させることで、Genie One・Genie CodeなどのエージェントもユーザーごとのAI権限内で関連性の高い信頼できる資産に検索範囲を絞り込めるようにする。

## 設計のポイント

- 組織の業務構造(部門・事業ユニット・地域)に沿ったDomain/Subdomainでデータ・AI資産を分類し、技術的な保管場所ではなく業務観点で発見できるようにする。
- 認定(Certification)・利用実績・人気度などのシグナルに基づくAIレコメンドを組み合わせ、信頼できる資産を優先的に提示する。
- 人向けに整理したDomainのメタデータをUnity Catalog SemanticsとGenie Ontologyにそのまま連携させ、エージェントの検索範囲をドメイン単位に絞り込みつつ既存の権限モデル内で回答させる。
- 各Domainにオーナーや説明・連絡先を付与し、ガバナンスの説明責任と資産の信頼性シグナルを明示する。

## 使いどころ

- データ・AI資産が急増し、どれが信頼できる正解データか分からなくなってきた組織のデータガバナンス/データスチュワード担当者。
- 複数の社内エージェント(Genie等)が誤ったテーブルや古い指標を参照するリスクを減らしたい場合。
- 「このテーブルが正か誰かに聞く」を減らし、業務ユーザーが自力で信頼できるダッシュボードやテーブルに辿り着けるようにしたい場合。
