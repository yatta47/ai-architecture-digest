---
type: case
title: 全社AIコアを4年かけて構築した不動産金融大手のデータ基盤戦略
title_original: Your AI is ready. Your data foundation probably isn't.
company: Cushman & Wakefield
industry: other
cloud: []
patterns:
- text-to-sql
- data-federation
components:
- Databricks
- Genie
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/your-ai-ready-your-data-foundation-probably-isnt
published_at: '2026-07-16'
---

## 概要

商業不動産サービス大手Cushman & Wakefieldは、事業部門にテクノロジストを配置するプロダクト運営モデルと、事業責任者との共同投資意思決定を4年間続け、全社共通の企業AIコアを構築してきた。Databricksの自然言語データガバナンスツールGenieを活用し、専門知識がなくてもデータ品質検証やガバナンスポリシーの確認を行えるようにしたことで、アイデアから成果までのリードタイムを月単位から日単位へ短縮した。

## 設計のポイント

- 技術投資をサイバー・インフラを除き必ず事業責任者と共同立案・共同発表する仕組みにし、全社の優先事項と技術投資を常に一致させる。
- 「AIパイロットの乱立」を避け、トップダウンで最大インパクトの領域から着手することで、データ基盤への信頼を先に確立してからAI活用を広げる。
- 自然言語インターフェース（Genie）でデータ品質・ガバナンス確認を非技術者でも行えるようにし、共通データ基盤への信頼を現場レベルで底上げする。

## 使いどころ

- 複数事業部が分断されたデータとサイロ化したAI施策を抱える大企業のデータ・AI戦略担当者。
- 技術投資と事業優先順位を一致させるガバナンス体制を作りたいCIO/CDIO。
- 非技術者でもデータ品質やガバナンス状況を自分で確認できるようにしたい組織。
