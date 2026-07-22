---
type: announcement
title: Claude Compliance APIで60以上のセキュリティ・コンプライアンスツールと連携
title_original: Claude now works with more security and compliance tools
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- guardrails
components:
- Claude Compliance API
- Claude Enterprise
- Claude Platform
- CrowdStrike
- Okta
- Microsoft Purview
- Datadog
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/compliance-api-security-partners
published_at: '2026-05-21'
---

## 概要

AnthropicがClaude Compliance API経由で60以上のセキュリティ・コンプライアンスパートナーとの連携を発表。会話内容やアップロードファイルなどのコンテンツデータと、ログイン・管理操作などのアクティビティイベントをDLP・SIEM・IDプラットフォームなど既存の管理ツールに流し込み、他のアプリケーションと同じガバナンス体制でClaudeを統制できるようにする。

## 設計のポイント

- コンテンツデータ（会話・ファイル・プロジェクト）とアクティビティイベント（ログイン・管理操作・設定変更）を分離したAPIとして公開し、パートナー側が既存のダッシュボード・アラートにそのまま統合できるようにする
- DLP・SASE・SIEM・ID・eDiscovery・AIセキュリティ姿勢管理など既存のセキュリティカテゴリの分類に沿ってパートナーを整理し、企業が既存ツールの延長でClaudeを統制できるようにする

## 使いどころ

- すでにSIEMやDLPなどのセキュリティ基盤を運用している企業が、Claudeの利用状況を既存の統制フローに組み込みたい場合
- IT・セキュリティ部門が、生成AIツールの利用を他の業務アプリと同水準で監査・監視したい場合
