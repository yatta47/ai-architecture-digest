---
type: guidance
title: AssemblerからJavaへのメインフレーム近代化を、COBOLを中間段にしたAI多段変換で行う手法
title_original: Modernizing mainframe Assembler to Java using Amazon Bedrock and AWS Transform
industry: cross-industry
cloud:
- aws
patterns:
- spec-driven-development
- human-in-the-loop
- document-processing
components:
- Amazon Bedrock
- AWS Transform
- Kiro IDE
- Amazon S3
- Amazon Bedrock Converse API
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/modernizing-mainframe-assembler-to-java-using-amazon-bedrock-and-aws-transform/
published_at: '2026-11-16'
---

## 概要

メインフレームのAssemblerプログラムをJava Spring Bootへ移行するため、業務ルール抽出・仕様化・Assembler→COBOL変換・検証・COBOL→Java変換の5段階手法を示す。中間にCOBOLを挟み、SMEが検証できる形でビジネスロジックを保全する。

## 設計のポイント

- 直接変換せず中間COBOLを挟み、人が読める形でSMEが検証できるチェックポイントを作る
- 業務ルール抽出(BRE)の品質が後続精度を左右するため、ドキュメントやデータ辞書を文脈として与える
- temperature 0でConverse API経由のバッチ実行とし、各段の出力をS3に保存して次段の入力にする
- 機能等価テストを各段に置き、サニタイズしたテストデータで検証する

## 使いどころ

- Assembler資産を抱え、継承者が減っている金融・保険・航空の基幹バッチ刷新
- レガシー移行でビジネスルール欠落のリスクを抑えたい場面
