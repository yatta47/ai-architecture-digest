---
type: announcement
title: エージェント向け文書パース品質を測る5次元ベンチマーク ParseBench
title_original: 'ParseBench: A Benchmark for Enterprise Document Parsing'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
components:
- LlamaParse
- LlamaParse Agentic
- GPT-5 Mini
- Gemini 3 Flash
- Amazon Textract
- Azure Document Intelligence
- Google Cloud Document AI
- HuggingFace
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/parsebench
published_at: '2026-07-18'
---

## 概要

LlamaIndexが、人手検証済みの約2,000ページ・167,000超のルールからなる文書パース評価ベンチマーク「ParseBench」を公開した。表・グラフ・内容忠実性・意味的書式・視覚的グラウンディングの5次元で14手法を評価し、LlamaParse Agenticが全次元で競争力を持つ唯一の手法(総合84.9%)だったと報告している。データセット・評価コード・論文はすべて公開されている。

## 設計のポイント

- テキスト類似度(BLEU/編集距離)は空白やHTML/Markdownの差を過剰に減点しつつヘッダー転置やグラフのOCR化といった致命的誤りを見逃すため、ダウンストリームでの正しさ(セマンティック正確性)を測る指標を設計する
- 消費側の使い方に沿い、表は「列見出しをキーにしたレコード集合」として扱うTableRecordMatch、グラフは値・系列名・軸ラベルの許容誤差付き照合という評価軸を採用する
- 正解データはフロンティアVLMの自動ラベリング＋人手検証の2段パイプラインで作る

## 使いどころ

- 保険請求審査・財務分析・契約抽出など、エージェントがセル値や書式に基づいて判断する高精度が要る業務に携わる人
- OCR/パーサーの選定を検討している場面
- 自社パイプラインの弱点(欠落・幻覚・表崩れ)を把握したい場面
