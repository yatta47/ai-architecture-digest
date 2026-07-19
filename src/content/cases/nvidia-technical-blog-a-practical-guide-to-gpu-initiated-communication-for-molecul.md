---
type: case
title: GROMACS分子動力学シミュレーションをGPU起動通信(NVSHMEM)で高速化
title_original: A Practical Guide to GPU-Initiated Communication for Molecular Dynamics at Scale
ai_relevant: false
company: NVIDIA
industry: other
cloud:
- on-prem
patterns: []
components: []
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/a-practical-guide-to-gpu-initiated-communication-for-molecular-dynamics-at-scale/
published_at: '2026-07-09'
---

## 概要

分子動力学シミュレーションパッケージGROMACSは、CPUがGPU間のハロー交換通信を仲介する従来のMPI方式により、1タイムステップあたり最大12回のCPU-GPU同期が発生しスケーラビリティを制限していた。NVIDIA NVSHMEMを用いたGPU起動のリモートメモリアクセスでCPUを通信のクリティカルパスから排除し、依存関係を考慮したカーネル融合とインターコネクト対応の転送ロジックにより、NVIDIA EosおよびGB200 NVL72クラスタでGPU対応MPI比最大2倍のストロングスケーリング性能を達成した。
