---
type: announcement
title: 組織向けClaude Enterpriseプラン
title_original: Claude for Enterprise
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- context-engineering
- enterprise-access-control
components:
- Claude Enterprise
- GitHub integration
- SSO
- SCIM
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-for-enterprise
published_at: '2024-09-10'
---

## 概要

組織が社内知識を使って安全にClaudeと協業できるClaude Enterpriseプランを発表。50万トークンの拡張コンテキストウィンドウやGitHubとのネイティブ連携でコードベース全体を扱えるようにし、SSO・ロールベース権限・監査ログ・SCIMなどエンタープライズ向けセキュリティ機能を備える。

## 設計のポイント

- 拡張コンテキストウィンドウ(50万トークン)により大量の社内ドキュメントやコードベースをまとめて渡せる設計にする
- SSO・SCIM・監査ログなどIDガバナンス機能を製品に組み込み、データ保護とアクセス制御を両立する
- GitHubリポジトリとの同期により、コードベース全体を踏まえた機能開発・デバッグ・オンボーディング支援を可能にする

## 使いどころ

- 複数チームが社内知識を横断的に活用しながらAIで生産性を高めたい大企業
- セキュリティ・コンプライアンス要件からSSOや監査ログが必須の規制業界
