---
type: guidance
title: チャート画像から数値データを抽出する方法と、従来OCRでは不可能な理由
title_original: 'Extracting Data From Charts: A Step-by-Step Guide'
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaParse
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/extracting-data-from-charts
published_at: '2026-07-19'
---

## 概要

棒グラフや円グラフの値は文字ではなく『高さ』や『角度』という視覚的関係として符号化されているため、軸ラベルは読めても数値そのものは復元できないのが従来OCRの限界である。手動・従来OCR・VLM(LlamaParse等)の3手法を比較し、グラフ種別の識別から軸・凡例の読み取り、データ点の記録、構造化出力までの抽出手順と検証方法を解説する。

## 設計のポイント

- チャート抽出は幾何学的な座標変換問題であり、テキスト認識(OCR)とは別の能力が必要と明確に切り分ける
- 積み上げ棒グラフの合計と本文中の数値との突合など、抽出後の妥当性検証を工程として組み込む
- 抽出した値ごとに元のグラフ画像への参照(引用・信頼度スコア)を残し、後から差異を追跡できるようにする

## 使いどころ

- 決算資料や業界レポートのグラフから数百点規模のデータを人手を介さず抽出したいアナリスト業務
- スキャンされた古いレポートや低解像度PDFからチャートデータを再利用したい調査チーム
