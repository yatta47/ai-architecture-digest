---
type: announcement
title: GitHub MobileでCopilotクラウドエージェントによるActions失敗修正が可能に
title_original: 'GitHub Mobile: Fix failing Actions checks with Copilot cloud agent'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- ci-cd
components:
- GitHub Copilot cloud agent
- GitHub Actions
- GitHub Mobile
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-23-github-mobile-fix-failing-actions-checks-with-copilot-cloud-agent
published_at: '2026-07-23'
---

## 概要

GitHub ActionsのチェックがPRで失敗した際、モバイルアプリから「Fix with Copilot」を選ぶだけでCopilotが原因分析と修正PRの作成まで自律的に行う機能が追加された。修正案は元のPRの上に積まれ、レビュー依頼が通知される。

## 設計のポイント

- 失敗したチェックを起点に、既存PRの上に新たな修正PRを積む形で変更を提案し、マージ前に必ず人がレビューする
- モバイル単体での「ワンタップ修正」フローとして設計し、外出先でもCI詰まりを解消できるようにする

## 使いどころ

- 外出中でもCIの失敗をすぐに解消してPRを前進させたい開発者
- 軽微なActions失敗の一次対応をエージェントに任せたいチーム
