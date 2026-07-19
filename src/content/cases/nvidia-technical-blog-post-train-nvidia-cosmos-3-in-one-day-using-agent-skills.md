---
type: case
title: TAO Agent SkillsによるNVIDIA Cosmos 3の1日ポストトレーニング
title_original: Post-Train NVIDIA Cosmos 3 in One Day Using Agent Skills
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- ai-agent
- reasoning-computation-separation
- inference-optimization
components:
- NVIDIA Cosmos 3 Nano
- NVIDIA TAO
- LoRA
- TAO AutoML
- Cosmos 3 Reasoner NIM
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/post-train-nvidia-cosmos-3-in-one-day-using-agent-skills/
published_at: '2026-07-13'
---

## 概要

NVIDIA Cosmos 3 Nano(視覚言語推論モデル)をNVIDIA TAOのagent skillsとLoRAで自動ポストトレーニングし、動画質問応答タスクのゼロショット精度54.41%を1回の学習で87.14%まで押し上げ、TAO AutoMLによるハイパーパラメータスイープで93.35%まで改善した。コーディングエージェントが数個の自然言語プロンプトだけでデータ整形・コンテナ起動・評価・スイープを自動実行し、従来数日かかっていた作業を1日に圧縮した。

## 設計のポイント

- LoRAはベースモデルの重みを凍結し低ランク行列のみ学習するため、フルパラメータSFTに比べ約7分の1のGPU時間で済み、1日での学習完了を可能にしている。
- TAO agent skillsがフレームワーク詳細・ランチャー挙動・設定構造・データ読み込み・評価手順といったタスク固有知識をパッケージ化し、コーディングエージェントが手作業でコマンドや設定ファイルを組み立てずに正しい手順を推論できるようにしている。
- Cosmos 3のMoT(mixture-of-transformers)アーキテクチャは推論用のReasonerタワーと生成用のGeneratorタワーに分離されており、TAO agent skillsはポストトレーニングをReasoner側の重みだけに自動的に絞り込む。
- 学習済みLoRAアダプタはCosmos 3 Reasoner NIMを通じてOpenAI互換エンドポイントとしてそのまま配信でき、CUDA依存やインフラ構築の複雑さを回避して本番投入までを短縮している。

## 使いどころ

- 特有のカメラアングルやエッジケースを持つ現場向けに、視覚言語基盤モデルを迅速にドメイン適応させたいチーム。
- データ整形・ベースライン評価・ハイパーパラメータ探索といった多日にわたるエンジニアリング作業を、コーディングエージェントとAutoMLで1日に圧縮したい場合。
- ポストトレーニング後のモデルをインフラ構築なしに素早く本番のOpenAI互換エンドポイントとして提供したいチーム。
