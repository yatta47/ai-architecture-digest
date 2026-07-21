---
type: guidance
title: JAX/MaxTextでNVFP4を使いBlackwell上のLLM事前学習を高速化するレシピ
title_original: Train Models Faster with JAX and MaxText Using NVFP4 on NVIDIA Blackwell
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- training-optimization
- cost-optimization
- llmops
components:
- JAX
- MaxText
- NVIDIA TransformerEngine
- NVIDIA GB200 Grace Blackwell Superchip
- NVIDIA GB300 Grace Blackwell Ultra Superchip
- Llama 3 8B
- Llama 3.1 405B
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/train-models-faster-with-jax-and-maxtext-using-nvfp4-on-nvidia-blackwell/
published_at: '2026-06-25'
---

## 概要

NVIDIAはJAX向けTransformerEngineとMaxTextに、4bit精度NVFP4を用いた事前学習レシピを実装し、NVIDIA BlackwellおよびRubinプラットフォーム上でFP8比最大1.73倍のスループット向上を達成した。16要素マイクロブロックスケーリングやランダムアダマール変換、2D重みスケーリング、確率的丸めなど5つの技術を組み合わせることで、Llama 3 8Bや405Bの事前学習において最終損失の測定可能な劣化なく高速化を実現している。

## 設計のポイント

- マイクロブロックを16要素に縮小し、E4M3ブロックスケールをper-tensor FP32スケールの下に階層化することで外れ値の影響とFP4量子化誤差を抑える。
- WGRAD向けGEMM入力のみにランダムアダマール変換を適用し、FPROP/DGRADには適用しないことで2Dスケールの整合性を保ちながら外れ値をガウス化する。
- 重みに16×16ブロック単位の2D FP8スケーリングを採用し、FPROPとその転置であるDGRADで同一スケールを共有して精度を安定させる。
- softmaxによる量子化誤差増幅が起きやすいAttentionブロックは高精度のまま残し、学習FLOPsの大半を占めるMLP層のGEMMのみをNVFP4量子化することで収束リスクを抑えつつ速度向上を最大化する。

## 使いどころ

- 数千アクセラレータ・数兆トークン規模のLLM事前学習で、精度劣化なくステップ時間を短縮したいAIインフラチーム。
- NVIDIA GB200/GB300などBlackwell世代GPU上でJAX/MaxTextベースの学習基盤を運用し、FP8からFP4への移行を検討しているMLエンジニア。
- 同じ計算予算でより多く・より大きなモデルを学習したいAIファクトリーや研究機関。
