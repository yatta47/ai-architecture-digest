---
type: announcement
title: Claude Opus 4.7による自律的コード脆弱性スキャン・パッチ生成『Claude Security』
title_original: Claude Security is now in public beta
industry: cross-industry
cloud: []
patterns:
- eval
- guardrails
components:
- Claude Security
- Claude Opus 4.7
- Claude Code
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-security-public-beta
published_at: '2026-04-30'
---

## 概要

Claude Opus 4.7を用いてリポジトリの脆弱性を発見し修正パッチ案まで生成するClaude Securityが、Enterprise顧客向けにパブリックベータ公開された。既知パターン検索ではなくコンポーネント間のデータフローを追跡してコードを理解し、多段階の検証パイプラインで誤検知を減らして確信度を付与、スケジュールスキャンやSlack/Jira連携、CrowdStrikeやMicrosoft Securityなどパートナー製品への組み込みも進む。

## 設計のポイント

- 既知の脆弱性パターン照合ではなく、モジュール間のデータフローを追跡してコードの意味を理解するアプローチを取る
- 発見した脆弱性ごとに独立した複数ステージの検証を経てから提示し、誤検知を減らして確信度スコアを付ける
- スキャンから修正パッチ適用までを1つのワークフローに収め、既存の監査・チケット管理システムと連携させる

## 使いどころ

- 自社コードベースを継続的に脆弱性スキャンし修正サイクルを高速化したいエンタープライズのセキュリティチーム
- 監査・トリアージの記録を既存のSlack/Jira等のワークフローに統合したい場合
