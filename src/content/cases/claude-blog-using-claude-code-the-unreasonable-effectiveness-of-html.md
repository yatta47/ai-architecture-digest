---
type: guidance
title: Claude Codeの成果物にMarkdownでなくHTMLを使う理由
title_original: 'Using Claude Code: The unreasonable effectiveness of HTML'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- context-engineering
- spec-driven-development
components:
- Claude Code
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
published_at: '2026-05-20'
---

## 概要

Claude Codeチームのメンバーが、Markdownに代わり出力形式としてHTMLを選ぶ理由と使い方を紹介する記事。HTMLは表・SVG図・CSS・インタラクション要素などMarkdownより高い情報密度と視認性を持ち、リンク共有もしやすいため、100行を超える仕様書やプランをレビューしやすくする。ブレインストーミング→モックアップ→実装計画という一連の作業をHTMLファイル群として作り、次のセッションにそのまま文脈として渡す運用パターンを提案している。

## 設計のポイント

- 100行を超える仕様書やプランはMarkdownより表・SVG図・CSSを使えるHTMLの方が構造的に読みやすく、レビューされやすい。
- ブレインストーミング→デザイン案比較→モックアップ→実装計画という一連の成果物をHTMLファイル群として蓄積し、次のセッションにまとめて文脈として渡す。
- HTMLにスライダーやノブなどの操作要素を組み込み、人間が調整した結果をそのままプロンプトへコピーバックできるようにする。
- ファイルシステムやMCP(Slack/Linearなど)、ブラウザ、Git履歴から集めた情報をHTMLの図として要約させ、大きなコンテキストを人が消化しやすい形に変換する。

## 使いどころ

- 設計案の比較検討や実装計画の作成など、仕様策定・探索フェーズのドキュメント化。
- 同僚やチームにレビューしてもらう際、添付ファイルではなくリンクで共有して読んでもらいたいとき。
- パラメータやレイアウトを対話的に調整しながら意思決定したいデザインレビューや設定調整の場面。
- 複数ファイルやツールから集めた情報を1つの可読な成果物にまとめて別セッションへ引き継ぎたいとき。
