---
type: announcement
title: Claude Designがブランドの一貫性を保ったままCode/Figma/Canva等と連携し、日常業務の制作フローに定着
title_original: Claude Design now stays on brand for daily work
industry: cross-industry
cloud: []
patterns:
- context-engineering
- guardrails
components:
- Claude Design
- Claude Code
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-design-stays-on-brand-for-daily-work
published_at: '2026-06-17'
---

## 概要

Claude Designは複数のデザインシステムをGitHubリポジトリやデザインファイルから取り込み、生成物を自動的にデザインシステムと照合・修正してからブランドに沿った出力を返すようになった。/design-syncやハンドオフ機能によりClaude CodeとClaude Designの間で作業を同期でき、Adobe・Canva・Figma・Replit・Vercel・Wixなど既存の制作ツールへの連携先も拡充している。

## 設計のポイント

- デザインシステムを取り込み、生成物を自動で規約と照合・修正することで、複数人が並行してデザインを試作してもブランドから逸脱しないようにする。
- デザインとコードの作業をClaude DesignとClaude Codeの間で同期させ、スクリーンショットからの再現ではなく既存の作業をそのまま引き継いで実装に移行できるようにする。
- 管理者ロールで標準デザインシステムを1つに承認・固定できるようにし、大規模チームでの表記ゆれや逸脱編集を防ぐガバナンス機構を設ける。

## 使いどころ

- 複数人が並行してデザイン案を試作する際に、ブランドガイドラインからの逸脱を防ぎたいデザインチーム。
- デザインからコードへのハンドオフで、スクリーンショットからの再現作業に時間を取られているエンジニア。
- デザインシステムを大規模チーム全体で統制し、承認された標準から外れた編集を防ぎたいデザイン責任者。
