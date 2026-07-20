---
type: guidance
title: 既存アプリにRTXセンサーシミュレーションを統合するOmniverse SDK「ovrtx」
title_original: Integrate NVIDIA Omniverse RTX Sensor Simulation Into Existing Apps
ai_relevant: false
company: NVIDIA
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/integrate-nvidia-omniverse-rtx-sensor-simulation-into-existing-apps/
published_at: '2026-07-20'
---

## 概要

NVIDIA Omniverseライブラリ群の一部であるovrtxは、OpenUSDシーンからカメラ・LiDAR・レーダーなどのRTXベースのセンサー出力をリアルタイムに生成する軽量なC/Python SDKである。ホストアプリケーションがレンダリングループやUI、データモデルの制御を保持したまま、CAD・Blender・PLM/PDM・ロボティクスなど既存のアプリケーションスタックへ組み込める設計になっている。ovphysx（物理演算）やovstage（共有USDシーンランタイム）など他のOmniverseライブラリと組み合わせることで、合成データ生成・デジタルツイン・物理AI検証向けのマルチモーダルなシミュレーションパイプラインを構築できる。
