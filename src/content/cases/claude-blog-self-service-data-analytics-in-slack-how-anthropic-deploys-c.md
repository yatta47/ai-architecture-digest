---
type: case
title: AnthropicがClaude TagでSlack上のセルフサービス・データ分析エージェントを展開する方法
title_original: 'Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- text-to-sql
components:
- Claude Tag
- Claude Code
- Slack
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
published_at: '2026-08-13'
---

## 概要

Anthropicのデータチームは、Claude Codeで実現した約95%精度のデータ分析基盤(統制されたセマンティックレイヤー、スキルファイル、評価スイート)を、非アナリストも使うSlack上のClaude Tagに展開した際の学びを共有する。スキルファイルをデータモデルと同じ頻度で継続的に読み直させる、集計スキルだけでなく予測・コホート分析・可視化の作法までスキル化する、社内ナレッジインデックスに接続して数値変動の背景を説明できるようにする、サービスアカウントの権限を意図的に絞るなど、Slackという文脈情報の乏しい場での回答精度と権限設計を扱う。

## 設計のポイント

- スキルファイルを『一度配布したら終わり』ではなく『提供コンテンツ』として扱い、会話のたびにディスク上のスキルディレクトリを読み直させることでデータモデルの変更に追随する
- 『どのテーブルを使うか』の知識スキルだけでなく、予測・コホート分析・ファネル分析・可視化・分析文章の書き方といった『アナリストならどう分析するか』のランブックスキルを追加する
- 指標の変動理由を説明するため、データウェアハウスだけでなく社内のインシデント記録やSlackスレッドを検索できるナレッジインデックスに接続する
- Claude Tagはサービスアカウントとしてウェアハウスにアクセスし行レベルセキュリティが効かないため、チャンネル参加権限や質問範囲を意図的に設計して権限を絞る

## 使いどころ

- 分析専任者ではない社内の非技術者にセルフサービスでデータ分析を提供したい組織
- 既存のCLI/エージェント向けに構築した精度の高いデータ分析基盤をチャット上に横展開したいデータチーム
- 指標変動の『なぜ』を単なる数値だけでなく社内文脈と合わせて説明したい場面
