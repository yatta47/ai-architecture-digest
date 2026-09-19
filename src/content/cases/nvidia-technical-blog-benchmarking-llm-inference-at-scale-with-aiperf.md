---
type: guidance
title: LLM推論をスケールでベンチマークするNVIDIA AIPerf
title_original: Benchmarking LLM Inference at Scale with AIPerf
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- eval
components:
- NVIDIA AIPerf
- vLLM
- NVIDIA DCGM
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/benchmarking-llm-inference-at-scale-with-aiperf/
published_at: '2026-09-18'
---

## 概要

NVIDIAは、GenAI-Perfの後継となるLLM推論ベンチマークツールAIPerfを公開した。マルチプロセスアーキテクチャによりクライアント自体がボトルネックにならない設計で、15種類以上のエンドポイントや実運用トレースを再現するデータセット、Poisson/ガンマ分布などの到着パターンを指定した負荷生成に対応し、TTFT・ITL・スループットをパーセンタイル付きで計測できる。

## 設計のポイント

- 単一プロセスのベンチマーカーがPythonのGILでボトルネックになる問題を避けるため、ワーカーとレコードプロセッサをZMQで協調させるマルチプロセス構成にする
- constant/Poisson/gammaなど到着パターンをバースト度付きで指定でき、本番トラフィックに近い負荷形状を再現できるようにする
- ShareGPTや実運用トレースリプレイ形式のデータセットを標準サポートし、合成負荷と実トラフィック再現の両方を同じツールで扱えるようにする
- ストリーミングを前提にTTFT/ITLをトークン単位で計測し、ベンチマーク結果の再現性を担保する

## 使いどころ

- 自前のcurl/asyncioスクリプトでは再現性のあるLLM推論性能評価ができず困っているエンジニア
- 本番トラフィックに近い負荷パターンでvLLM/SGLangなどの推論サーバーを検証したいチーム
- GPUテレメトリを含めた詳細な推論性能レポートが必要な場合
