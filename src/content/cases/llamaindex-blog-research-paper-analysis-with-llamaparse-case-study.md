---
type: case
title: Arcee AI、LlamaParseで400万ページのNLP論文をLLMファインチューニング用データセット化
title_original: 'Case Study: Streamlined Research Paper Analysis with LlamaParse at Arcee AI'
company: Arcee AI
industry: other
cloud: []
patterns:
- document-processing
- fine-tuning
- prompt-optimization
components:
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/case-study-streamlined-research-paper-analysis-with-llamaparse-at-arcee-ai
published_at: '2026-07-22'
---

## 概要

小規模言語モデル(SLM)を手がけるArcee AIは、S3上に蓄積した2017年以降のNLP研究論文約400万ページをLlamaParseで解析し、専用LLMをファインチューニングするためのデータセットを構築した。従来のOCRやOSSツールでは表・数式の抽出精度が不足していた課題を、LlamaParseのプロンプトによる抽出指示のチューニングで解決した。

## 設計のポイント

- 表・数式など構造化要素を含むPDFはOCRではなくプロンプト指示可能なパーサーで抽出精度を作り込む
- LlamaIndex側との協働(白手袋対応)で反復的にプロンプトを調整し、幻覚や抜け漏れを段階的に減らす

## 使いどころ

- 大量のPDF論文からLLM学習用データセットを構築したい研究/MLチーム
- 表や数式など複雑なレイアウトを含む文書のデータ化に苦労している企業
