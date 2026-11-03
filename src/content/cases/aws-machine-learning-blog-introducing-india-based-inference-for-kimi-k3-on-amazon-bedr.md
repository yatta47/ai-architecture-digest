---
type: announcement
title: Amazon BedrockでKimi K3のインド国内推論が利用可能に
title_original: Introducing India-based inference for Kimi K3 on Amazon Bedrock
company: Moonshot AI
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- multi-model-routing
- document-processing
components:
- Amazon Bedrock
- Kimi K3
- Cross-Region inference
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-india-based-inference-for-kimi-k3-on-amazon-bedrock/
published_at: '2026-11-03'
---

## 概要

Amazon Bedrockがオープンウェイトのマルチモーダルモデル Kimi K3 のインド国内推論（ムンバイ/ハイデラバード）に対応した。グローバルとインドの推論プロファイルを使い分けてデータ所在要件を満たし、ヒンディー語文書のOCRと理解の例も示す。

## 設計のポイント

- 推論プロファイルIDで推論先リージョンの範囲を制御し、データレジデンシーを担保する
- マルチモーダルモデルで別OCR・翻訳サービス無しに多言語文書を読む
- プロンプトキャッシュでコストと応答時間を下げる（Ultrahumanは80%減・85%高速化と報告）

## 使いどころ

- インドの金融・公共でKYC文書をデジタル化したい場合
- データを国内に留めて最新のオープンモデルを使いたいチーム
