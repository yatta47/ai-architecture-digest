---
type: opinion
title: AIネイティブ企業の財務が粗利を守る——オントロジー基盤で動くAIコワーカー活用論
title_original: How Tech Builds AI, and Finance Protects Margin
industry: cross-industry
cloud: []
patterns:
- text-to-sql
- context-engineering
- ai-agent
- human-in-the-loop
components:
- Databricks Genie One
- Unity Catalog
- Lakebase
- Databricks Marketplace
- Delta Sharing (Open Sharing)
- Stripe
- NetSuite
data_sources:
- 利用量データ
- コンピュートコスト
- 課金・サブスク/従量課金データ
- 決済トランザクション
- 収益・粗利データ
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/tech-builds-ai-finance-protects-margin
published_at: '2026-07-17'
---

## 概要

利用量・価格・コンピュートコストが時間単位で動くAIネイティブ企業では、月次で締める従来の財務基盤ではユニットエコノミクス（粗利）を守り切れない、という問題提起の論考。Databricksは、数値の「意味」を捉え続けるオントロジーと、それに根ざして自然言語で出典付きの回答を返す『Genie One』を財務向けAIコワーカーとして位置づけ、Amagiの本番運用などを例に挙げる。

## 設計のポイント

- 精度（正しい数字）だけでなく、製品・利用実態・プラン条件に根ざした「正確さ」を担保するため、ビジネスの意味を捉えるオントロジーを常に最新化する
- 運用データと分析データをUnity Catalog／Lakebaseで一つの基盤に統合し、Stripe等の外部データもETLなしで取り込む
- 回答は出典追跡・権限・AIコスト自体まで一元的にガバナンスする
- 最終判断は人間（human-in-the-loop）が下し、リプライシングやメータリング修正などのアクションにつなげる

## 使いどころ

- サブスクと従量課金が混在し、コンピュートが最大の変動費になっているテック／AIネイティブ企業のCFO・財務（FP&A）チーム
- 粗利・収益リスク・コンピュート消費を、月次締めではなく継続的に舵取りしたい場面
