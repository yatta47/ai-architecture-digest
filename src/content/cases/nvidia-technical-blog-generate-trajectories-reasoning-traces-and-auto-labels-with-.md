---
type: announcement
title: NVIDIAが自動運転向け推論VLA基盤モデル『Alpamayo 2 Super』を公開、軌道生成と推論トレースを1モデルに統合
title_original: Generate Trajectories, Reasoning Traces, and Auto-Labels with NVIDIA Alpamayo 2 Super
company: NVIDIA
industry: other
cloud: []
patterns:
- reasoning-computation-separation
- unified-runtime
- reinforcement-learning
- video-intelligence
components:
- NVIDIA Alpamayo 2 Super
- NVIDIA Cosmos 3 Super Reasoner
- NVIDIA Halos
- Hugging Face
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/
published_at: '2026-08-04'
---

## 概要

NVIDIAは340億パラメータのオープン推論VLA(Vision-Language-Action)モデル「Alpamayo 2 Super」を公開した。320億パラメータのCosmos 3 Super Reasonerと20億パラメータのdiffusionベースAction Expertを組み合わせ、強化学習でpost-trainingすることで、軌道生成・Chain-of-Causation推論トレース・メタアクション予測・グラウンディング付きVQA・自動ラベリングを単一の基盤モデルで提供する。最大7台のカメラによる360度知覚を備え、軌道予測やLingoQAなど複数のベンチマークで最高水準の性能を達成し、自動運転開発における効率的でスケーラブルな開発・評価を可能にする。

## 設計のポイント

- 推論を担う32BのCosmos 3 Super Reasonerとアクション生成を担う2BのdiffusionベースAction Expertを分離し、認識・推論とアクション生成の役割を明確に分担する設計
- 強化学習によるpost-trainingで軌道生成・推論・メタアクション予測・VQA・自動ラベリングを単一の基盤モデルに統合し、開発ワークフローの各段階で同じモデルを再利用可能にする
- 軌道と同時にChain-of-Causation推論トレースを出力することで、意思決定の根拠を可視化し、失敗が知覚・推論・行動生成のどこに起因するかを診断しやすくする
- OpenMDW-1.1という許諾的ライセンスでモデル重みと推論ノートブックをHugging FaceおよびGitHubに公開し、ファインチューニングや派生モデル作成、商用再配布を制限なく許可する

## 使いどころ

- 自動運転ポリシーのオフライン教師データ生成や評価用クリティックとして共通の基盤モデルを活用したいAV開発チーム
- 困難なシーンのキュレーションや、失敗原因が知覚・推論・行動生成のどこにあるかを切り分けたい開発者
- NVIDIA Halosなどの安全性検証ワークフローに推論トレースを組み込みたいチーム
- 自前の走行クリップに対してChain-of-Causation自動ラベルと2Dグラウンディングを付与し、データエンジンとして活用したい組織
