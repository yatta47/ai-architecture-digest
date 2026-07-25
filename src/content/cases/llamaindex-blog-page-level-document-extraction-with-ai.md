---
type: announcement
title: LlamaExtractのページ単位抽出で200ページ文書の『どこから来た数字か』を即座に追跡可能にする
title_original: 'Beyond Full-Text Extraction: Why Page-Level Granularity Matters'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaExtract
- LlamaParse
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/beyond-full-text-extraction-why-page-level-granularity-matters
published_at: '2026-07-19'
---

## 概要

文書抽出はこれまで『非構造化テキストの海に溺れる』か『抽象化されすぎて出典を追えない要約』の二択だったのに対し、LlamaExtractのページ単位抽出機能は各ページを独立した抽出単位として扱い、バウンディングボックスと引用付きで抽出値をページに紐づける。SEC提出書類分析、M&A契約レビュー、臨床試験文書、保険金請求、不動産デューデリジェンスなど監査証跡が必要な業務での活用例を挙げている。

## 設計のポイント

- 文書全体を一つの塊として要約するのではなく、ページごとに独立した抽出単位として扱いつつスキーマの一貫性を維持する設計にした
- 抽出結果にバウンディングボックスと引用を必ず付与し、『この数字はどこから来たのか』という監査時の質問にワンクリックで答えられるようにした
- 自然言語プロンプトからスキーマを自動生成する機能で、JSONを手書きする手間を省いている

## 使いどころ

- 10-K等の財務諸表から数値を抽出し、出典ページを監査担当に即座に示したい investment analyst
- 数百件規模の契約書から特定条項だけを拾い読みしたい法務のM&Aデューデリジェンス
- 臨床試験文書や保険金請求書類で、規制当局からの照会に出典付きで即答したいコンプライアンス担当
