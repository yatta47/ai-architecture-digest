---
type: guidance
title: '取引基盤モデルを自作する: 金融インテリジェンスのための事前学習'
title_original: Build Your Own Transaction Foundation Model for Financial Intelligence
industry: financial-services
cloud:
- on-prem
patterns:
- tabular-foundation-model
- fine-tuning
components:
- NVIDIA CUDA-X cuDF
- NVIDIA CUDA-X cuML
- NVIDIA NeMo AutoModel
- XGBoost
- IBM TabFormer
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/build-your-own-transaction-foundation-model-for-financial-intelligence/
published_at: '2026-07-09'
---

## 概要

Stripe・Nubank・Visa・Mastercardなど金融各社が取引基盤モデルで不正検知や与信スコアリングを本番改善している流れを受け、NVIDIAはcuDF/cuMLによるGPUデータ処理、独自ドメイントークナイザ、NeMo AutoModelによるLlamaベースのゼロからの事前学習、埋め込み抽出、下流分類器強化までの一連のワークフローを公開した。IBM TabFormer不正検知データセットで、強力なXGBoostベースラインに対しAverage Precisionが約50%向上した。

## 設計のポイント

- 汎用LLMのBPEトークナイザではなく、取引ごとに約12個の意味トークンに変換する独自ドメイントークナイザで語彙数を6,251まで圧縮しトークン効率を3倍以上にする
- デコーダのみのLlamaベースモデルを取引シーケンスに対しゼロから事前学習し、自己注意で離れたイベント間の関係(旅行パターン後の異常な少額決済連続など)を学習させる
- クラス不均衡が強いタスクではROC-AUCではなくAverage Precisionを主要指標として全ての改善を評価する
- 事前学習済み埋め込みを既存の表形式特徴と組み合わせて下流分類器に投入し、単体の特徴量エンジニアリングを補完する

## 使いどころ

- 大量の取引履歴を持つ金融機関が不正検知・与信・LTV予測など複数タスクに転用できる基盤モデルを内製したい場合
- 手作業のルールベース特徴量が限界を迎えているタスクでシーケンシャルな行動パターンを学習させたいデータサイエンスチーム
