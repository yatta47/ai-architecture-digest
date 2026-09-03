---
type: case
title: Bedrock上のLLMでダッシュボード表示不良を検知するラストマイル品質監視基盤
title_original: How an AWS team detects dashboard content failures at scale using Amazon Bedrock
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- event-driven
- guardrails
- root-cause-analysis
components:
- Amazon Bedrock
- Amazon Quick
- Amazon EventBridge
- Amazon Redshift
- AWS Lambda
- Amazon Rekognition
- Amazon S3
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-an-aws-team-detects-dashboard-content-failures-at-scale-using-amazon-bedrock/
published_at: '2026-09-02'
---

## 概要

インフラ監視では検知できない、BIダッシュボードの表示内容そのものの欠落や数値の誤りを、LLMによる画面のビジュアル解析とエージェント型ブラウザ自動操作で検出するAWS社内の仕組みを解説する記事。5段階のサーバーレスパイプラインで、視覚的整合性と数値整合性を並行検証し、検知までの時間を最大72時間から1時間未満に短縮した。

## 設計のポイント

- インフラ監視・データ層検証ではカバーできない『表示されている内容そのもの』を検証する最後の砦のレイヤーを追加する
- ヘッドレスブラウザでスクリーンショットを取得し、Rekognitionでテキスト・数値を検知してマスクしてから保存し機密情報を残さない
- 視覚整合性チェックと数値整合性チェックの2つの並行検証メカニズムを同じ設計原則で構築する
- LLMに算術計算をさせず数値検証は別ロジックに任せることで誤検知を防ぐ運用上の工夫を行う

## 使いどころ

- 経営会議直前にダッシュボードの空欄や誤表示に気づきたくないBIチーム
- AIがダッシュボードデータを要約・ナラティブ生成する前段での数値正確性担保
- ユーザー報告に依存せず表示不良を自動検知したい大規模BI運用チーム
