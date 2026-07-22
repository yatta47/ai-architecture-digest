---
type: announcement
title: Claude Platformの操作履歴を追跡する監査ログAPI
title_original: Audit Claude Platform activity with the Compliance API
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- Compliance API
- Claude Platform
- Claude Enterprise
- Claude API
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-platform-compliance-api
published_at: '2026-03-30'
---

## 概要

Claude PlatformにCompliance APIが追加され、管理者は組織内の監査ログにプログラムからアクセスできるようになった。ワークスペースメンバー追加やAPIキー作成などの管理・システム操作と、ファイル作成/削除やスキル削除などのリソース操作を活動フィードとして取得でき、期間・ユーザー・APIキーで絞り込める。モデルとの直接対話（推論）自体はログ対象外。

## 設計のポイント

- 監査対象を「アクセス/設定を変更する管理・システム操作」と「データを作成・変更するリソース操作」の2カテゴリに分離し、それぞれ意味のある粒度でログ化している。
- モデルへの推論リクエストそのものはログ対象から除外し、ガバナンス上重要な操作ログとプライバシー配慮が必要な利用ログを明確に切り分けている。
- APIキーやユーザー、期間でフィルタ可能な単一の活動フィードエンドポイントとして提供し、既存のコンプライアンス基盤に統合しやすくしている。
- Claude EnterpriseとClaude APIの組織を同一の親組織に紐づけることで、複数プロダクトにまたがる監査ログを一つのフィードに集約できる。

## 使いどころ

- 金融・医療・法務など規制産業のセキュリティ/コンプライアンスチームが、手作業のエクスポートに頼らず利用者の操作履歴を継続的に監査したい場合。
- 既存のSIEMやGRCツールにAI利用状況のログを取り込み、他システムと同じ運用フローで監視したい管理者。
- Claude EnterpriseとClaude APIを併用する組織が、両方の監査ログを一元的に確認したい場合。
