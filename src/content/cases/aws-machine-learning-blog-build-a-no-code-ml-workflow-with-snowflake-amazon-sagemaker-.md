---
type: guidance
title: Snowflake×SageMaker Canvas×Amazon Quickでコード不要のML基盤を構築（第1回）
title_original: Build a no-code ML workflow with Snowflake, Amazon SageMaker Canvas and Amazon Quick – Part 1
industry: healthcare
cloud:
- aws
patterns:
- data-federation
components:
- Snowflake
- Amazon SageMaker Canvas
- Amazon Quick
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-no-code-ml-workflow-with-snowflake-amazon-sagemaker-canvas-and-amazon-quick-part-1-setting-up-your-snowflake-environment/
published_at: '2026-08-20'
---

## 概要

Snowflakeに蓄積された販売・在庫・患者接点等のデータを、コードを書かずにAmazon SageMaker Canvasで特徴量作成・モデル構築まで行い、Amazon Quickでダッシュボード化する3部構成の第1回。ある医療機関の不正検知ユースケースを題材に、まずAWSアカウントとSnowflake環境のセットアップを解説する。

## 設計のポイント

- データサイエンスチームを介さず、業務分析担当者がSnowflakeのデータから直接モデルを構築できるようノーコードツールを選定する
- データ取得（Snowflake）・モデリング（SageMaker Canvas）・可視化（Amazon Quick）を3段階に分け、段階ごとにエンタープライズのセキュリティ・ガバナンスを維持する
- 実データ移動を最小化する接続構成をシリーズ第1回のセットアップ段階で先に固める

## 使いどころ

- データサイエンスリソースが限られる中で予測モデルを内製化したい業務部門
- Snowflakeに蓄積された医療・小売データを予測分析に活用したい組織
- モデル構築から可視化までを一気通貫でノーコード化したいチーム
