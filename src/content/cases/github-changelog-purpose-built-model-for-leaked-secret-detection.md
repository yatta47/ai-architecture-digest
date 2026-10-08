---
type: announcement
title: 秘密情報検出に特化したモデルをGitHubが導入
title_original: Purpose-built model for leaked secret detection
company: GitHub
industry: cross-industry
cloud: []
patterns:
- guardrails
- fine-tuning
- defense-in-depth
components:
- GitHub secret scanning
- Push protection
- GitHub Copilot
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-07-purpose-built-model-for-leaked-secret-detection
published_at: '2026-10-07'
---

## 概要

GitHubが秘密情報検出に特化して微調整したモデルを、シークレットスキャン、プッシュ保護、Copilotのセキュリティレビューに展開。周辺コードを読み、形式が不定なパスワードも検出する。

## 設計のポイント

- 生成せず検出だけを行う専用モデルを用いる。
- 前後の文脈を読ませて形式のない資格情報を拾う。

## 使いどころ

- AIエージェントが書くコードからの漏えいを防ぎたい開発組織に効く。
