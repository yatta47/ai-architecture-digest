---
type: announcement
title: GitHub AI Scanを最大20リポジトリまで一括開始
title_original: Bulk start AI Scan for repositories
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- GitHub AI Scan
- GitHub Code Scanning
- CodeQL
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-16-bulk-start-ai-scan-for-repositories
published_at: '2026-11-16'
---

## 概要

AI Scan for repositoriesで最大20リポジトリの脆弱性スキャンを一括開始できるようになった(パブリックプレビュー)。CodeQL非対応の言語も対象で、結果はコードスキャンのバックログにCodeQLアラートと並ぶ。Copilotライセンスは不要。

## 設計のポイント

- 組織設定の有効化時や組織アラート画面から一括でスキャンを開始できる
- 結果をCodeQLアラートと同じバックログで扱う

## 使いどころ

- 多数のリポジトリを持つ組織でのセキュリティ棚卸し
- CodeQL非対応言語の補完
