---
type: case
title: 需要予測から発注までを自律ループで自動化する補充システム
title_original: Automate replenishment with MMF, Databricks Genie, and Amazon Quick
industry: retail
cloud:
- aws
patterns:
- ai-agent
- decision-execution
- event-driven
components:
- Databricks Many Model Forecasting
- Chronos-2
- Databricks Genie
- Amazon Quick
- Amazon S3 Tables
- Model Context Protocol
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/automate-replenishment-with-mmf-databricks-genie-and-amazon-quick/
published_at: '2026-09-14'
---

## 概要

小売の在庫補充において、需要予測（Databricks MMF/Chronos-2）から需要急増の検知（Genieエージェント）、供給側の在庫照合と最安サプライヤー選定、発注実行（Amazon Quick Flows）までを一連のループとして自動化する構成を紹介する。判断ルールに当てはまらないケースのみ人間のレビューへエスカレーションする。

## 設計のポイント

- 予測と実行を別システムに置かず、共通の商品IDで需要（Databricks）と供給（S3 Tables）を判定時に突き合わせる
- Model Context Protocol経由でGenieエージェントの予測結果をAmazon Quickから参照し、データを一箇所にコピーしない
- ルールで対応できない需要急増のみを人間レビューへエスカレーションするヒューマン・イン・ザ・ループ設計
- 検知の閾値にノイズ除去のフロア（低ボリューム商品の除外）を設けて誤検知を抑える

## 使いどころ

- 需要予測はあるが発注実行までの『最後の1マイル』が手作業で滞留している小売・流通企業
- 複数サプライヤーからの動的な調達先選定を自動化したい場合
- フォーキャスト精度は十分でも、システム間の連携不足がボトルネックになっているケース
