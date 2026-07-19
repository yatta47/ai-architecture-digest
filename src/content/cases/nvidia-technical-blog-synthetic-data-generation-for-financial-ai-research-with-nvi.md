---
type: case
title: 金融ニュース見出しの合成データを反復生成・重複排除するNeMoパイプライン
title_original: Synthetic Data Generation for Financial AI Research with NVIDIA NeMo
company: NVIDIA
industry: financial-services
cloud:
- on-prem
patterns:
- synthetic-data-generation
- llmops
- fine-tuning
- inference-optimization
components:
- NVIDIA NeMo Data Designer
- NVIDIA NeMo Curator
- NVIDIA Nemotron-3-Nano-30B-A3B
- vLLM
- NVIDIA B200
- SLURM
- Ray
- sentence-transformers
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/synthetic-data-generation-for-financial-ai-research-with-nvidia-nemo/
published_at: '2026-07-09'
---

## 概要

金融ニュースの見出しデータはイベント種別が偏在し希少事象が不足するという課題に対し、NeMo Data Designerによるカテゴリ重み付き生成、NeMo Curatorによるセマンティック重複排除、Nemotronモデルによる高スループット推論を組み合わせた反復ループで50万件超のユニークな見出しを合成した。単発の大量生成では重複率65%に達したのに対し、生成・重複排除・few-shot例更新・カテゴリ重み補正を82回繰り返すことで累積重複排除率約82%を達成し、モデル蒸留や分類タスクに使える多様な合成コーパスFinHeadlineMixを構築した。

## 設計のポイント

- 新規バッチをそのバッチ内だけでなく蓄積済みコーパス全体と比較するグローバル重複排除で、バッチ間の重複を防ぎ全体の意味的多様性を保つ
- farthest-from-centroidに基づくfew-shot例の動的選択とカテゴリ重みの反復補正により、希少イベントのカバレッジを高め生成の偏りを是正する
- 各イテレーションでコーパス状態・カテゴリ重み・few-shot例・埋め込みをチェックポイントし、SLURMジョブチェーンでクラッシュ復旧しながら数日規模のパイプラインを継続実行する
- vLLMによる4-way tensor parallelismでのMoEモデル推論と、別GPU群でのRayベース重複排除を並列稼働させ、生成と重複排除のスループットを両立する

## 使いどころ

- 金融ニュースのように事象の出現頻度に偏りがあるドメインで、希少イベントを含む学習・評価データを増強したいチーム
- 単発の大量生成では重複ばかり増える課題に直面している、大規模合成データセット構築の担当者
- モデル蒸留や分類タスク向けに、教師モデルに迫る性能をコンパクトな学生モデルに持たせたいMLチーム
