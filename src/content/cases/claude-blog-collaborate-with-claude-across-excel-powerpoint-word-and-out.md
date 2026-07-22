---
type: announcement
title: Claude for Microsoft 365によるExcel・PowerPoint・Word・Outlook横断のコンテキスト共有
title_original: Collaborate with Claude across Excel, PowerPoint, Word and Outlook
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- context-engineering
components:
- Claude for Excel
- Claude for PowerPoint
- Claude for Word
- Claude for Outlook
- Claude Enterprise
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook
published_at: '2026-05-07'
---

## 概要

Claude for Excel/PowerPoint/Wordが一般提供、Claude for Outlookがパブリックベータとなり、1つの会話コンテキストを4つのMicrosoftアプリ間で保持できるようになった。Excelの前提を変えるとPowerPointのグラフやWordのメモの数値が自動更新されるなど、ファイルを跨いだ編集が連動する。管理者向けにはOpenTelemetryによる監査ログ連携やアプリ・ユーザー別の利用状況を追えるAnalytics APIも提供される。

## 設計のポイント

- 会話をファイル単位で永続化し、サイドバーを閉じても翌日同じコンテキストから再開できるようにする
- Outlookでは返信案とカレンダー招待を必ず人がレビューしてから送信するhuman-in-the-loopを徹底する
- OpenTelemetryでプロンプト・ツール呼び出し・参照文書を自社コレクターへストリームし、セキュリティ部門が可視化できるようにする

## 使いどころ

- メール確認→文書作成→分析→資料化のように複数アプリを行き来する定型ワークフローを持つナレッジワーカー
- IT/セキュリティ部門が全社導入時の利用状況とガバナンスを監査したい場合
