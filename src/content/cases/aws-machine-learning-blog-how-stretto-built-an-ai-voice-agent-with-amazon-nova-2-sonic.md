---
type: case
title: Nova 2 Sonicで破産相談の電話インテークを行う音声エージェント
title_original: How Stretto built an AI voice agent with Amazon Nova 2 Sonic
company: Stretto
industry: other
cloud:
- aws
patterns:
- voice-agent
- ai-agent
components:
- Amazon Nova 2 Sonic
- Amazon Bedrock
outcome:
  type: revenue
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-stretto-built-an-ai-voice-agent-with-amazon-nova-2-sonic/
published_at: '2026-11-18'
---

## 概要

StrettoはBankruptcy.comの入力フォームを、音声エージェントTaraによる電話インテークに置き換えた。Nova 2 Sonicの音声対音声モデルで会話しつつ債務情報を構造化し、弁護士が定めた規則でリードを選別する。

## 設計のポイント

- 長いフォームの離脱を、会話形式の聞き取りで避ける。
- 会話から構造化データをリアルタイムに抽出する。
- 弁護士が定義した規則でリードを分類する。
- 低遅延と割り込み処理を備えたS2Sモデルを採用する。

## 使いどころ

- 機微な情報を電話で聞き取る業務。
- 人手のインテークが採算に合わない領域。
