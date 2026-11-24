---
type: announcement
title: Bedrockのモデル提供元向けトラステッドアクセスAPIとAnthropic EFS/EDC
title_original: Introducing the Amazon Bedrock Trusted Access API with Anthropic's Enterprise Frontier Safeguards and Enterprise
  Data Controls
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- guardrails
- policy-as-code
- defense-in-depth
components:
- Amazon Bedrock
- AWS KMS
- Amazon S3
- AWS IAM
- AWS Organizations
- Claude
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-trusted-access-api-with-anthropics-enterprise-frontier-safeguards-and-enterprise-data-controls/
published_at: '2026-11-24'
---

## 概要

Amazon Bedrockがモデル提供元のトラステッドアクセスプログラムを一元的に発見・申請・登録できるAPIを一般提供し、Anthropicの Enterprise Frontier Safeguards(EFS)とEnterprise Data Controls(EDC)をパブリックプレビューで開始した。自動安全監視で検知したリスクはSafety Caseとして顧客側がレビューでき、保持データの保管先を自社アカウント(EFS)かAmazon管理ストレージ(EDC)から選べる。

## 設計のポイント

- 適格性確認(eligible/requestable)と規約同意の登録を分離し、アカウント/組織/プロジェクト単位で適用範囲を選ばせている。
- 登録操作をAPI化してIAMポリシーとSCPで誰が参加できるかを統制できる。
- EFSでは顧客のKMSキーとS3バケットポリシー経由でのみ保持データへアクセスし、アクセス喪失から24時間でモデル提供を止める設計で、データ主権を担保している。
- 自動監視は複数リクエストにまたがる悪用やエージェントの逸脱を検知し、ケースを顧客のバケットに出力して人手レビューを顧客側に残す。

## 使いどころ

- 医療・金融・法務などデータ可視性の規制が厳しい企業が最上位モデルを使うとき。
- 安全監視ポリシーを満たしつつ保持データの保管場所を自社で管理したい場合。
- 複数プロバイダーのアクセスプログラムを組織内で統一的に統制したい管理者。
