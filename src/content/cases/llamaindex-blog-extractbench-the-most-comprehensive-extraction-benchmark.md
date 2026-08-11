---
type: announcement
title: 文書抽出の本番運用品質を測るベンチマークExtractBenchと新層Agentic Plusを公開
title_original: 'ExtractBench: The Most Comprehensive Extraction Benchmark'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
components:
- LlamaExtract
- ExtractBench
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-extractbench
published_at: '2026-08-11'
---

## 概要

人がチェックせず自律的に動くエージェントが業務文書を処理する時代には、文書抽出は人間のレビューがあった頃より高い精度基準を満たす必要がある。LlamaIndexは8業務領域・67文書種別にわたる370件(4,869ページ)の実企業文書を用い、長尺文書の網羅性・実スキャンや手書き文字・単語/ページ単位のグラウンディング・コストを同時に評価する初のオープンベンチマークExtractBenchを構築し、フロンティアVLM・コーディングエージェント・専用抽出APIなど14システムを評価した。あわせて、このベンチマークで首位となる新しいLlamaExtract層Agentic Plus(value F1 95.6%、ページあたり8.1セント)を発表した。

## 設計のポイント

- 固定フィールドの復元精度だけでなく、未知スキーマへの対応・視覚的グラウンディング・ページあたりコストまで含めて評価軸を分離する
- タスクの難易度・入力の見た目(スキャン/手書き)・表構造・文書長・業務ドメインという5つの独立した軸でタグ付けし、低スコアの原因を追跡可能にする
- どの抽出システムの出力も正解として信用せず、複数システムの合意・データファーストで生成した合成データ・人手レビューという3系統で正解データを構築する

## 使いどころ

- 人手のレビューなしで自律的に業務文書を処理するエージェントの抽出精度を検証したいチーム
- スキャンや手書きを含む実務文書でのモデル/APIの精度とコストを比較検討したい場合
- 百ページを超える長尺文書での網羅性(尻切れ抽出)を評価したい場合
