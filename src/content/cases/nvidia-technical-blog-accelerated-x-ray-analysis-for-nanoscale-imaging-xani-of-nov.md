---
type: case
title: X線自由電子レーザー(XFEL)データ解析をGPUで9カ月から4時間に短縮するXANIワークフロー
title_original: Accelerated X-Ray Analysis for Nanoscale Imaging (XANI) of Novel Materials
ai_relevant: false
company: NVIDIA
industry: public-sector
cloud:
- on-prem
patterns: []
components: []
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/accelerated-x-ray-analysis-for-nanoscale-imaging-xani-of-novel-materials/
published_at: '2026-06-11'
---

## 概要

X線自由電子レーザー(XFEL)施設は毎秒最大100万ショット・3500万画素のカメラで原子・電子レベルの超高速現象を捉えるが、従来のCPUベース単一ノードPythonパイプラインでは42TBのデータ解析に9カ月を要していた。NVIDIAのXANIワークフローはcuPyNumericによるGPU分散計算とGPUDirect Storage・マルチスレッドHDF5によるI/O最適化により、32基のNVIDIA GB200 Grace Blackwellスーパーチップ上で同じデータを4時間未満（GPU単体で43倍、64GPUで1000倍高速化）で解析可能にし、量子材料など複数分野の研究コミュニティに採用されている。
