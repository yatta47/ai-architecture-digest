---
type: guidance
title: Claude Platform on AWSを本番・開発者PC・外部環境から使うマルチ環境アクセス構成
title_original: Implementing Multi-Environment Access for Claude Platform on AWS
industry: cross-industry
cloud:
- aws
- multi-cloud
- on-prem
patterns:
- llm-gateway
- defense-in-depth
components:
- Claude Platform on AWS
- AWS Organizations
- AWS IAM
- Amazon EKS
- SigV4
- OIDC
- Anthropic SDK
- AWS CLI
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/implementing-multi-environment-access-for-claude-platform-on-aws/
published_at: '2026-10-01'
---

## 概要

Claude Platform on AWSの1つのサブスクリプションを、AWS上の本番、開発者ノートPC、他クラウドやオンプレのCI/CDという認証要件の異なる3環境から共有する手順書。専用のAI Servicesアカウントにサブスクリプションとワークスペースを集約し、クロスアカウントSigV4、ワークスペース限定APIキー、OIDCフェデレーションと短期キーの3経路を構築する。

## 設計のポイント

- サブスクリプション、ワークスペース、APIキー、クロスアカウントロールをAI Servicesアカウントに集約し、ワークロードアカウントはロールを引き受けて推論する構成にした。
- 本番と開発のワークスペースを分けて、トラフィックを分離した。
- AWSワークロードはクロスアカウントSigV4にしてAPIキーの保管やローテーションを不要にした。
- 外部環境はOIDCフェデレーションから一時認証情報と短期トークンを得て、永続的な認証情報を持たない。

## 使いどころ

- 複数AWSアカウントを持つ組織がClaudeを本番と開発で安全に分離して使いたい場合。
- オンプレやほかのクラウドのCI/CDパイプラインから秘密情報を持たずにClaudeを呼びたい場合。
- チームやワークロード単位でワークスペースを分けたい組織。
