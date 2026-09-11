---
type: case
title: 資産運用大手がClaudeを投資調査・ツール開発に組み込む
title_original: T. Rowe Price brings more of Claude to its investment process
company: T. Rowe Price
industry: financial-services
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- Claude
- Claude Cowork
- Claude Code
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/t-rowe-price-brings-more-of-claude-to-its-investment-process
published_at: '2026-09-10'
---

## 概要

資産運用会社T. Rowe Priceが、ポートフォリオマネージャー・アナリストの調査業務にClaudeとClaude Coworkを、投資ツール開発にClaude Codeを導入した。リサーチの要約や知識集約的なマルチステップ業務を支援しつつ、人間の判断とアカウンタビリティを中心に据えたガバナンス体制の下で運用している。

## 設計のポイント

- 各AI活用はビジネス部門がオーナーシップを持ち、全社のAIガバナンス基準の下で統制する体制にする
- リサーチ要約やマルチステップ業務ではAIが下調べを担い、最終判断は人間のアナリスト・PMに残す
- 投資部門向けツール開発そのものをClaude Codeで内製し、開発ツールと業務ツールの両輪でAIを組み込む

## 使いどころ

- 大量の情報を読み込み判断する必要があるファンダメンタルズ調査を担うアナリスト・PM
- 投資・運用業務を支援する社内ツールを素早く開発したい社内開発チーム
