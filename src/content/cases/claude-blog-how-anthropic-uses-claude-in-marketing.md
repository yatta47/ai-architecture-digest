---
type: case
title: Claude Codeによる広告クリエイティブ・コピー生成の自動化
title_original: How Anthropic's Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- Claude Code
- Figma
- Google Ads
- Google Sheets
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-anthropic-uses-claude-marketing
published_at: '2026-01-26'
---

## 概要

Anthropicの成長マーケティング担当Austin Lauは、非エンジニアながらClaude Codeを使い、Figmaでの広告クリエイティブ変体生成プラグインと、Google広告向けのコピー生成ワークフローを構築した。これにより1件あたり30分かかっていた広告制作作業が30秒に短縮され、より多くのコピー実験とブランド整合性の検証に時間を割けるようになった。

## 設計のポイント

- 小さく反復的な作業(コピー&ペーストの繰り返し)から着手し、Figmaプラグインという単一目的のツールに落とし込む
- カスタムスラッシュコマンド(/rsa)とAgent Skillsでブランドトーンや文字数制約などのドメイン知識を組み込み、出力の質を担保する
- 生成結果はあくまで叩き台とし、人間が反復的にレビュー・推敲してから広告出稿用CSVへ変換する

## 使いどころ

- 非エンジニアのマーケターが定型的なクリエイティブ・コピー生成業務を自動化したい場面
- 厳格な文字数制約やブランドガイドラインを守りつつ大量の広告バリエーションを作成する必要がある運用
- 既存のキャンペーン実績データを踏まえて訴求文言をブレインストーミングし、レビューを経て配信する承認フロー
