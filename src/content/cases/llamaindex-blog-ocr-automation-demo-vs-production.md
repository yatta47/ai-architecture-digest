---
type: guidance
title: デモの99%が本番で83%に落ちる理由:OCR自動化の3つのアーキテクチャ比較
title_original: 'OCR Automation: Demo vs Production'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- human-in-the-loop
components:
- LlamaParse
- Tesseract
- AWS Textract
- Azure
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ocr-automation
published_at: '2026-08-12'
---

## 概要

LlamaIndexは、ルールベースOCR(Tesseract)・ML系クラウドOCR API(AWS Textract、Azure)・LLMが要素ごとに最適なモデルへルーティングするエージェント的パース(LlamaParse)の3つを比較する。本番精度を左右するのはパース手法そのものより入力品質(解像度300DPI・傾き補正)と信頼度スコアに基づく人手レビューへのルーティングであり、真の指標は精度ではなく『人手介入なしで処理できる割合』だとする。

## 設計のポイント

- 単一モデルに全要素を任せず、テキストはOCR、表はレイアウト認識、グラフはビジョンモデルというように文書要素ごとに最適なモデルへLLMがルーティングするエージェント的アーキテクチャにした。
- スキャン解像度を300DPI以上に標準化し、傾き補正(デスキュー)を前処理として組み込むことで、パース層以前の入力品質を改善した。
- フィールドごとの信頼度スコアで閾値を設定し、低信頼の抽出結果だけを人間レビューへルーティングするhuman-in-the-loopを構築した。
- 精度そのものではなく『人手介入なしで使える割合(ストレートスルー処理率)』を成功指標に据えた。

## 使いどころ

- レイアウトが一定で単一文書種別を高ボリューム処理する場合はルールベースOCRで十分な現場。
- 表・グラフ・混在レイアウトなど複雑な文書が多く、単一のOCR APIでは精度が頭打ちになっている企業。
- デモでは99%出ていた精度が実文書コーパスで83%に落ち込むなど、本番運用に向けて精度低下の要因を切り分けたいチーム。
