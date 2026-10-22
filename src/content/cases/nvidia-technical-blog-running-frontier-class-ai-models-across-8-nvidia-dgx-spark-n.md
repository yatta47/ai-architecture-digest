---
type: announcement
title: DGX Spark 8ノード構成の公式対応と、フロンティア級モデルのローカル実行
title_original: Running Frontier-Class AI Models Across 8 NVIDIA DGX Spark Nodes
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- multi-model-routing
- parallel-execution
components:
- NVIDIA DGX Spark
- NVIDIA Sync
- NVIDIA NeMo Switchyard
- RoCEnante
- vLLM
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/
published_at: '2026-10-21'
---

## 概要

NVIDIAはDGX Sparkの8ノードクラスタを公式対応とし、統合メモリを1TBに拡大して、フロンティア級モデルのローカル実行を可能にした。Spark向け集合通信バックエンドRoCEnanteでテンソル並列デコードを高速化し、NeMo Switchyardでモデルプール間のリクエストを振り分ける。

## 設計のポイント

- スイッチ接続ではテンソル並列デコードの全縮約遅延を減らす専用バックエンドを使い、8ノードで4.43倍の高速化を得る。
- 共有クラスタ上でモデルプールを分け、リクエストをSwitchyardで振り分けて総スループットを上げる。
- トポロジー（スイッチ型・リング型）をコストと柔軟性で使い分ける。

## 使いどころ

- 手元の環境で巨大モデルや複数エージェントの負荷を試したい開発者。
- 小規模なモデルの事前学習をローカルで高いスケール効率で回したいチーム。
