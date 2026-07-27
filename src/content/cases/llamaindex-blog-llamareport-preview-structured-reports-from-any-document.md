---
type: announcement
title: 任意のドキュメントを構造化レポートに変換するLlamaReport
title_original: 'LlamaReport preview: Transform any documents into structured reports'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- human-in-the-loop
- parallel-execution
components:
- LlamaParse
- LlamaReport
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamareport-preview-transform-any-documents-into-structured-reports
published_at: '2026-07-20'
---

## 概要

LlamaIndexがベータ公開したLlamaReportは、ソース文書とテンプレートを与えるとLlamaParseによる文書解析からレポート生成、LLMによる編集提案までを一気通貫で行うAPIファースト製品。従来のRAGが単発の質問応答に留まっていたのに対し、業務でそのまま使える構造化レポートの自動生成を狙う。

## 設計のポイント

- 文書とテンプレート（Markdown/質問票/既存記事など柔軟な形式）を入力に、まず生成計画（プラン）を作ってから並列実行でレポートを組み立てる
- レポート全体を書き直すのではなく、部分編集とその根拠提示によるLLMアシスト編集を可能にした
- プラン生成・レポート生成・編集の各ステップをストリーミングイベントで公開する開発者向けAPIを用意した

## 使いどころ

- 決算資料やSEC提出書類から企業レポートを作成する金融アナリスト
- 業界調査から顧客向け資料を合成するコンサルタント
- 製品ドキュメントやAPIガイドを文書群から自動生成・保守したい開発チーム
