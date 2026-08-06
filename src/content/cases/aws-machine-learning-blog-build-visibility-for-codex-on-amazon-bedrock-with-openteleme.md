---
type: guidance
title: ローカルCodexの利用状況をOpenTelemetry経由でCloudWatchに集約する可視化パターン
title_original: Build visibility for Codex on Amazon Bedrock with OpenTelemetry and Amazon CloudWatch
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- cost-optimization
components:
- Codex
- Amazon Bedrock
- Amazon CloudWatch
- AWS IAM Identity Center
- OpenTelemetry
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-visibility-for-codex-on-amazon-bedrock-with-opentelemetry-and-amazon-cloudwatch/
published_at: '2026-08-06'
---

## 概要

開発者ローカルで動くCodexコーディングエージェントの利用実態を、集中プロキシを追加せずに可視化する構成を紹介。各開発者ワークステーション上のOTelコレクターがCodexのメトリクスを部門・チーム・コストセンターなどの組織属性で拡張し、SigV4署名付きでCloudWatchへ送信する。ダッシュボードは採用状況や消費集中度の判断材料になるが、正式な課金額はCURの参照が必要と明記している。

## 設計のポイント

- モデル推論経路に集中プロキシを挟まず、各開発者端末のローカルコレクターがメトリクスを収集・送信する非侵襲な構成にする
- IAM Identity Centerの認証情報をテレメトリ送信にも流用し、モデルアクセスと可観測性で同一のアイデンティティを使う
- トークン数などの利用量メトリクスと、CUR 2.0による課金確定額を明確に分離し、見積りと実額を混同しない
- プレースホルダー値をディメンションとして送らず、取得できない組織属性はブロックごと省略して低品質な時系列を作らない

## 使いどころ

- コーディングエージェントの全社導入を判断する技術リーダーが、部門横断の採用状況や消費集中度を把握したい場合
- コストセンター別のshowbackやチャージバックを行いたいプラットフォームチームの運用可視化として
- エージェントの応答遅延や失敗率から、モデルアクセスやネットワークの不調を切り分けたい運用チームとして
