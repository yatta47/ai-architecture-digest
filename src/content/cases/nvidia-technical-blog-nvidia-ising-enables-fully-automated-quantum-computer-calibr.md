---
type: announcement
title: 量子プロセッサ校正を自動化するVLM「NVIDIA Ising Calibration 1.5」
title_original: NVIDIA Ising Enables Fully Automated Quantum Computer Calibration with Enhanced In-Context Learning
company: NVIDIA
industry: other
cloud:
- on-prem
patterns:
- ai-agent
- inference-optimization
- eval
components:
- NVIDIA Ising Calibration 1.5
- NVIDIA NeMo Agent Toolkit
- NVIDIA DGX Spark
- NVIDIA NIM
- QCalEval
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-ising-enables-fully-automated-quantum-computer-calibration-with-enhanced-in-context-learning/
published_at: '2026-07-27'
---

## 概要

NVIDIAは量子プロセッサの診断結果を解釈し校正方法を判断する31Bパラメータのビジョン言語モデル「Ising Calibration 1.5」を公開した。QCalEvalベンチマークでゼロショット・インコンテキスト学習の両方において他のオープンモデルを上回り、NVFP4量子化により単一GPUやDGX Sparkでのローカル展開を可能にした。重みやデータ、評価コードはOpenMDWライセンスで公開され、NeMo Agent Toolkitと組み合わせることで量子ビット校正の自動化エージェントを構築できる。

## 設計のポイント

- ゼロショットとインコンテキスト学習の両方を測定するQCalEvalベンチマークで性能を継続的に検証する
- NVFP4量子化版を別途用意し単一GPUやDGX Sparkなどローカル環境でのエージェント展開を可能にする
- モデル重み・学習データ・評価スクリプトをOpenMDWライセンスで全公開し独自QPU向けの再学習を可能にする
- NeMo Agent Toolkitと統合し診断結果の解釈から次アクションの推奨までを自動化するワークフローに組み込む

## 使いどころ

- 自前の量子ハードウェアラボでQPUの立ち上げ・再校正を自動化したいチーム
- クローズドモデルを使わずローカルGPUで校正エージェントを動かしたい研究機関
- 超伝導量子ビットやイオントラップなど複数モダリティの校正データを横断的に扱う開発者
