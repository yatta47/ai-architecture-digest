---
type: guidance
title: SFT・DPO・RFT・Vision FTを使い分けるファインチューニング手法ガイド
title_original: Fine-tuning guide
industry: cross-industry
cloud: []
patterns:
- fine-tuning
components:
- Fine-tuning API
- gpt-4.1
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/fine-tuning
published_at: '2025-07-18'
---

## 概要

OpenAIのファインチューニングガイドは、教師ありファインチューニング(SFT)・直接選好最適化(DPO)・強化ファインチューニング(RFT)・Vision fine-tuningという4手法を、対応モデルと適したユースケースとともに整理する。ファインチューニングは新しい知識を教える手段ではなく、既存知識の出力形式や振る舞いを最適化する手段と位置づけられる。

## 設計のポイント

- 分類やフォーマット固定などの明確な正解があるタスクにはSFT、優劣比較はできても正解が一つに決まらない主観的タスクにはDPOを選ぶ。
- ファインチューニングでプロンプトを短縮できれば、トークンコストとレイテンシの両方を削減できる。
- 新しいドメイン知識をモデルに教えたい場合はファインチューニングではなくRAGを使うという誤解を避ける。

## 使いどころ

- 同じ入力形式が繰り返される分類・フォーマット統一タスクで、プロンプト長を削減しコストを下げたい場合。
- 機微情報を毎回プロンプトに含めず、あらかじめモデルに振る舞いとして学習させたい場合。
