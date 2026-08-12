---
type: announcement
title: Compliance APIがClaude CoworkとClaude Codeのセッションもカバー
title_original: Compliance API coverage extends to Claude Cowork and Claude Code
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- guardrails
components:
- Claude Compliance API
- Claude Cowork
- Claude Code
- Claude Enterprise
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/compliance-api-cowork-and-claude-code
published_at: '2026-08-11'
---

## 概要

AnthropicはCompliance APIの対象をClaude Cowork(デスクトップ/Web/モバイル)とClaude Code(CLI/デスクトップ)に拡張した(Claude Enterpriseのベータ)。プロンプト・応答・ツール呼び出し・スキル/アーティファクトを含む統合セッション記録を、既存のCompliance ChatsAPIと同じインターフェースで取得でき、監査やeDiscoveryのための個別ロギング基盤構築を不要にする。

## 設計のポイント

- 新しいセッションエンドポイントを既存のCompliance APIインターフェースに追加する形にし、既存の連携やAPIキーを変更せず利用できるようにした。
- プロンプト・応答・ツール呼び出し・スキル/アーティファクトを1つのセッションレコードに統合し、監査やeDiscoveryのために単一の記録として取得できるようにした。
- OpenTelemetryなど既存のエクスポート基盤と並行利用できるようにし、追加のインフラ構築を不要にした。

## 使いどころ

- 複数のClaude製品(チャット・Cowork・Code)にまたがる利用状況を1つのAPIで監査したいコンプライアンス・セキュリティチーム。
- 監査証跡やeDiscoveryのために、エージェントのツール呼び出しまで含めた完全なセッション記録が必要な規制業界の企業。
- サーフェスごとに個別のロギング基盤を構築せずに、Claude Enterpriseの利用状況を一元管理したい組織。
