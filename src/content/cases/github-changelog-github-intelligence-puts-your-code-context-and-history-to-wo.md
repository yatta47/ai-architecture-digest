---
type: announcement
title: エージェントに記憶と継続学習を与えるGitHub intelligence
title_original: GitHub intelligence puts your code, context, and history to work
company: GitHub
industry: cross-industry
cloud: []
patterns:
- context-engineering
- memory-consolidation
- ai-agent
components:
- GitHub Copilot Memory
- Copilot dreaming
- Copilot CLI
- VS Code
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-28-github-intelligence-puts-your-code-context-and-history-to-work
published_at: '2026-10-28'
---

## 概要

GitHub intelligenceはMemory、Dreaming、コード検索の3機能でエージェントに文脈を提供する層である。Copilot Memoryは一般提供となり、個人設定やリポジトリ規約をセッション横断で再利用する。

## 設計のポイント

- 個人・リポジトリ単位の記憶をクライアント横断で共有し、毎回の指示の繰り返しを減らす。
- Dreamingが過去作業を振り返って記憶を更新し、スキルや指示ファイルの変更はPRでレビューさせる。
- Dreamingはオプトインで、管理者がポリシーで制御する。

## 使いどころ

- 同じ規約や設定を毎セッション説明している開発者・チーム。
- コードレビューの繰り返し指摘をガイダンス化したい組織。
