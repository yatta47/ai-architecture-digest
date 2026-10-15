---
type: announcement
title: PR上の脆弱性をAIで検出するCode scanningのAI Scan
title_original: AI Scan for pull requests generally available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- ci-cd
components:
- GitHub Code Scanning
- CodeQL
- GitHub Code Security
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available
published_at: '2026-10-15'
---

## 概要

GitHubはPRの変更に対するAI Scanを一般提供した。CodeQLが未対応のPHP、Shell、Terraform、Dockerfileなどを補完する。指摘は助言扱いでマージをブロックせず、Code Security AI Creditsを消費する。

## 設計のポイント

- CodeQLと併用して未対応言語を補う
- AI指摘は助言にとどめ、チェック失敗やマージ阻止には使わない
- 指摘にAIバッジと自動修正案を付ける

## 使いどころ

- PHPやIaCなどCodeQL対象外の資産を持つリポジトリのセキュリティ担当
