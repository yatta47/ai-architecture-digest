---
type: case
title: Anthropic財務チームのClaude Cowork活用：決算資料の整合性チェックと月次コメント自動下書き
title_original: How Anthropic's finance team uses Claude to shape the narrative behind the numbers
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- context-engineering
- document-processing
- human-in-the-loop
components:
- Claude Cowork
- Claude for Excel
- Google Workspace
- Slack
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-anthropics-finance-team-uses-claude-to-shape-the-narrative-behind-the-numbers
published_at: '2026-05-22'
---

## 概要

Anthropicの企業財務チームが、四半期取締役会資料や月次財務レビューの数値と文章の整合性チェックにClaude Cowork、財務モデルの診断にClaude for Excelを活用している事例。ナラティブの整合性検証を自動化することで週10〜20時間を判断業務に振り向けられるようになったという。

## 設計のポイント

- Claude Coworkに決算資料全体を渡し、すべての数値・主張が単一の正データソースと整合しているかを検証させ、取締役会メンバーの視点で文脈依存の記述や自己矛盾を指摘させる
- 月次レビューでは前月のドキュメントを参照させることで、数値だけでなく文章のトーンの一貫性も維持する
- ドキュメント・メール・Slackなど部署横断のコンテキストをプロジェクトメモリに蓄積し、意思決定の経緯を後から参照できるようにする
- 用途（月次レビュー用・取締役会資料用）ごとに別プロジェクトを分け、トーンや慣習に合わせたメモリを個別に管理する

## 使いどころ

- 複数人が同時編集する決算資料で、数値更新のたびに全体の整合性を手作業で再チェックする負担を減らしたいチーム
- 月次の定型的な財務コメント下書きを、確立された文体で毎回一から書く手間を省きたい財務チーム
