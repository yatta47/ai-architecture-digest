---
type: announcement
title: スキーマ駆動の文書抽出エージェント Extract v2.5（専用ハーネスと根拠付け）
title_original: Introducing Extract v2.5
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- eval
components:
- LlamaIndex Extract
- ExtractBench
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-extract-v2-5
published_at: '2010-05-01'
---

## 概要

LlamaIndexがスキーマ駆動の文書抽出エージェントExtract v2.5を公開した。文書抽出専用のエージェントハーネスにより全ティアで精度が向上し、AgenticとAgentic Plusには根拠箇所を示すAdvanced Citationsが加わった。ページ単価は据え置きで、長いリスト・ページ跨ぎ・スキャン帳票での改善が示されている。

## 設計のポイント

- 文書の種類・レイアウト・情報密度に応じて推論量を変えるStructural Reasoningで、複雑な文書にだけ労力を割く。
- 中間表現で全件を保持しスキーマに照らして検証し、長いリストの取りこぼしを防ぐ。
- 抽出値のバウンディングボックスを返すCitationsで、人手の突き合わせを可能にする。

## 使いどころ

- ファンド報告書など数十ページにわたる反復レコードを漏れなく構造化したい場面。
- 手書き注記や修正跡が混在するスキャン帳票から正規値だけを取り出したい業務。
- 抽出結果の根拠確認が求められる規制・監査対応の文書処理。
