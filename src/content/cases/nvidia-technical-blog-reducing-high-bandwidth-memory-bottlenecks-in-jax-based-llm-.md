---
type: case
title: JAXのホストオフロードによるLLM学習のHBMボトルネック解消
title_original: Reducing High-Bandwidth Memory Bottlenecks in JAX-Based LLM Training with Host Offloading
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- llm-training-optimization
- cost-optimization
components:
- JAX
- MaxText
- XLA
- NVIDIA GB200 NVL72
- DeepSeek-V3
- Llama 3.1 405B
- NVIDIA Nsight Systems
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/reducing-high-bandwidth-memory-bottlenecks-in-jax-based-llm-training-with-host-offloading/
published_at: '2026-07-10'
---

## 概要

NVIDIAはJAXの学習フレームワークMaxTextで、活性化テンソルの一部をピン留めホストメモリへ退避する『ホストオフロード』により、GPUのHBM圧迫を軽減する手法を検証した。NVIDIA GB200 NVL72（Grace-Blackwell、NVLink-C2C 900GB/s）上でDeepSeek-V3 671BとLlama 3.1 405Bを用いた実験では、Latency Hiding Schedulerとパイプライン転送を併用することで活性化再計算より最大57%高いスループットを達成し、GPUメモリ不足で実行不可能だった大きなバッチ構成も実行可能にした。

## 設計のポイント

- 活性化再計算の代替として、フォワードパスで選択した活性化をピン留めホストメモリへ退避し、バックワードパスで転送し直すことでHBM使用量を削減する
- Grace-BlackwellのNVLink-C2C（900GB/s）のような高帯域CPU-GPU接続を前提に、転送をGPU計算とオーバーラップさせて初めて性能が出る
- XLAのカスタムスケジューリングフラグと専用コピーストリームでLatency Hiding Schedulerとパイプライン転送を組み合わせ、疎なMoEモデルほど効果が大きい
- NVIDIA Nsight Systemsでプロファイリングし、非同期データ転送とメモリ使用率が期待通りか検証する

## 使いどころ

- 大規模MoEモデル（DeepSeek-V3級）や高密度Transformer（Llama 3.1 405B級）をGPUメモリ制約なく学習したいチーム
- 活性化再計算によるスループット低下を避けつつ、より大きなバッチサイズ・シーケンス長で学習したい場合
- Grace BlackwellやVera Rubinなど高帯域CPU-GPU接続を持つプラットフォームでハードウェア性能を最大限引き出したいMLインフラ担当者
