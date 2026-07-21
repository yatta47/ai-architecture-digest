---
type: guidance
title: スキャンした紙のカルテをFHIR準拠データへ自動変換するイベント駆動パイプライン
title_original: Automate medical record digitization with Amazon Bedrock Data Automation and AWS HealthLake
company: AWS
industry: healthcare
cloud:
- aws
patterns:
- document-processing
- event-driven
components:
- Amazon Bedrock Data Automation
- AWS Lambda
- Amazon S3
- AWS HealthLake
- AWS CloudFormation
- Amazon CloudWatch
- AWS CloudTrail
- AWS KMS
outcome:
  type: productivity
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/automate-medical-record-digitization-with-amazon-bedrock-data-automation-and-aws-healthlake/
published_at: '2026-06-09'
---

## 概要

紙のカルテがモダンな臨床システムと連携せず、手作業のデータ入力に多額のコストがかかっている課題に対し、AWSはAmazon Bedrock Data AutomationとAWS HealthLakeを組み合わせた、スキャンPDFからFHIR R4準拠データへの変換パイプラインのリファレンス構成を公開した。S3へのPDFアップロードをトリガーに、Bedrock Data Automationが独自MLモデルなしで50超の臨床フィールドを信頼度スコア付きで抽出し、LambdaがそれをFHIR R4形式に変換してHealthLakeに取り込むことで、検証・索引付け済みのクエリ可能なFHIR APIエンドポイントとして提供する。CloudFormationにより約15〜20分でデプロイできる一方、実PHIを扱う本番利用には追加のHIPAA対応が必要な、合成データ向けのデモンストレーション用サンプルと位置付けられている。

## 設計のポイント

- S3のイベント通知を起点に抽出Lambda→FHIR変換Lambdaと処理を連鎖させ、スケジューラやポーリングを排した完全イベント駆動の構成にしている。
- Amazon Bedrock Data Automationにカスタム医療ブループリント(50超の臨床フィールド定義)を与えることで、テンプレート作成や独自MLモデルの学習なしに構造化抽出を実現している。
- 抽出フィールドごとに信頼度スコアを返し、FHIR変換前にしきい値でバリデーションすることでデータ品質を担保している。
- 抽出用Lambdaと変換用Lambdaを役割ごとに疎結合な2関数に分割し、各段階を独立してスケール・置換可能な構成にしている。

## 使いどころ

- 紙のカルテが電子カルテ・FHIR対応システムと連携しておらず、患者の全既往歴を参照できずに診療している医療機関。
- 手作業でのデータ入力コストを削減しつつ、大量のスキャン文書を構造化データへ変換したい医療IT組織。
- FHIR R4準拠のデータストアとAPIエンドポイントを求める、相互運用性が必要な医療情報基盤。
- 実PHIを扱う前段階として、合成データでパイプラインのPoC・検証を行いたいチーム(本番投入には追加のHIPAA対応が必要)。
