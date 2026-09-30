---
type: announcement
title: インド国内に推論を閉じるBedrock上のClaude地理的クロスリージョン推論
title_original: Amazon Bedrock expands Claude model availability to in-country inferencing in India
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- llmops
components:
- Amazon Bedrock
- Claude Opus 5
- Claude Sonnet 5
- Claude Haiku 4.5
- Amazon Bedrock Guardrails
- Amazon CloudWatch
- AWS CloudTrail
- AWS Cost Explorer
- Anthropic SDK
- Boto3
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-expands-claude-model-availability-to-india-cross-region-inference/
published_at: '2026-09-30'
---

## 概要

Amazon BedrockでClaude Opus 5・Sonnet 5・Haiku 4.5がインドの地理的クロスリージョン推論プロファイルで利用可能になり、推論をムンバイ（ap-south-1）とハイデラバード（ap-south-2）の間に限定できるようになった。単一リージョンの容量に縛られずピーク時のスループットを確保しつつ、課金・クォータ・ログはソースリージョンに集約される。Messages API、InvokeModel、Converse APIからの呼び出し方法も示す。

## 設計のポイント

- 地理的推論プロファイル（in.プレフィックスのモデルID）を使い、データ処理を国内の複数リージョンに限定しながら容量をプールする。
- 課金・クォータ・CloudWatch/CloudTrailログはソースリージョンに集約されるため、監視を一箇所で行える。
- 既定でモデル入出力を保存しないゼロデータ保持モデルを前提にデータ所在要件を設計する。

## 使いどころ

- データをインド国内で処理する必要がある企業の生成AIアプリケーション。
- トラフィックピーク時にも安定したスループットが必要なインド向けサービス。
