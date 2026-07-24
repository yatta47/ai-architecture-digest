---
type: guidance
title: カスタムグレーダーでo4-miniの推論を強化するReinforcement Fine-Tuning
title_original: Reinforcement fine-tuning guide
industry: cross-industry
cloud: []
patterns:
- reinforcement-learning
- fine-tuning
- eval
components:
- o4-mini
- Structured Outputs
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/reinforcement-fine-tuning
published_at: '2025-07-18'
---

## 概要

Reinforcement Fine-Tuning(RFT)は、固定の正解ではなく開発者が定義したグレーダーによる採点をもとにo-seriesモデルの重みを更新し、高スコアの出力が生成されやすくなるよう調整する手法。医療診断や法律判例の関連性判定など、専門家の合意が得られる明確なタスクに向く。

## 設計のポイント

- RFTを使う前に、専門家が独立して同じ答えに収束するかを確認し、タスクの曖昧さがRFTに適さないほど大きくないかを検証する。
- 評価スコアが最小値・最大値に張り付いていないか事前にevalsで確認し、強化学習で改善する余地があるスコア分布かどうかを見極める。
- モデルがまぐれで高評価を得られない設計(ガードプルーフ)にタスクを再構成し、正しい推論過程を伴わない偶然の正解に報酬が出ないようにする。

## 使いどころ

- 専門家レビューを合格基準として明確化できる、法務・医療などドメイン特化タスクをモデルに学習させたい場合。
