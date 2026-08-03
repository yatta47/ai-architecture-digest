---
type: opinion
title: AnthropicのプロダクトデザイナーがClaude Designで作りこむ前にアイデアを可視化する運用
title_original: How the product designer who built Claude Design uses it to explore ideas before building them
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- context-engineering
components:
- Claude Design
- Claude Opus 5
- Claude Code
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them
published_at: '2026-07-24'
---

## 概要

Anthropicのプロダクトデザイナーは、ブランドガイドをプロンプトに蒸留しClaudeにHTMLを生成させるプロトタイプから始め、それが社内で広くプロダクトモックアップやスライド、アニメーション制作にまで使われるツールClaude Designに育った経緯を紹介する。エンジニアの出荷速度にデザインが追いつくための「作り込む前に探索する」ワークフローが中心的なテーマである。

## 設計のポイント

- ブランドのフォント・色・アセット・原則をプロンプトに事前に蒸留しておき、生成物が自動的にブランド準拠になるようにする
- HTMLを『Webサイトの形式』ではなく汎用の視覚メディアとして扱い、スライドや動画、PDF相当の成果物を同じ生成経路で作る
- コーディング（Claude Code）と可視化・探索（Claude Design）を役割分担し、双方向に同期して行き来できるようにする

## 使いどころ

- 画面遷移のクリックスルー・プロトタイプを状態ごとに手作業でつなぐ代わりに素早く作りたいプロダクトデザイナー
- アイデア出しの場でその場でスライドやビジュアルを作って合意形成を早めたいチーム
