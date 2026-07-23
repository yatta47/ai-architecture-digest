---
type: case
title: Anthropic法務チームがClaudeでマーケティング審査・契約レビュー・PIA作成を自動化した社内ワークフロー
title_original: How Anthropic's legal team cut review times from days to hours with Claude
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
- human-in-the-loop
- ai-agent
components:
- Claude Enterprise
- MCP
- Google Drive
- Slack
- Google Docs
- Office 365
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-anthropic-uses-claude-legal
published_at: '2025-12-08'
---

## 概要

Anthropicの法務チームは、コーディング不要でClaudeを使い、マーケティング資料の自己レビュー、契約書のリドライン、利益相反審査、プライバシー影響評価(PIA)作成という4つの反復業務をワークフロー化した。Slackに組み込んだセルフサービスツールやGoogle Docs連携、過去文書を参照するMCPサーバーを組み合わせることで、マーケティング資料の審査ターンアラウンドを2〜3日から24時間に短縮した。

## 設計のポイント

- 法務チーム独自の過去のガイダンスやレビュー観点を『Skill』としてファイル化し、文書種別ごとにClaudeへ読み込ませることで属人化していた審査基準を再利用可能にした
- MCPサーバー経由でGoogle Driveの過去PIAフォルダに接続し、過去文書を参照しながら新規文書のドラフトを生成するRAG的な構成を採用した
- リスクを低・中・高でフラグ付けした一次レビュー結果を提示し、最終判断は必ず人間の弁護士が行うヒューマンインザループを維持した
- 新しい専用UIを作らず、SlackやGoogle Docsなど既存の業務ツールにClaudeを直接組み込むことで導入の摩擦を減らした

## 使いどころ

- マーケティング・広報コンテンツを法務レビュー前に自己点検し、担当者への差し戻し回数を減らしたいチーム
- 契約書の版比較やフォールバック文言の提案など、反復的な契約レビュー業務を抱える法務・契約管理チーム
- 従業員からの副業・兼業申請など利益相反チェックを効率的にトリアージしたいHR・法務部門
- 過去の類似文書を参照しながら新規の定型文書(PIAなど)を作成する必要がある業務チーム
