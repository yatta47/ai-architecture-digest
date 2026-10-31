---
type: case
title: LTL貨物の請求例外処理をマルチエージェントで自動化した物流事例
title_original: How Worldwide Express automated freight exceptions with Amazon Bedrock
company: Worldwide Express
industry: logistics
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- decision-execution
components:
- Amazon Bedrock
- SpeedShip (TMS)
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-worldwide-express-automated-freight-exceptions-with-amazon-bedrock/
published_at: '2026-10-30'
---

## 概要

Worldwide ExpressはLTL運送の請求例外(明細不一致・価格差異・付帯料金)を手作業で処理しており、約1,500万ドルのキャッシュが滞留していた。AWSとLTMとともにBedrockベースのマルチエージェントをTMSのSpeedShipに組み込み、6か月でアクティブな例外を75%削減、入金までの期間を4週間短縮した。

## 設計のポイント

- 例外を種別ごとに分け、特定・原因調査・連絡・解決実行という人手の5工程をエージェントに分担させる。
- 既存のTMSに直接組み込み、解決の実行までを同じシステム内で完結させる。
- キャリアごとに異なるルールをエージェントが参照して判断し、外注による1件ずつの対応から置き換える。

## 使いどころ

- 三者照合の失敗が多く請求例外の滞留が資金繰りに響く物流・サプライチェーン企業。
- キャリアや取引先ごとの個別ルールに沿った突合・交渉業務を自動化したい経理部門。
