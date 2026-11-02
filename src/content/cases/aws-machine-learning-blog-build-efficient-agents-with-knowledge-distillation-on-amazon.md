---
type: guidance
title: ナレッジ蒸留でエージェントを小型モデルに置き換えコストを下げる手法
title_original: Build efficient agents with knowledge distillation on Amazon SageMaker AI
industry: retail
cloud:
- aws
patterns:
- fine-tuning
- ai-agent
- cost-optimization
components:
- Amazon SageMaker AI
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-efficient-agents-with-knowledge-distillation-on-amazon-sagemaker-ai/
published_at: '2026-11-02'
---

## 概要

ショッピングアシスタントを題材に、フロンティアモデル(教師)が生成した多段トラジェクトリのうちタスクを解いたものだけで小型モデル(生徒)をSFTするSeqKDの流れを示す。サーバーレス学習とホールドアウトでの評価までを扱う。

## 設計のポイント

- エージェントは1タスクで複数回モデルを呼ぶため、小型モデル化の効果が呼び出し回数に比例して効く。
- 教師の軌跡は成功したものだけを残して学習データにし、品質を担保する。
- 学習後は保持した評価ベンチマークで生徒モデルを教師と比較してから切り替える。

## 使いどころ

- エージェントの推論コストが運用規模で採算に合わなくなっているチーム。
- 特定ドメインのタスクでフロンティアモデル並みの品質を小型モデルで再現したい場合。
