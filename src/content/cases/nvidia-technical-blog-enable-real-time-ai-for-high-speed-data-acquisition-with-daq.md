---
type: case
title: 'DAQIRI: 高速データ収集をリアルタイムAI処理に直結する基盤'
title_original: Enable Real-Time AI for High-Speed Data Acquisition with DAQIRI
company: CERN
industry: public-sector
cloud:
- on-prem
patterns:
- out-of-band-inference
- event-driven
components:
- NVIDIA DAQIRI
- NVIDIA Holoscan
- NVIDIA TensorRT
- NVIDIA nvCOMP
- DPDK
- NVIDIA ConnectX
- NVIDIA DGX Spark
- NVIDIA IGX
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/enable-real-time-ai-for-high-speed-data-acquisition-with-daqiri/
published_at: '2026-07-09'
---

## 概要

従来の『収集・保存・解析』アーキテクチャは高レートなセンサー/検出器データに対応できず、多くのデータが破棄されてきた。NVIDIA DAQIRIはLinuxカーネルをバイパスしゼロコピーで検出器データをGPUへ直結するソフトウェア中心のパイプラインで、CERNのA-GHOSTプロジェクトではHL-LHCで従来破棄されていたデータストリームにCAEやTransformerベースモデルをリアルタイム適用する実証が進む。

## 設計のポイント

- DPDKによるカーネルバイパスとNICからGPUのDMAバッファへのゼロコピー転送で、大容量計装データをPCIe転送時間に近いレイテンシでGPUへ届ける
- YAML駆動の設定で、既存の計装機器を変更せずにフィルタリング・推論・圧縮・適応制御などのストリーム処理を組み替えられるようにする
- Holoscan・TensorRT・nvCOMPといったNVIDIAエコシステムだけでなく、独自の計装専用ソフトウェアへも直接ストリーミングできる柔軟性を持たせる

## 使いどころ

- 大型科学実験施設で従来は保存・解析できなかった高帯域検出器データにAIモデルをリアルタイム適用したい研究チーム
- 産業用CTスキャナーや高帯域SDRなど、高速データ取得装置にエッジAI処理を組み込みたい開発者
