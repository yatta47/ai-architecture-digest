---
type: guidance
title: Amazon QuickをPrivateLinkでオンプレミスデータへ閉域接続する構成
title_original: Securing Quick access from corporate networks with AWS PrivateLink
industry: cross-industry
cloud:
- aws
- on-prem
patterns:
- defense-in-depth
components:
- Amazon Quick
- AWS PrivateLink
- AWS Direct Connect
- AWS Site-to-Site VPN
- Amazon VPC
- Amazon S3
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/securing-quick-access-from-corporate-networks-with-aws-privatelink/
published_at: '2026-10-21'
---

## 概要

Amazon QuickのAIエージェントやダッシュボードから、オンプレミスのデータへ公衆インターネットを通さず接続する手順の解説。ユーザー向け通信はVPCエンドポイント、データ取得はVPC接続という二つの経路を使い分け、セキュリティグループとエンドポイントポリシーで多層防御にする。

## 設計のポイント

- ユーザー向けトラフィックとQuickがデータを取りに行くトラフィックを分けて、それぞれ別の閉域接続手段を当てる。
- Direct ConnectまたはSite-to-Site VPNの上にVPCエンドポイントを構成し、通信をAWSバックボーン内に収める。
- セキュリティグループとエンドポイントポリシーを重ね、監査証跡も確保する。

## 使いどころ

- HIPAA・FedRAMP・PCI-DSSなどでデータを制御された境界内に置く必要がある企業。
- 社内DBやプライベートMCPサーバーをAIエージェントから利用したい管理者。
