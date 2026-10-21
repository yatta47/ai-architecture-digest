---
type: guidance
title: DatabricksでRFD4-Proteinaを研究データ付きで動かす
title_original: Deploy RFD4-Proteina on Databricks
company: Databricks / NVIDIA
industry: healthcare
cloud: []
patterns:
- ai-agent
- llmops
components:
- RFD4-Proteina
- Genesis Workbench
- Databricks AI Runtime
- Genie Code
- BioNeMo Agent Toolkit
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/deploy-rfd4-proteina-model-databricks
published_at: '2026-10-21'
---

## 概要

タンパク質設計モデルRFD4-Proteinaを、オープンな青写真Genesis Workbench経由でDatabricks AI Runtimeのサーバーレス GPU上で実行する構成を紹介する。研究データ・実験追跡・ガバナンスを同一基盤にまとめる。

## 設計のポイント

- モデルを研究データの隣で動かし、機密IPを外に出さない。
- Genie Codeとエージェントスキルで入力準備から候補分析までのパイプラインを構築する。

## 使いどころ

- 創薬・ライフサイエンスで新モデルを自社実験データと結びつけたい場面。
