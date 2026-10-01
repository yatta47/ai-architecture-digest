---
type: case
title: Amazon Paymentsの獲得ファネル全体を最適化するマルチ目的コンテキスチュアルバンディット
title_original: Uplifting conversion across the acquisition funnel with personalization using contextual bandits on AWS
company: Amazon Payments
industry: financial-services
cloud:
- aws
patterns:
- reinforcement-learning
- generative-recommendation
components:
- Amazon SageMaker AI
- Amazon Bedrock
- LinUCB
outcome:
  type: revenue
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/uplifting-conversion-across-the-acquisition-funnel-with-personalization-using-contextual-bandits-on-aws/
published_at: '2026-10-01'
---

## 概要

生成AIで大量に作れるパーソナライズ済みコンテンツの「どれを誰に見せるか」という選択問題に対し、Amazon PaymentsはSageMaker AI上でマルチ目的のコンテキスチュアルバンディット(LinUCB)を適用した。申込開始・申込完了・承認の各段階にLinUCBモデルを置きUCBスコアを線形結合してファネル全体を最適化し、7週間のA/Bテストで一方の顧客層は最終ファネル転換率が相対で高い1桁%向上、もう一方は改善なしだった(原因はモデルでなくコンテンツ)。

## 設計のポイント

- 顧客を固定セグメントでなく行動シグナルの特徴ベクトルで表現し、少ないトラフィックでも未知の訪問者に汎化できるLinUCBを採用した。
- UCBの決定論的な選択ルールにより、各インプレッションの判断を監査・再現できるようにした。
- 開始・提出・承認の各段階に別のLinUCBモデルを置き、UCBスコアを重み付き線形結合することで、ある段階の最適化が他段階を悪化させるシーソー問題と承認シグナルの希薄さを回避した。
- エンティティIDは推薦結果のルーティングにのみ使い、モデル入力にはしない。

## 使いどころ

- 生成AIでコンテンツのバリエーションが急増し、A/B/nテストでは学習が追いつかないマーケティング・獲得施策。
- 承認など成果が稀で遅れて得られる多段ファネルの最適化。
- 意思決定の説明可能性・再現性が求められる金融系サービスのパーソナライズ。
