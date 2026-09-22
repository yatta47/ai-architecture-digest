---
type: announcement
title: Claude Opus 5.5がAmazon Bedrockで利用可能に
title_original: Claude Opus 5.5 is now available on AWS
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- cost-optimization
components:
- Amazon Bedrock
- Claude Opus 5.5
- AWS SDK
- Amazon Bedrock Converse API
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/claude-opus-5-5-is-now-available-on-aws/
published_at: '2026-09-22'
---

## 概要

Claude 5.5ファミリー最初のモデルであるClaude Opus 5.5がAmazon BedrockとClaude Platform on AWSで利用可能になった。トークン効率と価格改定によりタスクあたりの平均コストが下がり、常時オンの適応的思考とeffortパラメータによる推論量の制御が可能になっている。

## 設計のポイント

- 推論量を手動のthinking budgetではなくeffortパラメータで制御できるようにした
- キャッシュ読み取りの大幅値下げとトークン効率化でエージェント的な長時間タスクのコストを抑えた
- 生物・サイバーセキュリティ・AI開発領域の安全性分類器をOpusモデルとして初めて搭載した
- US/EU/AU/JP/Globalの推論プロファイルとbedrock-runtime/bedrock-mantle両対応でリージョン選択の柔軟性を確保した

## 使いどころ

- 長時間実行するエージェント的なソフトウェア開発タスクを任せたいチーム
- レビューや修正の手間を減らしたい長文レポート・ドキュメント作成業務
- 推論コストをタスクの難易度に応じて動的に調整したい運用
