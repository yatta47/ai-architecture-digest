---
type: announcement
title: 'LangSmith Fine-Tuning: エージェント軌跡から微調整モデルまでを一貫実行するCLI'
title_original: Introducing LangSmith Fine-Tuning
company: LangChain
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- llmops
- eval
components:
- LangSmith
- smithtune
- Fireworks
- Baseten Loops
- LoRA
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-fine-tuning
published_at: '2026-09-24'
---

## 概要

LangChainが、LangSmithの軌跡から教師あり微調整(SFT)用データを作り、FireworksまたはBasetenで学習し、LangSmithで評価・デプロイまでを一つのCLI(smithtune)で行う機能を公開した。特化モデルにより、汎用フロンティアモデルと同等以上の性能を低コスト・低レイテンシで狙える。

## 設計のポイント

- 各ターンでモデルが実際に見た文脈を記録する軌跡形式を使い、行動と真の文脈を対応づけて学習データにする。
- ルーブリックに基づきエージェント群が良い軌跡を選別し、データセットを監査可能な成果物として保存する。
- 学習前にplanで設定を確認し、検証損失が最小のチェックポイントを選ぶ。
- リプレイ評価でベースと微調整後を比較し、結果に応じてデータや設定を見直すループを回す。

## 使いどころ

- 特定タスクのエージェントを小型モデルに置き換えてコストとレイテンシを下げたいチーム。
- 本番トレースを資産として蓄積・選別し、継続的にモデルを改善したい場合。
- GPU調達なしで微調整を試したい場合。
