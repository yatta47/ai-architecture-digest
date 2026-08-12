---
type: case
title: スーパーバイザ無しで収束する自己組織化マルチエージェントクラスタ(kiro-flock)
title_original: Scaling patterns for self-organizing multi-agent clusters with Kiro
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- parallel-execution
components:
- Kiro CLI
- Amazon EC2
- Amazon S3
- Amazon API Gateway
- AWS Lambda
- Amazon Cognito
- Amazon CloudWatch
- Amazon Bedrock
- Strands Agents SDK
outcome:
  type: quality
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/scaling-patterns-for-self-organizing-multi-agent-clusters-with-kiro/
published_at: '2026-08-11'
---

## 概要

AWSは、中央のスーパーバイザではなく共有S3バケット上の追記専用ログを介してKiro CLIエージェントのクラスタが収束するオープンソース参照実装kiro-flockを公開した。スーパーバイザ型が抱えるコンテキストウィンドウの上限や単一障害点を避けつつ、コードレビューや大量移行のような分解可能なタスクで多様なアプローチを引き出せる。

## 設計のポイント

- 中央のスーパーバイザを置かず、各エージェントが自分のログだけを追記書き込みする共有S3バケットを介して合意形成する『共有状態による協調』にした。
- 各エージェントが読む隣接ログの数を『半径』パラメータで制限し、全員に全ログを見せると最初の投稿へ収束してしまう問題を回避した。
- 反復ごとにセッションを使い捨て(フレッシュセッション)にすることで、コンテキストのドリフトを防いだ。
- タスクの性質(分解可能・順序に依存しない・多様性が資産になる)によってクラスタ型とスーパーバイザ型を使い分ける判断基準を明示した。

## 使いどころ

- 大規模コードベースのレビューや大量モジュールの移行など、独立した貢献を多数集めて1つの目標に近づけたい作業。
- 単一プランナーの偏りを避け、本当に多様なアプローチのブレインストーミングを得たいチーム。
- エージェントが自由に参加・離脱でき、単一障害点を避けたい長時間実行のワークロード。
