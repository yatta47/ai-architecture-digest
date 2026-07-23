---
type: announcement
title: ClaudeのCoworkをプラグインで職務特化型アシスタントに拡張
title_original: Customize Cowork with plugins
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Claude Cowork
- Claude Code
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/cowork-plugins
published_at: '2026-01-30'
---

## 概要

AnthropicはClaude Coworkにプラグイン機能を追加し、スキル・コネクタ・スラッシュコマンド・サブエージェントをひとまとめにして、営業・法務・財務などの職務に特化したAIアシスタントを作れるようにした。プラグインはファイルベースで作成・編集・共有が容易で、CRMや社内ナレッジベースへの接続、業務プロセスの再現、決まった作業のコマンド化などを一度定義すれば以降のやり取りで自動的に活用される。まずは社内で使われている11種類のプラグインをオープンソースで公開し、有料ユーザー向けのリサーチプレビューとして提供を開始した。

## 設計のポイント

- スキル・コネクタ・スラッシュコマンド・サブエージェントをファイルベースの1パッケージにまとめ、チームで再利用・共有できるようにする
- 職務固有のプロセスやツール接続を一度プラグインとして定義すれば、以降の関連するやり取りすべてで自動的にそのコンテキストが参照される
- 自社で使っているプラグインをオープンソースの出発点として提供し、ユーザーが自分のチーム向けにカスタマイズできるようにする

## 使いどころ

- 営業・法務・財務・マーケティングなど特定職務向けにAIアシスタントの振る舞いを標準化したいチーム
- CRMや社内ドキュメントなど既存ツールに接続した定型業務をスラッシュコマンドとして配布したい場合
- 組織全体でベストプラクティスを一貫させ、管理者がプロセス徹底に費やす時間を減らしたい場合
