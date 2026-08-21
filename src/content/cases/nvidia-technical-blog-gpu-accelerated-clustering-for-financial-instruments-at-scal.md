---
type: case
title: GPU分散行列分解AdaptGrowで金融商品100万本のクラスタリングを数分で実行
title_original: GPU-Accelerated Clustering for Financial Instruments at Scale
industry: financial-services
cloud: []
patterns:
- gpu-accelerated-ml
components:
- NVIDIA GB200
- PyTorch Distributed
- NCCL
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/gpu-accelerated-clustering-for-financial-instruments-at-scale/
published_at: '2026-08-21'
---

## 概要

相関・テールディペンデンス行列から金融商品のクラスタとファクタ負荷量、構造変化点を検出するGPU加速の行列分解手法AdaptGrowを紹介する。メモリ効率の良いSymNMFで所要メモリを約1/5に抑え、単一GPUで10万銘柄、16ノードで100万銘柄までスケールし、100万銘柄でも2〜4分で収束する。

## 設計のポイント

- 行列分解にメモリ効率の良いSymNMFを採用し、必要ストレージを約20n²から4n²バイトへ削減する
- 固有スペクトルに応じてフルバッチAdaGradとブロック確率的SVRG勾配を適応的に切り替え、相関行列・TPDM両方の入力でソルバー再調整を不要にする
- 単一GPUから16ノードへの行方向シャーディングによる分散実装で、ハード・ソフトクラスタリングと安定性診断を両立する

## 使いどころ

- 大規模ポートフォリオでリスク集約や構成銘柄のクラスタリングを行うクオンツ運用チーム
- 相関構造の変化点（構造ブレイク）をリアルタイムに近い速度で検知したいリスク管理部門
- 既存のシングルGPU環境からマルチノードへのスケールアウトを見据えた基盤設計
