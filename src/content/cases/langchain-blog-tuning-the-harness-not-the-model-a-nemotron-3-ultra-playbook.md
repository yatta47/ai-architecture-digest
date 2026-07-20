---
type: case
title: ハーネスチューニングでNemotron 3 Ultraをフロンティア級エージェントに引き上げる
title_original: 'Tuning the harness, not the model: a Nemotron 3 Ultra playbook'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
- context-engineering
- eval
- llmops
components:
- Nemotron 3 Ultra
- LangSmith
- LangChain Deep Agents
- Opus 4.8
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/tuning-the-harness-not-the-model-a-nemotron-3-ultra-playbook
published_at: '2026-07-08'
---

## 概要

LangChainはNVIDIAのオープンモデルNemotron 3 Ultraに対し、モデル自体は変更せずシステムプロンプト・ツール記述・ミドルウェアといったエージェントハーネスのみをチューニングした。トレース駆動の評価ループで失敗パターンを観察し、安価なスクリーニングから段階的に検証することで、Deep Agentsベンチマークで最高0.86（Opus 4.8の0.87に匹敵）を達成しつつコストは約10分の1（1回あたり約4.48ドル対43.48ドル）に抑えた。ハーネスチューニングには限界があり、変更を重ねてもスコアが動かない場合はモデルの事後学習側の問題を示唆すると結論づけている。

## 設計のポイント

- evalをハーネス変更の学習データとして扱い、勝率が複数回の試行で再現し他のケースを退行させない場合のみ変更を採用する
- システムプロンプトの汎用的な書き換えより、トレースで観測した特定の失敗行動1つに対応する短く単一目的の指示ブロックの方が効果が持続する
- 変更は代表性のある小規模データで安価にスクリーニングし、有効性が確認できた場合のみ高コストなフルスイートで再評価するコスト段階方式をとる
- モデルの重みと生成パラメータは固定し、システムプロンプト・ツール記述・ミドルウェアだけを変えて性能差を切り分ける

## 使いどころ

- オープンモデルをエージェントハーネス上で使いフロンティアモデル並みの性能を引き出したいチーム
- コーディングエージェントやDeep Agentsなど長時間稼働するツール使用エージェントの品質改善に取り組むチーム
- エージェント開発のためのeval基盤・トレース分析ループを構築したいチーム
