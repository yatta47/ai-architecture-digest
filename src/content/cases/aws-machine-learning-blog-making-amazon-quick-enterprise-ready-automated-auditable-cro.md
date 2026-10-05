---
type: case
title: Amazon Quickのエージェント資源をアカウント間で冪等に昇格するMCPサーバー
title_original: 'Making Amazon Quick enterprise-ready: Automated, auditable cross-account resource promotion'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- ci-cd
- policy-as-code
components:
- Amazon Quick
- Amazon Bedrock AgentCore
- Model Context Protocol
- Amazon S3
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/making-amazon-quick-enterprise-ready-automated-auditable-cross-account-resource-promotion/
published_at: '2026-10-05'
---

## 概要

開発アカウントで作ったAmazon Quickのエージェント、コネクタ、ナレッジベース等を本番アカウントへ昇格する作業を、AgentCore上のMCPサーバー（Quick Resource Migrator）で自動化する。API経由でリソースと権限を読み取り再適用し、監査可能で再実行可能にする。

## 設計のポイント

- 作成・読取・更新・一覧のみを組み合わせ、対象側へdeleteを発行しないことで実行が追加・更新に限定され安全になる。
- 手作業の再構築を、1回のツール呼び出しで完結する冪等なワークフローにまとめる。
- リソースと権限をAPIで取得して再現するため、環境間の差異と監査上の曖昧さを減らせる。

## 使いどころ

- dev/QA/prodの複数アカウント運用でエージェントをプロモートする企業。
- エージェント基盤のガバナンスと変更監査を求める管理者。
