---
type: announcement
title: ParseBench-2：重大度で重み付けした文書パース精度ベンチマーク
title_original: Introducing ParseBench-2
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
components:
- ParseBench
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-parsebench-v2
published_at: '2026-11-12'
---

## 概要

LlamaIndexは文書パースの評価指標ParseBenchの第2版を公開した。数値の誤り(75%→57%)など致命的な誤りを重く、表現形式の違いを軽く扱う重大度重み付け指標を導入し、新しいパーサーも比較している。

## 設計のポイント

- 人間の判断に合わせ、誤りの重大度で重み付けして採点する。
- 価格と性能のパレートフロンティアで比較する。
- 評価対象を拡張し、パーサーの実力差を明確にする。

## 使いどころ

- 文書パーサー選定を行うRAG/文書処理チーム。
- OCRや抽出精度を定量比較したい開発者。
- 独自の評価指標を設計する担当者。
