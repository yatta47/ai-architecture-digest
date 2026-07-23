---
type: announcement
title: Claude Codeの開発貢献度を可視化するコントリビューションメトリクス
title_original: Understand Claude Code's impact with contribution metrics
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- Claude Code
- GitHub
- Claude GitHub App
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/contribution-metrics
published_at: '2026-01-29'
---

## 概要

AnthropicはClaude Codeの開発チームへの貢献度を可視化する「コントリビューションメトリクス」をパブリックベータで提供開始した。GitHubと連携し、Claude Code支援によるPRのマージ数やコミット行数、ユーザー単位の利用状況を既存の分析ダッシュボードで確認できる。Anthropic社内ではClaude Code導入後、エンジニア1人あたりのPRマージ数が67%増加し、コードの70〜90%がClaude Code支援で書かれているという。

## 設計のポイント

- GitHubのPRやコミットとClaude Codeのセッション活動を突合し、AI支援の有無を保守的に判定する
- 外部ツールやデータパイプラインを不要にし、既存の分析ダッシュボードにメトリクスを自動反映する
- DORAメトリクスやスプリントベロシティなど既存のKPIと組み合わせて使う設計にする

## 使いどころ

- エンジニアリング組織でClaude Code導入効果を定量的に把握したい管理者
- チームごとのAI支援コード生成の浸透度を比較したいマネージャー
- 既存の開発生産性KPIにAI支援の効果を追加で可視化したい場合
