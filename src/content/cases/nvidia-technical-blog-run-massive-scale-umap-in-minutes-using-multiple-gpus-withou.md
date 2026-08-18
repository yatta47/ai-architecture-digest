---
type: guidance
title: cuML/cuVSによるマルチGPU UMAPの大規模ベクトル処理
title_original: Run Massive-Scale UMAP in Minutes Using Multiple GPUs—Without Losing Accuracy
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- vector-search-scaling
- cost-optimization
components:
- NVIDIA cuML
- NVIDIA cuVS
- NVIDIA H100
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/run-massive-scale-umap-in-minutes-using-multiple-gpus-without-losing-accuracy/
published_at: '2026-08-18'
---

## 概要

NVIDIAはcuML/cuVS 25.06でUMAPの全近傍kNNグラフ構築をマルチGPUに対応させ、データセットをバランスの取れたクラスタに分割して各GPUが独立にローカルkNNグラフを計算・統合することで全対全通信を回避した。MIRACLやWikipediaデータセットでの検証では、H100 GPU8基を用いて870GBのベクトルデータを8分で処理し、CPU実行に対し最大74倍の高速化を達成しつつ埋め込み品質(信頼性スコア)を維持した。

## 設計のポイント

- データセットをknn_n_clustersで指定するバランスの取れたクラスタに分割し、各GPUが担当クラスタを独立に処理することで全対全通信を避け、複数GPUへ自然にスケールさせる
- knn_overlap_factorでクラスタ境界をまたぐ近傍関係の精度を調整し、計算時間・メモリ使用量と埋め込み品質のトレードオフを制御可能にする
- 全近傍グラフ構築ステップ(cuVSのall-neighbors API)をUMAPのtransform()だけでなくtrainステップからも切り離して再利用可能なAPIとして公開し、大規模ベクトル処理の他用途にも転用できるようにする

## 使いどころ

- 数千万〜数億ベクトル規模のデータに対して探索的データ分析やトピックモデリング、シングルセル解析を反復的に(パラメータを変えながら)実行したいデータサイエンスチーム
- 従来はCPUや単一GPUでは時間・日単位かかっていたUMAP埋め込み計算を、分単位のインタラクティブな探索に変えたい大規模ベクトルデータ基盤
- 既存のcuML単一GPU UMAPワークフローをそのまま拡張し、追加のコード変更を最小限にマルチGPU化したい場合
