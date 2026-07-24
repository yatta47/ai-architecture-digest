---
type: guidance
title: Claude 2.1の200Kコンテキストで検索精度を高めるプロンプト技術
title_original: Long context prompting for Claude 2.1
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
- context-engineering
components: []
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-2-1-prompting
published_at: '2023-12-06'
---

## 概要

Claude 2.1は200Kトークンのコンテキスト内に埋め込まれた文脈から外れた一文の想起を拒否しがちだったが、回答冒頭に「最も関連する文はこちらです」という一文を追加するプロンプト調整だけでNeedle-in-a-Haystack評価の正答率が27%から98%に向上したという実験結果を報告する。

## 設計のポイント

- 長文コンテキストでの検索拒否を防ぐため回答の書き出しを誘導するプレフィックスを追加する
- 『根拠不十分なら答えない』という安全側の学習が長文検索の妨げになり得る点を評価で切り分ける
- 文書内の挿入位置による結果のブレを見るため文書順序をランダム化して再現性を検証する

## 使いどころ

- 長大な契約書や規制文書から特定の一文を正確に抽出したい場合
- Needle-in-a-Haystack的な長文検索精度をプロンプト調整のみで改善したいLLM導入チーム
