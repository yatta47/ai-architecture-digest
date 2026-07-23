---
type: guidance
title: Supervised Fine-tuningでモデルの出力スタイル・挙動を訓練データでカスタマイズ
title_original: Supervised fine-tuning
industry: cross-industry
cloud: []
patterns:
- fine-tuning
components:
- gpt-4.1
- gpt-4.1-mini
- gpt-4.1-nano
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/supervised-fine-tuning
published_at: '2025-07-21'
---

## 概要

Supervised fine-tuning (SFT) は正解例を与えてモデルの応答スタイルや挙動を訓練する手法で、分類・ニュアンスの翻訳・特定フォーマットでの生成・指示追従の失敗修正に向く。データセット構築→アップロード→ファインチューニングジョブ作成→評価という4ステップで構成され、着手前にまずevalsを整備しておくことが推奨される。

## 設計のポイント

- fine-tuningの効果を判定するため、着手前にベースモデルとの比較評価の仕組み（evals）を先に用意しておく。
- 学習データはJSONL形式・chat completions形式で、最低10行、実用的には50〜100件程度から始める。

## 使いどころ

- 特定フォーマットでの出力や指示追従の失敗を安定して修正したい場合。
- ニュアンスの翻訳や分類など、プロンプトだけでは再現しづらいスタイルをモデルに学習させたい場合。
