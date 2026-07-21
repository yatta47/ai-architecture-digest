---
type: announcement
title: MCPコネクタの認可をIdPに一元化し、初回ログイン時にゼロタッチで権限を付与する仕組み
title_original: Centrally manage authorization for MCP connectors
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- policy-as-code
- defense-in-depth
components:
- Claude
- Model Context Protocol
- Okta
- Enterprise-Managed Authorization extension
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/enterprise-managed-auth
published_at: '2026-06-18'
---

## 概要

MCPコネクタの有効化には、これまで管理者による組織全体の有効化とユーザー個別の認可という2段階が必要だったが、新たなEnterprise-managed authによりOktaなどのIDプロバイダのグループ・ロールを通じて認可を継承させ、初回ログイン時点でコネクタが利用可能な状態にできるようになった。MCPへのCross App Access拡張という公開仕様に基づくため、Asana・Atlassian・Canva・Figma・Linearなど任意のMCPプロバイダが同じ方式で対応できる。

## 設計のポイント

- MCPアクセス管理を既存のIdPガバナンスの枠組みに統合し、権限付与・スコープ設定・失効をIdP側の操作だけで完結させる。
- IdPへの照会が低コストであることを利用してアクセストークンの有効期間を短縮し、ユーザーの権限剥奪が起きた際にコネクタアクセスが速やかに失効するようにする。
- コネクタをIdP経由の接続のみに限定できるようにし、個人アカウントを誤って業務ツールに接続してしまう事故を防ぐ。

## 使いどころ

- 新入社員のオンボーディングのたびに、コネクタごとのOAuth承認待ちの行列が発生していた情報システム部門。
- 多数のMCPコネクタを組織全体に安全かつ迅速に展開したいが、個別のOAuth管理を避けたいセキュリティチーム。
- 退職・異動時にAIツールへのアクセスを即座に失効させたい、ガバナンス要件の厳しい企業のIT運用担当。
