---
type: guidance
title: NVIDIA FLAREによる連合学習でマルチモーダルAIを複数拠点間で訓練する
title_original: Building Federated Multimodal AI Workflows with NVIDIA FLARE
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- federated-learning
- fine-tuning
components:
- NVIDIA FLARE
- FedUMM
- BLIP
- LoRA
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/building-federated-multimodal-ai-workflows-with-nvidia-flare/
published_at: '2026-08-19'
---

## 概要

生データを一元化できない複数拠点にまたがるVision-Language Model（VLM）の学習を、NVIDIA FLAREが連合学習として調整するアーキテクチャを解説する。William & MaryとNVIDIAが共同開発したFedUMMは、凍結したBLIPバックボーンの上に軽量なLoRAアダプタのみを交換する方式で、1ラウンドあたりの通信量を28.6GBから0.094GBへ削減しながら中央集約学習に近い性能を維持した。大きなモデル更新を扱う場合に備え、大容量オブジェクトの外部化・テンソルストリーミング・ディスクオフロード集約といったメモリ/帯域対策もFLAREに組み込まれている。

## 設計のポイント

- 何を連合させるか（フルモデル更新か、凍結バックボーン上の軽量アダプタのみか）を最初に決め、通信コストとモデル性能のトレードオフを設計判断として明示する
- クライアントの更新契約（何がローカルに留まり、何が拠点外に出て良いか、どのモデル部分を更新するか）を実装前に定義し、拠点ごとに異なるタスク/モダリティ混合にも対応できるようにする
- 大容量オブジェクトを軽量な参照に置き換えて転送する外部化と、Tensor Downloaderによるプル型のチャンク単位ストリーミングで、通信メッセージサイズとピークメモリを抑える
- サーバー側の集約時にクライアント数に比例してメモリが線形に増える問題を、受信した更新を一時ディスクに書き出すディスクオフロードで解消する

## 使いどころ

- 複数の医療機関や組織にまたがるデータを一元化せずにVLM/マルチモーダルモデルを学習したい場合
- 帯域やサーバーメモリの制約から、フルモデル更新の連合学習をそのまま運用できないチーム
- 拠点ごとにタスクやモダリティの構成が異なる、非対称なデータ分布を持つ連合学習ワークロード
