---
type: guidance
title: Microsoft Entra IDで複数AWSアカウントのID・アクセス管理を一元化する参照アーキテクチャ
title_original: Microsoft Entra identity management and access management for AWS
industry: cross-industry
cloud:
- aws
- azure
patterns:
- defense-in-depth
- single-sign-on
components:
- Microsoft Entra ID
- AWS IAM
- Microsoft Entra Conditional Access
- Multifactor Authentication (MFA)
- Privileged Identity Management (PIM)
- Microsoft Entra ID Protection
- Microsoft Defender for Identity
- Microsoft Defender for Cloud Apps
- Microsoft Sentinel
data_sources:
- 認証リクエスト
- 脅威シグナル
- IDリスク情報
- IAMロール/ユーザー
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/aws/aws-azure-ad-security
published_at: '2026-07-10'
---

## 概要

AWSはアカウントごとに独立したIAMストアを持つため、複数アカウント環境ではID管理がサイロ化し、パスワードや認証の管理が煩雑になりやすい。本リファレンスアーキテクチャは、既存のMicrosoft Entra IDを各AWSアカウントとフェデレーションし、SSO・MFA・条件付きアクセスによる一元的なID/アクセス管理を実現する構成を示す。既存のIDプロバイダーやAWSアカウントに影響を与えず検証し、準備が整ってから切り替えられる段階移行のアプローチも解説する。

## 設計のポイント

Entra IDをアイデンティティ プロバイダーとして各AWSアカウントに接続し、AWSマネジメントコンソールやリソースへのアクセス認可を条件付きアクセスとリスクベース評価に集約する。最も機密性の高いアカウントにはP2ライセンスのPIMによるJust-In-Time昇格やEntra ID Protectionのリスク検知、Defender for Identityの振る舞い監視を追加し、多層防御(defense-in-depth)を段階的に重ねる。既存環境と並行して構築・テストし、切り替え時期を自分で制御することで移行リスクを抑える設計とする。

## 使いどころ

複数のAWSアカウントを運用し、すでにMicrosoft 365やハイブリッドID基盤でEntra IDを使っている組織が、追加コストを抑えつつID管理を一元化・強化したい場面に効く。AWSのIDアーキテクト・管理者・セキュリティアナリスト向けの手引きとして有用。
