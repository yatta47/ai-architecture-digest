---
type: announcement
title: 長時間稼働AIエージェント向け高速・低コスト推論モデル「Nemotron 3 Ultra」
title_original: NVIDIA Nemotron 3 Ultra Powers Faster, More Efficient Reasoning for Long-Running Agents
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- inference-optimization
- reasoning-computation-separation
components:
- NVIDIA Nemotron 3 Ultra
- NVIDIA NeMo RL
- NVIDIA NeMo Gym
- NVFP4
- LatentMoE
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/
published_at: '2026-06-25'
---

## 概要

NVIDIAは、550BパラメータのMixture-of-Expertsモデル「Nemotron 3 Ultra」(アクティブパラメータ55B)を公開した。長時間稼働するマルチエージェントワークフローのオーケストレーションに特化し、フロンティア級の推論精度を保ちながら同クラスの他のオープンモデル比で最大5倍のスループットと最大30%のコスト削減を実現する。ハイブリッドMamba-Transformer構造、NVFP4量子化、LatentMoE、Multi-Token Predictionといったアーキテクチャ革新に加え、10以上のドメイン特化教師モデルを用いたMulti-Teacher On-Policy Distillation(MOPD)による継続的な性能改善の仕組みを備える。

## 設計のポイント

- ハイブリッドMamba-Transformer構成により、長コンテキスト処理の効率性とエージェントが必要とする正確な事実リコールを両立させる。
- NVFP4量子化により単一チェックポイントをHopper/Blackwell/Ampereなど複数世代のGPUアーキテクチャ横断で動かし、BF16比最大5倍のスループットを実現する。
- LatentMoEによる効率的なエキスパートルーティングとMulti-Token Prediction(MTP)を組み合わせ、推論・コード生成・ツール呼び出しなど多様なワークロードでの生成速度を向上させる。
- Multi-Teacher On-Policy Distillation(MOPD)で10以上のドメイン特化教師モデルから密な報酬信号を非同期・反復的パイプラインで取り込み、モデルを継続的に専門化・改善する。

## 使いどころ

- 長時間稼働するマルチエージェントワークフローで、フロンティア級推論モデルをオーケストレーション役に、軽量モデルを高頻度な実行・検証・ツール呼び出し役に使い分けたい開発者。
- コーディングセッション全体での設計一貫性維持、大量の矛盾する調査根拠の統合、数千の制約にまたがるチップ設計検証など、高難度な推論を要するエージェントタスク。
- トークン消費とターン当たりコストを抑えつつ長文脈を扱う必要がある、コスト重視のエージェント基盤運用チーム。
- オープンなレシピ・重み・ライセンスを求め、独自ドメインへのファインチューニングや特化を行いたい企業・ソブリンAI開発パートナー。
