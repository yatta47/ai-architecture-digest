---
type: guidance
title: 帯域制約下でのIoT Edgeデバイスへの機械学習モデル差分配信と推論
title_original: Enable machine learning inference on an Azure IoT Edge device
industry: other
cloud:
- azure
patterns:
- inference-optimization
components:
- Azure IoT Edge
- Azure IoT Hub
- Azure Blob Storage
- Azure Machine Learning
- LiteRT
- ONNX
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/iot/machine-learning-inference-iot-edge
published_at: '2026-05-06'
---

## 概要

砂漠や洋上などネットワーク環境の悪い現場で稼働する風力・石油設備を想定し、LiteRT/ONNXの物体検出モデルをIoT Edgeモジュールとしてエッジ側にロードし、モジュールツインの仕組みでモデルだけを差分更新する構成を示す。エッジ側にモデルリポジトリを持たせることで、帯域の狭い回線でのモデル配布コストを抑えつつほぼゼロダウンタイムでモデルを切り替えられる。

## 設計のポイント

- AIモデル本体をDockerイメージから分離し、IoT Edgeモジュールツインでモデルファイルだけを差分ダウンロードさせることで帯域コストを削減する
- 推論モジュールをWeb APIとしても公開し、同じエッジ上の他アプリ/モジュールから再利用できるようにする
- エッジ側にローカルのモデルリポジトリを持たせ、モデル切り替え時のダウンタイムをほぼゼロにする

## 使いどころ

- 洋上風力発電設備や油田などネットワークが細く不安定な現場でのAI画像推論
- モデル更新のたびに数GBのコンテナイメージ全体を配信するコストを避けたいエッジAI運用チーム
