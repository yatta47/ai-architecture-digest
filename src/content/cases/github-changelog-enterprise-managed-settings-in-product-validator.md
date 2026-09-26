---
type: announcement
title: Copilotエンタープライズ管理設定のアプリ内バリデータ
title_original: Enterprise managed settings in-product validator
company: GitHub
industry: cross-industry
cloud: []
patterns:
- policy-as-code
- guardrails
components:
- GitHub Copilot
- managed-settings.json
- team-mappings.json
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-25-enterprise-managed-settings-in-product-validator
published_at: '2026-09-25'
---

## 概要

GitHub Copilotのエンタープライズ管理設定に対し、不正なJSONや未対応設定、無効なチーム割り当てを検出するアプリ内バリデータが追加された。エンタープライズAIコントロール画面で、問題のファイルとJSONパスを確認できる。

## 設計のポイント

- ポリシーをファイル（JSON）で管理し、適用前に検証して設定ミスによる未適用を防ぐ。
- エラーを対象ファイルとJSONパス単位で示し、修正を容易にする。

## 使いどころ

- Copilotのポリシーを.github-privateリポジトリで管理する管理者。
- チーム別設定を多数運用する企業の統制担当。
