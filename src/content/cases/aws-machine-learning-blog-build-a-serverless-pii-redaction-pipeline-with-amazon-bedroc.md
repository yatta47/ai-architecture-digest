---
type: case
title: Bedrock Data Automationで作るサーバーレスPII自動黒塗りパイプライン
title_original: Build a serverless PII redaction pipeline with Amazon Bedrock Data Automation
company: AWS
industry: healthcare
cloud:
- aws
patterns:
- document-processing
- guardrails
components:
- Amazon Bedrock Data Automation
- AWS Step Functions
- AWS Lambda
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-serverless-pii-redaction-pipeline-with-amazon-bedrock-data-automation/
published_at: '2026-09-16'
---

## 概要

医療フォームや保険金請求書などスキャン文書に含まれるPIIを検出・黒塗りするため、Amazon Bedrock Data Automation(BDA)のカスタムブループリント機能とサーバーレスなバッチパイプラインを組み合わせた設計を紹介。BDAが自然言語指示に基づきフィールド単位で対象を抽出し、信頼度スコアとバウンディングボックス座標を使って後処理で黒塗りを適用する。

## 設計のポイント

- 何が機微情報かをフィールド単位の自然言語指示として定義し、患者名と医師名のように似た属性でも文脈で区別する
- inferenceType: explicitを使い、変換なしの原文抽出でフィールドをスコープする
- 抽出結果のバウンディングボックス座標を使い、PDFをPNG化した上で座標指定の黒塗りを後処理で適用する
- Step FunctionsとLambdaでBDA呼び出しからバッチ黒塗りまでをサーバーレスに構成する

## 使いどころ

- 医療・保険・金融など大量のスキャン文書からPIIを除去してから第三者共有する必要がある業務
- 文書レイアウトが多様でOCR+パターンマッチでは精度が出ない既存の黒塗り運用の置き換え
- カスタムMLモデルの学習・再学習なしにフィールド単位のPII検出を導入したいチーム
