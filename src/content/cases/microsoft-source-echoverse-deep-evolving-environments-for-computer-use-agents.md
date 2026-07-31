---
type: case
title: コンピュータ操作エージェントを鍛える高忠実度合成環境「Echoverse」
title_original: 'Echoverse: Deep, Evolving Environments for Computer-Use Agents'
company: Microsoft
industry: cross-industry
cloud: []
patterns:
- reinforcement-learning
- ai-agent
- eval
components:
- GitHub
- Hugging Face
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/research/blog/echoverse-deep-evolving-environments-for-computer-use-agents/
published_at: '2026-07-31'
---

## 概要

Microsoft Researchは、コンピュータ操作エージェントを訓練するための高忠実度な合成環境「Echoverse」を開発。12種類の深い訓練用ワールドと検証器を用いて、モデル・環境・検証器を同時に進化させるループにより9Bモデルのスコアを36.5%から67.1%まで引き上げた。

## 設計のポイント

- 環境の数を増やすより、既存のワールドの忠実度(深さ)を高めることを優先する設計判断
- モデルの実行結果を読み直し、失敗箇所の環境・タスク・検証器を修正する「共進化ループ」を採用
- 日付ピッカーやネストしたフィルタなど、エージェントが苦手とする特定のUI操作を集中的に鍛える能力ターゲティング型ワールドを用意
- 検証は画面のピクセルではなくアプリケーションの実際の状態に基づいて行う

## 使いどころ

- ログイン必須の業務システム(メール・銀行・医療記録・社内コンソール等)向けにコンピュータ操作エージェントを訓練したいチーム
- 静的なベンチマークが飽和してしまう問題を避けたいAIエージェント研究者
- 特定のUI操作(日付選択・複雑なフィルタなど)でエージェントが繰り返し失敗するケースの改善
