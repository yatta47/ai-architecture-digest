---
type: guidance
title: Dynamo-TritonでHSTU生成推薦モデルを配信する構成
title_original: Deploying an HSTU Generative Recommender with NVIDIA Dynamo-Triton
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- generative-recommendation
- inference-optimization
components:
- NVIDIA Dynamo-Triton
- HSTU
- PyTorch AOTI
- FlexKV
- NVIDIA recsys-examples
- NV embedding cache
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/deploying-an-hstu-generative-recommender-with-nvidia-dynamo-triton/
published_at: '2026-09-30'
---

## 概要

HSTUベースの生成推薦モデルをPyTorch開発から本番推論へ移す流れを示す記事。AOTIでC++向けにコンパイルし、FlexKVによるKVキャッシュで長い利用者履歴の再計算を避ける。キャッシュヒット率100%、バッチ8で8層モデルが最大5.93倍低遅延になった。

## 設計のポイント

- PyTorch AOTIでモデルをネイティブC++成果物にコンパイルし、別ランタイム向けの書き直しなしでDynamo-Tritonから配信する。
- 利用者履歴のKV状態をGPUとホストの階層キャッシュに保持し、再計算を減らす。
- GPUキャッシュが逼迫した際はLRU方式で古い利用者を退避する。
- PythonとネイティブC++の双方で成果物を検証してから配信する。

## 使いどころ

- 履歴が長い大規模パーソナライズ推薦の低遅延サービング。
- 従来の検索・ランキング多段構成を系列モデルに置き換える検討。
- 再訪ユーザーが多く、KVキャッシュが効く推論ワークロード。
