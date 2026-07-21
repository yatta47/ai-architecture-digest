---
type: case
title: 検証・敵対的サブエージェントで1日でプロトタイプを仕上げたハッカソン優勝3作品
title_original: Meet the winners of our Claude Opus 4.8 Build Day hackathon
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
- eval
components:
- Claude Opus 4.8
- Claude Code
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon
published_at: '2026-06-17'
---

## 概要

Claude Opus 4.8を使った12時間ハッカソンの優勝3チームの事例。歴史的建造物の3D復元(Tekton)、Census準拠の合成人口シミュレーション(Sim Francisco)、スマホ写真から3Dシーンを生成するツール(Custom Universe)を、いずれも検証・敵対的サブエージェントによる自己修正ループで1日のうちに完成させた。

## 設計のポイント

- 検証・敵対的エージェントを独立したコンテキストウィンドウで走らせ、自己修正ループで基準を満たすまで再チェックする
- 大規模タスクは着手前にPRDとチケット単位のタスクリストへ分解し、並列ワークフローとして実行する
- コストがかさむ逐次推論はモデル自身に最適化させ、代表ペルソナへのクラスタリングなどでバッチ化しコストを1〜2桁削減する

## 使いどころ

- 歴史的建造物の3D復元や学術検証など、根拠追跡が求められるドメインでの自己検証エージェント活用
- 大規模シミュレーションや合成データ生成でコストを抑えたい場合の推論バッチ最適化
