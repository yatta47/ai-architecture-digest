---
type: case
title: Nemotron 3 UltraとACE-RTLエージェントによる高精度・低コストなRTLコーディング自動化
title_original: NVIDIA Nemotron 3 Ultra Leads Open Models on Accuracy and Efficiency in Agentic RTL Coding
company: NVIDIA
industry: manufacturing
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
- inference-optimization
components:
- NVIDIA Nemotron 3 Ultra
- ACE-RTL
- GLM 5.2
- Kimi K2.6
- CVDP benchmark
- Cadence
- Siemens
- Synopsys
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-leads-open-models-on-accuracy-and-efficiency-in-agentic-rtl-coding/
published_at: '2026-07-23'
---

## 概要

NVIDIAはACE-RTLエージェント（生成・テスト・振り返りを繰り返すgenerator/reflector/coordinator構成）とNemotron 3 Ultraモデルを組み合わせ、RTL設計向けのCVDPベンチマークで97.1%というオープンモデル最高水準の平均正答率を達成した。長文脈・RTL特化学習とハイブリッドMamba-AttentionのMoEアーキテクチャにより、GLM 5.2やKimi K2.6と比べて反復あたりのトークン消費を最大71%削減しつつ精度でも上回っている。これによりCadence、Siemens、Synopsysなど既存EDAツールへの実用的な統合が可能になるとしている。

## 設計のポイント

- generator・reflector・coordinatorの3役割に分離したエージェント構成にし、コーディネーターが過去の失敗履歴とフィードバックを踏まえて次の生成方針を決める
- シミュレーション/ツール検証のフィードバックを反復的に取り込むgenerate-test-reflectループにより単発生成より大幅に正答率を改善する
- 長文脈・RTL特化データで事前学習したモデルを使うことで、繰り返しのデバッグ文脈を保持したまま高スループットな推論を実現する
- 精度だけでなく反復あたりのトークン消費量も評価指標に加え、コストと正答率のトレードオフを可視化する

## 使いどころ

- 半導体設計チームがRTLコード生成・修正・デバッグを自動化してエンジニアの反復作業を減らしたい場合
- 既存のEDAツール（Cadence/Siemens/Synopsys）と連携したエージェント型コーディングパイプラインを構築したい場合
- 同じ計算予算でより多くのRTLタスクを試行したい、あるいは反復コストを抑えたいチーム
