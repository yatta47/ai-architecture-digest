---
type: guidance
title: NVIDIA Cosmosによる物理AI向けワールドモデルのシミュレーションと配備
title_original: Build World Models for Interactive Simulation with NVIDIA Cosmos
company: NVIDIA
industry: manufacturing
cloud: []
patterns:
- inference-optimization
components:
- NVIDIA Cosmos
- Cosmos NIM
- NVIDIA Alpamayo
- GR00T
- H200
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/build-world-models-for-interactive-simulation-with-nvidia-cosmos/
published_at: '2026-10-30'
---

## 概要

物理AI向けのワールド基盤モデルとツールであるCosmosについて、Cosmos 3 Nanoのレシピで自動運転・ロボット・手術のカメラ映像とLiDARを同期生成する方法を示す。NIMによる配備では量子化や投機的デコーディングなどでH200上で約2〜3倍の高速化とする。

## 設計のポイント

- 学習と推論のレシピ及びエージェントスキルを提供するフレームワークと、API提供のNIMとで開発と配備の課題を分けて扱う。
- 量子化、投機的デコーディング、KVキャッシュ対応ルーティングで推論を高速化する。
- GPUメモリ要件はモデルとタスクで変わる(Cosmos3-Nanoの生成はBF16で58GiB、FP8とオフロードで44GiB)。

## 使いどころ

- 自動運転やロボットのセンサーデータを合成して学習・検証したい開発者。
- ワールドモデルを本番のアプリケーションに配備するGPU構成を検討する場合。
