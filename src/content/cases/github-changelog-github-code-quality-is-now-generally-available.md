---
type: announcement
title: GitHub Code Quality GA、CodeQLとAI検出・Copilot Autofixでマージ前に品質問題を検出
title_original: GitHub Code Quality is now generally available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- human-in-the-loop
- guardrails
components:
- CodeQL
- Copilot Autofix
- GitHub Actions
- GitHub Advanced Security
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-20-github-code-quality-is-now-generally-available
published_at: '2026-07-20'
---

## 概要

GitHub Code QualityがGitHub Enterprise CloudおよびGitHub Teamで一般提供開始となった。CodeQLによる決定論的解析とAIによる保守性・信頼性検出を組み合わせてプルリクエスト中の問題を検出し、Copilot Autofixがマージ前にレビュー可能な修正案を提示する仕組みで、GitHub社内では検出された問題の67.3%がマージ前に解消されているという。GA版では組織横断ダッシュボード、カバレッジメトリクス表示、rulesetsによる品質ゲート、管理・取得用APIが追加され、料金はアクティブコミッター課金＋AI機能の従量課金＋CodeQL実行のコンピュート費用で構成される。

## 設計のポイント

- CodeQLの決定論的解析とAIによる保守性・信頼性検出を組み合わせるハイブリッド構成を採用
- Copilot Autofixが修正案を提示し人間がマージ前にレビュー・承認するヒューマン・イン・ザ・ループ設計
- GitHub rulesetsでカバレッジ閾値などの品質ゲートを設定し、evaluateモードでブロックせず段階的に導入できるようにする
- アクティブコミッター単位の月額固定費とAI機能・CodeQL実行の従量課金を組み合わせた価格モデル

## 使いどころ

- AIによるコード生成量が増える中でマージ前に保守性・信頼性の問題を検出したいエンジニアリング組織
- 組織横断でコード品質やテストカバレッジを可視化したいプラットフォーム/セキュリティチーム
- 既存のGitHub Advanced Securityと併用しつつ、品質ゲートを段階的（evaluateモード）に本番運用へ導入したいチーム
