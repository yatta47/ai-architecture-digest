---
type: announcement
title: 安全性分類器で自律操作を解禁したブラウザ拡張「Claude in Chrome」の一般提供
title_original: Claude in Chrome is generally available
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- human-in-the-loop
components:
- Claude in Chrome
- Claude
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-in-chrome-generally-available
published_at: '2026-08-26'
---

## 概要

Claude in Chromeがすべての有料Claudeプランで一般提供開始し、複数タブを横断したブラウザ操作を、都度の承認なしに自律的に実行できるようになった。ウェブ由来の悪意ある指示(プロンプトインジェクション)への対策として、行動を検証する安全性分類器や、ツール結果を事前スクリーニングするプローブを継続的に強化してきたことが今回の一般提供の前提になっている。

## 設計のポイント

- 内部の自動攻撃者・外部red-teamer・実運用監視から収集したプロンプトインジェクション攻撃ライブラリでモデルと防御を継続的に学習させる
- ウェブページやメールなどのツール結果をプローブで事前スクリーニングし、疑わしい内容を検出したらモデルに警告する
- 行動実行の直前に安全性分類器のゲートを挟むことで、都度承認を求めずに自律実行と安全性を両立させる

## 使いどころ

- 社内ダッシュボードやレガシーシステム、ベンダーポータルなどAPI連携のないツールをエージェントに操作させたい場合
- 複数タブ・複数ページにまたがるブラウザ作業を自動化しつつプロンプトインジェクションのリスクを抑えたい場合
