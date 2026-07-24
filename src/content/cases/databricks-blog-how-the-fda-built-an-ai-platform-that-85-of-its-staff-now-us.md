---
type: case
title: FDAがガバナンス基盤ELSA/Haloを構築しスタッフの85%が日常利用
title_original: How the FDA built an AI platform that 85% of its staff now use daily
company: US FDA
industry: public-sector
cloud: []
patterns:
- ai-agent
- rag
- document-processing
- llm-gateway
components:
- Databricks
- Unity Catalog
- MLflow
- MCP
- ELSA
- Halo
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-fda-built-ai-platform-85-its-staff-now-use-daily
published_at: '2026-07-23'
---

## 概要

米FDAは8センターに分散していたデータ基盤をDatabricks上に統合(Halo)し、その上に全16,000職員が使える生成AIプラットフォームELSAを構築。導入2ヶ月で利用率が1%未満から85%に達し、数百万ページの規制文書から回答を数分で得られるようになった。

## 設計のポイント

- 8つのセンターに分散していたバラバラなAI基盤・データストアをUnity Catalogのガバナンス機能で1つのプラットフォームに統合し、機微な規制データへの粒度の細かいアクセス制御を担保する
- Unity Catalogの上にMCPサーバーを重ねることで、データサイエンティストでなくとも職員自身が業務手順書などを取り込んで独自エージェントを作成できるようにする
- MLflowを使ったNLP抽出パイプラインで数百万ページの非構造化規制文書から構造化データを事前抽出し、ELSA経由でグラウンディングされた即答を実現する

## 使いどころ

- 複数部門・複数データサイロを抱える大規模組織で統合AI基盤を全社展開したい場合
- 専門知識を持つ現場職員自身がノーコードに近い形でエージェントを作れるようにしたい組織
