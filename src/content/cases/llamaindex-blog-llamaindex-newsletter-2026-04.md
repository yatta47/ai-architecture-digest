---
type: announcement
title: 'LlamaIndexニュースレター: ParseBench始動とOpus 4.7のチャート解析ベンチマーク結果'
title_original: LlamaIndex Newsletter 2026-04-21
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
components:
- ParseBench
- LiteParse
- LlamaParse
- Opus 4.7
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2026-04-21
published_at: '2026-07-18'
---

## 概要

LlamaIndexの週次ニュースレターでは、文書OCRベンチマークParseBenchの正式ローンチ、LiteParseの公式ページ開設(GitHubスター4,300超・500ページを2秒でパース)、Anthropic Opus 4.7のParseBenchでのベンチマーク結果(チャート解析+42.3%改善)をまとめて紹介している。LlamaParse Agenticが総合84.9%でトップを維持している。

## 設計のポイント

- TableRecordMatchやChartDataPointMatchなど、表・チャートを列見出しキーや実数値単位で評価する専用メトリクスを新設した
- 欠落・幻覚・読み順違反という3つの失敗モードを16万7000件超のルールベーステストで検証し、内容の忠実性を定量化する

## 使いどころ

- 新しいLLM/VLMが出るたびに文書解析性能を横比較したいエンジニアリングチーム
- 自社の文書処理パイプラインにどのモデル・パーサーを採用すべきか判断材料が欲しい開発者
