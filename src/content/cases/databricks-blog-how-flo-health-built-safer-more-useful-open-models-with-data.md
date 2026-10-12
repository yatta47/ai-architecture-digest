---
type: case
title: Flo Healthが医療安全性と有用性を測る評価基盤で公開モデルを微調整
title_original: How Flo Health built safer, more useful open models with Databricks AI Runtime
company: Flo Health
industry: healthcare
cloud:
- multi-cloud
patterns:
- fine-tuning
- eval
- llmops
- cost-optimization
components:
- Databricks AI Runtime
- NVIDIA H100
- Direct Preference Optimization
- LLM-as-a-judge
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-flo-health-built-safer-more-useful-open-models-databricks-ai-runtime
published_at: '2026-10-12'
---

## 概要

女性向け健康アプリのFlo Healthは、医療安全性と有用性をルーブリック化したAI審査員を臨床医のレビューで較正し、合成データとSFT・DPOでオープンモデルを微調整した。32基のH100での分散学習により、安全性は34%から約61%、有用性は42%から76%に改善した。

## 設計のポイント

- 学習より先に評価を定義し、医療リスクを具体的なルーブリックに分解してAI審査員に変換、食い違いは盲検の臨床医が裁定する。
- プライバシー優先の合成データとAI審査員で、人手注釈の学習ペア無しに学習信号を作る。
- タスクごとに適切なモデルを使うcompound AIを見据え、推論コストをフロンティアAPI比で桁違いに抑える狙いがある。

## 使いどころ

- 医療や金融など安全性要件が高い領域で、専用のオープンモデルを育てたいチーム。
- LLM審査員を人手の判断で較正して評価を自動化したい場面。
