---
type: case
title: Claude Codeで作った営業担当者向けメール自動下書きエージェント「CLAFTS」
title_original: How one Anthropic seller rebuilt his team's workflows with Claude Code
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- human-in-the-loop
components:
- Claude Code
- Claude API
- Claude Cowork
- Agent SDK
- Gmail
- Google Drive
- Google Calendar
- MCP
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering
published_at: '2026-06-05'
---

## 概要

コーディング未経験だったAnthropicの営業担当Jared Siresが、Claude CodeでGmail上に常駐するメール自動下書きツール「CLAFTS」を開発した。CLAFTSはGoogle Driveや社内資料をコンテキストとして参照し、Web検索で最新の製品ドキュメントを取得しながら本人の文体に合わせた返信を生成し、1日あたり数時間の作業時間削減につながった。この成功を機にJaredはGTMプロダクトマネージャーとなり、商談準備や議事録フォローアップを自動化するスキルをMCPサーバー経由でカレンダーやCRMと連携させ、Claude Coworkのプラグインとして営業チーム全体に展開している。

## 設計のポイント

- システムプロンプトを何百回も反復調整し、AIの出力を本人の文体・トーンに合わせ込む
- Web検索で常に最新の製品ドキュメントを参照させ、頻繁な仕様変更にも回答の鮮度を追従させる
- MCPサーバー経由でカレンダーやCRMに接続し、朝夕のブリーフ／リキャップ生成を自動化する
- 生成した下書きは必ず人がレビューしてから送信する運用とし、Human-in-the-loopを維持する

## 使いどころ

- 大量の顧客アカウントを抱える営業担当者の受信箱対応・返信ドラフト作成を自動化したい場合
- 商談前に顧客背景をリサーチしトークポイントを準備したい場合
- 会議メモやドキュメントから議事録フォローアップメールを自動生成したい場合
- 個人が作った便利ツールを組織全体のプラグインとして横展開したい場合
