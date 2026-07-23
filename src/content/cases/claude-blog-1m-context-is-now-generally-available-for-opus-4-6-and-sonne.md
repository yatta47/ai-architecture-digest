---
type: announcement
title: Claude Opus/Sonnet 4.6、100万トークンコンテキストを追加料金なしでGA化
title_original: 1M context is now generally available for Opus 4.6 and Sonnet 4.6
company: Anthropic
industry: cross-industry
cloud:
- aws
- gcp
- azure
patterns:
- context-engineering
- llmops
components:
- Claude Opus 4.6
- Claude Sonnet 4.6
- Claude Code
- Amazon Bedrock
- Google Cloud Vertex AI
- Microsoft Foundry
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/1m-context-ga
published_at: '2026-03-13'
---

## 概要

Claude Opus 4.6とSonnet 4.6の1Mトークンコンテキストウィンドウが標準料金のままGA提供された。長文コンテキストの圧縮・要約が不要になり、Claude Codeではコンパクション頻度が減少するなど、長時間稼働エージェントの実運用に効果が出ている。

## 設計のポイント

- コンテキスト長に応じた課金階層をなくし、900Kトークンでも9Kトークンと同一単価にすることで長文活用の心理的障壁を下げる
- MRCR v2などlong-context検索精度のベンチマークを公開し、単なるウィンドウ拡大ではなく実利用での再現性を担保する
- 既存のbetaヘッダー付きリクエストをそのまま許容し、移行コストなしで大規模コンテキストに切り替えられるようにする

## 使いどころ

- コードベース全体やログ・トレースを圧縮せず1回のセッションで扱いたいエージェント開発チーム
- 数百ページの契約書・判例・論文を横断的に参照する必要がある法務・研究系ワークロード
