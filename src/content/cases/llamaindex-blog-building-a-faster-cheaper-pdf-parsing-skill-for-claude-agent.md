---
type: case
title: トレース分析で改善したClaude Agent向けPDF解析スキルの高速化
title_original: Building a Better LiteParse Skill with Evals
company: LlamaIndex
industry: financial-services
cloud: []
patterns:
- eval
- prompt-optimization
- document-processing
components:
- Claude Agent SDK
- LiteParse
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-a-better-liteparse-skill-with-evals
published_at: '2026-07-18'
---

## 概要

LlamaIndexはClaude AgentにLiteParseをPDF解析スキルとして組み込み、ESG報告書QAベンチマークでの実行トレースを分析して同一PDFの再パースやOCRの無駄な有効化などのアンチパターンを特定した。ルールを固定化した改良版スキルにより、回答品質を上げながらコストを37%削減した。

## 設計のポイント

- PDFを一時ファイルに一度だけパースし、以降はそのファイルをgrep/sedで検索させることで再パースを防ぐ
- デジタル生成PDFにはOCRを無効化し、スクリーンショット読み込みは最後の手段かつ低解像度・単一ページに限定する
- grepとsedの往復ターンを減らすため、コンテキストをまとめて取得するコマンド化と検索回数の上限（3回で打ち切りBM25へフォールバック）を導入する

## 使いどころ

- コーディングエージェントにPDF解析ツールをスキルとして組み込む際の設計指針
- トレース分析に基づいてエージェントのツール利用パターンを継続的に改善したいLLMOpsチーム
