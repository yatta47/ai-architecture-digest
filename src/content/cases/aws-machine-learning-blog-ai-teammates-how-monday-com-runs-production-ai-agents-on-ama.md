---
type: case
title: 本番稼働するAIエージェント基盤：monday.comのSphera/Atlasアーキテクチャ
title_original: 'AI Teammates: how monday.com runs production AI agents on Amazon Bedrock'
company: monday.com
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- event-driven
- memory-consolidation
components:
- Amazon Bedrock
- Amazon SNS
- Amazon SQS
- Amazon EKS
- Amazon RDS
- Amazon ElastiCache
- Amazon EFS
- Amazon S3
- AWS Secrets Manager
- Claude Agent SDK
- monday-agent-sdk
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/ai-teammates-how-monday-com-runs-production-ai-agents-on-amazon-bedrock/
published_at: '2026-07-22'
---

## 概要

monday.comは社内エージェント基盤Spheraを通じ、Atlasのようなソフトウェアエンジニア役AIエージェントを人間の同僚と同じチームに配置し、Slack・monday・GitHubの3つの受信口を単一のエージェントセッションに集約して本番のPRを出荷している。SNS/SQSによるイベント駆動パイプライン、ElastiCache/EFS/S3による用途別の状態管理、Bedrockをモデル基盤としたClaude Agent SDKの薄いラッパーにより、10年物の巨大コードベース上でエンジニア1人当たりのPRスループットを5割以上向上させた。

## 設計のポイント

- Slackメンション・monday課題割当・GitHub PRレビュー依頼という3つの入り口をすべて同一のエージェントセッション(同一メモリ・同一ワークスペース)にルーティングし、システムを1つに統一する。
- SNSでファンアウトしSQSでチームごとにキューイングするpub/sub構成により、リトライ・DLQ・Bedrockスロットリング時のバックプレッシャー・過去1日分のイベントを使った耐障害性のあるリプレイを標準機能として得る。
- エージェントの状態を用途別に3つのストアへ分離する:即応性が必要なライブ状態はElastiCache、POSIX互換のセッション作業領域とクロスセッション記憶はEFS、確定済みの成果物・監査証跡はS3に格納する。
- Claude Agent SDKをランタイムとして採用しつつ、Bedrockへのプロバイダー中立なルーティング・ウォームスタートによるコールドスタート短縮・評価基準やツール連携などの独自ハーネスのために薄いラッパー(monday-agent-sdk)を自前で持ち、ランタイム自体はコモディティとして外部に委ねる。

## 使いどころ

- 数百万ユーザーが使う10年選手の巨大コードベースで、既存のオンコール・コンプライアンス体制を崩さずにAIコーディングエージェントを本番導入したい組織。
- AIエージェントをジョブキューではなく、プロフィール・マネージャー・評価スコアを持つ『チームメイト』として人間と同列に扱いたい開発組織。
- Slack・課題管理・コードレビューなど複数チャネルから届くイベントを、単一のエージェントランタイムに集約して運用を簡素化したいエンジニアリング基盤チーム。
- アシスタント利用(L1)からスキル/サブエージェント活用(L2)、完全なマルチエージェント自律配信(L3)へと段階的にAI活用を成熟させたい組織。
