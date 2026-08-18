---
type: case
title: 量子化認識蒸留(QAD)によるNemotron 3.5 LightningのNVFP4圧縮
title_original: Developing Nemotron 3.5 Lightning NVFP4 with QAD Using NVIDIA Model Optimizer
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- fine-tuning
- llmops
components:
- NVIDIA Model Optimizer
- Megatron-Bridge
- Nemotron 3.5 Lightning
- NVIDIA DGX B300
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/developing-nemotron-3-5-lightning-nvfp4-with-qad-using-nvidia-model-optimizer/
published_at: '2026-08-17'
---

## 概要

NVIDIAは量子化認識蒸留(QAD)を用いて、Nemotron 3.5 LightningモデルをBF16からNVFP4(W4A16)へ積極的に量子化しつつ精度低下を抑えるパイプラインを構築した。PTQで生成した量子化学生モデルを、凍結したフル精度教師モデルとのKLダイバージェンス損失で再学習することで、PTQ単体を上回る精度回復を実現している。結果としてモデルサイズを66GBから22GBに圧縮し、スループットを最大4倍向上させた。

## 設計のポイント

- PTQで先に積極的な量子化(W4A16/NVFP4)を行い、精度回復はQADの学習ステージに委ねることでサイズ・遅延の削減幅を最大化する
- 凍結したBF16教師モデルに対しKLダイバージェンス損失で学生モデルを蒸留し、フォワードパスに疑似量子化を組み込んで推論時のノイズに適応させる
- lm_headはW4A16(faithful lm_head)で量子化しつつAttention射影層はBF16に残すなど、レイヤーごとに量子化戦略を使い分ける
- キャリブレーション手法(max-calibrated vs MSEベース)によって動的スケールQADと固定スケールQADを使い分ける

## 使いどころ

- 推論スループットとメモリ効率を最大化したいがPTQ単体では精度劣化が許容できない大規模LLMのデプロイ
- GPUメモリが限られる環境で大規模モデルを圧縮しつつエージェント/コーディング系ベンチマークの精度を維持したい場合
- 既存のBF16チェックポイントを持つチームがNVIDIA Model OptimizerとMegatron-Bridgeで再現可能な量子化ワークフローを構築したい場合
