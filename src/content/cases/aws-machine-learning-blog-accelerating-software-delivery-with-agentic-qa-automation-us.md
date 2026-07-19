---
type: guidance
title: Amazon Nova Actによるエージェント型QA自動化基盤のCI/CD統合
title_original: Accelerating software delivery with agentic QA automation using Amazon Nova Act – Part 2
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- ci-cd
- parallel-execution
components:
- Amazon Nova Act
- Amazon ECS
- AWS Fargate
- AWS Secrets Manager
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/accelerating-software-delivery-with-agentic-qa-automation-using-amazon-nova-act-part-2/
published_at: '2026-07-14'
---

## 概要

Amazon Nova Actを使ったエージェント型QA自動化の参照実装「QA Studio」の続編。個々のユースケースをテストスイートとしてまとめ並列実行する仕組みと、CI/CDパイプラインに組み込むための非対話型CLIを追加した。

## 設計のポイント

- テストスイート内の各ユースケースを個別のFargateワーカータスクで並列実行し、直列実行に比べ合計実行時間を短縮する。
- CLIはOAuth 2.0クライアントクレデンシャルで非対話認証し、CI/CDランナーからブラウザログインなしで実行できるようにする。
- --base-urlや--varでテスト定義自体を変更せずに環境ごとの向き先・認証情報を上書きできるようにする。

## 使いどころ

- リグレッションスイートをCI/CDのデプロイゲートに組み込みたいQAチーム。
- 同じテストをdev/staging/本番など複数環境で使い回したいチーム。
