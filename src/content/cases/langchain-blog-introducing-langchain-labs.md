---
type: announcement
title: 'LangChain Labs: エージェントの継続学習に向けた応用研究プログラム'
title_original: Introducing LangChain Labs
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- prompt-optimization
- fine-tuning
components:
- LangSmith
- Nemotron
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-langchain-labs
published_at: '2026-06-10'
---

## 概要

LangChainは、エージェントが本番で生成するトレース・フィードバック・eval結果を学習データに変換し、継続的にエージェントを改善する応用研究プログラム「LangChain Labs」を立ち上げた。Harvey、NVIDIA、Prime Intellect、Fireworks、Basetenといった研究パートナーと組み、コストとレイテンシのパレートフロンティア改善、評価・シミュレーション環境の構築、モデルファミリー横断のプロンプト最適化などを初期テーマに掲げている。トレースデータの蓄積・変換基盤としてLangSmithを活用し、Nemotronのような小型モデルをコスト効率の良いサブエージェントとしてファインチューニングする取り組みも進めている。

## 設計のポイント

- LangSmithで収集したトレース・フィードバック・eval結果をそのまま継続学習の学習データとして再利用できる基盤を前提に設計している。
- 改善をハーネス最適化・モデル選択・ファインチューニングという複数レイヤーに分けて適用できるようにしている。
- コスト・レイテンシ・タスク性能のパレートフロンティア上で、モデルとハーネスの最適な組み合わせを継続的に探索する研究方針をとる。
- 本番相当のエンドツーエンド環境でエージェントを評価できるシミュレーション環境を体系的に構築する方向性を掲げている。

## 使いどころ

- 法務のような専門ドメインでエージェントの汎化性能を検証・向上させたいチーム(Harveyの事例)。
- コスト効率の良いサブエージェントとして小型モデルをファインチューニングしたいチーム。
- 複数モデルファミリー間でのプロンプト移行にかかる手動チューニングの手間を減らしたいチーム。
- 本番稼働中のエージェントのトレースデータを、継続的な改善サイクルに組み込みたい組織。
