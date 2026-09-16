---
type: guidance
title: 抽出精度が上がっても自動化率は上がらない、文書処理はルーティングゲートで決まる
title_original: A 97% Accurate Extractor Can Still Leave Half Your Documents in the Queue
industry: cross-industry
cloud: []
patterns:
- document-processing
- human-in-the-loop
- eval
components:
- Amazon Textract
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ocr-document-processing-review-queues
published_at: '2026-09-16'
---

## 概要

文書処理パイプラインではフィールド単位の抽出精度をいくら上げても、文書単位のストレートスルー処理率(人手を介さず処理できる割合)は必ずしも向上しない。20フィールドの請求書なら97%のフィールド精度でも文書丸ごと正しい確率は約54%にとどまり、どの46%が誤っているかを教えてくれるのはモデルの正確さではなくフィールド単位の信頼度シグナルであると論じる。

## 設計のポイント

- 文書単位のストレートスルー処理率はフィールド精度ではなく信頼度シグナルの分離性能で決まる
- 信頼度シグナルはページ単位ではなくフィールド単位で提供しないと、レビュー担当者がどの値を確認すべきか分からず文書全体が人手に回る
- 厳密なキャリブレーションよりも、誤った値が正しい値より低いスコアになる「分離性」の方が閾値運用には実用的
- 補正ログに対して閾値をスイープし、フラグ付き集合が実際の誤りをカバーする点を運用的に見つける

## 使いどころ

- OCRベンダーを精度指標だけで比較・選定しようとしている調達担当者
- 抽出モデルを改善したのに例外キューが減らない原因を診断したい運用チーム
- 文書自動化のROIをストレートスルー処理率で説明したいプロダクトオーナー
