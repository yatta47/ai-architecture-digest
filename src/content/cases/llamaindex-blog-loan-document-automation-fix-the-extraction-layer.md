---
type: guidance
title: ローン審査自動化はAI意思決定より先に抽出層を直すべき理由
title_original: 'Loan Document Automation: Fix the Extraction Layer'
industry: financial-services
cloud: []
patterns:
- document-processing
components: []
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/loan-document-automation
published_at: '2026-07-18'
---

## 概要

AI意思決定を導入しても抽出層が従来型OCRのままだと審査担当者は依然として40〜60%のファイルを手作業でレビューしており、ボトルネックが分類から条件確認に移動しただけになっている。テンプレート依存の従来型OCRは書式が変わると壊れるのに対し、エージェント型OCRは各要素に最適なモデルを動的に選び、隣接データとの整合性検証まで行う「推論の問題」として捉え直す。

## 設計のポイント

- 抽出の前に混在アップロードされたページ群を書類種別ごとに分類する専用ステップを設ける
- 銀行明細のように発行元ごとにレイアウトが異なる文書は、テンプレート学習ではなく文書構造への意味理解で対応する
- 手書き記入欄や複数ページにまたがる税務書類など、構造認識なしでは誤読が起きやすい箇所を明示的に扱う

## 使いどころ

- 月間数百件規模の住宅ローン・商業ローン審査で人手レビューを削減したい金融機関
- 自営業者や外国籍申請者など非定型書類が多い審査フローの自動化
