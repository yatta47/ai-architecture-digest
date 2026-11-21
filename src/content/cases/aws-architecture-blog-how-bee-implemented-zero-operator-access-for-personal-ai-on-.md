---
type: case
title: 個人AIデバイスBeeのゼロオペレーターアクセス設計
title_original: How Bee implemented Zero Operator Access for personal AI on AWS
company: Bee (Amazon)
industry: cross-industry
cloud:
- aws
patterns:
- confidential-computing
- defense-in-depth
components:
- Amazon EC2
- AWS Nitro System
- Amazon Machine Image
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-bee-implemented-zero-operator-access-for-personal-ai-on-aws/
published_at: '2026-11-20'
---

## 概要

Beeは、装着型パーソナルAIが扱う健康や金融などの機微な会話を守るため、Beeの技術者やAmazon従業員、AWS運用者がデータにアクセスする手段を持たない構成を作った。核はEC2インスタンスのアテステーションに基づくキー解放である。

## 設計のポイント

- 検証済みソフトウェアが動くインスタンスにだけ、端末が復号鍵を渡す。
- アテステーションでは測れないネットワーク、ストレージ、組織権限の経路を別の制御で塞ぐ。
- 承認済みAMIやモデルを別チームの透明性サービスに保管し、監査できるようにする。

## 使いどころ

- 機微なAI処理で運用者から顧客データを隔離したいとき。
- クラウド事業者以外の社内運用者も脅威モデルに含めるとき。
