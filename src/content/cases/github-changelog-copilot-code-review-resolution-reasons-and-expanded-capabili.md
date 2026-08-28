---
type: announcement
title: GitHub Copilotコードレビュー、Bot作成PRや大規模PRにも対応し解決理由のフィードバックを追加
title_original: 'Copilot code review: Resolution reasons and expanded capabilities'
company: GitHub
industry: cross-industry
cloud: []
patterns:
- human-in-the-loop
components:
- GitHub Copilot code review
- Copilot cloud agent
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-27-copilot-code-review-resolution-reasons-and-expanded-capabilities
published_at: '2026-08-27'
---

## 概要

GitHub Copilotコードレビューは、Copilotライセンスのないbotが作成したPR（Copilot cloud agent含む）や、従来300ファイル/2万行の上限を超える大規模PRもレビューできるようになった。あわせて、レビューコメントを解決する際に『対応済み』『対応しない』『誤り』の理由を選択できるようになり、フィードバックとして製品改善に活用される。

## 設計のポイント

- botが作成したPRやCopilot cloud agent発のPRも、組織へ直接課金する形でレビュー対象に含め、カバレッジの穴を塞ぐ
- ファイル数・行数の上限を撤廃し、大規模PRでも自動レビューが機能するようにする
- レビューコメントの解決理由（対応済み/対応しない/誤り）を構造化データとして収集し、モデル・プロダクト改善のフィードバックループに使う

## 使いどころ

- bot生成PRが多いリポジトリで、レビューカバレッジの抜け漏れを減らしたい開発チーム
- 大規模なモノレポやリファクタリングPRでも自動コードレビューを機能させたい場合
- AIコードレビューの誤検知率や有効性を定量的に把握・改善したいプロダクトチーム
