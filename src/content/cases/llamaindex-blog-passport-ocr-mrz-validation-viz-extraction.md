---
type: guidance
title: MRZチェックサム検証で信頼性を担保するパスポートOCR
title_original: 'Passport OCR: MRZ Validation & VIZ Extraction'
industry: cross-industry
cloud: []
patterns:
- document-processing
- guardrails
components: []
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/passport-ocr
published_at: '2026-07-18'
---

## 概要

パスポートには目視用のVisual Inspection ZoneとICAO標準のチェックサム付きMachine Readable Zone(MRZ)の2つの記録があるが、多くの実装は文字を抽出するだけでチェックデジット検証やVIZ-MRZの相互照合を行わずに「成功」と報告してしまう。記事はチェックサム検証・フィールド境界の固定・相互照合をエージェント型オーケストレーションに組み込むことで、改ざん検知や読み取り不能箇所の補完ができると説明する。

## 設計のポイント

- MRZの各フィールドをICAO 9303が定めるmodulo-10チェックデジットで検証し、単なる文字抽出と区別する
- VIZとMRZの値を独立に抽出するのではなく相互に突合し、片方が破損していてももう片方から補完する
- 非ラテン文字（アラビア語・中国語・キリル文字）を検知してスクリプトに応じたモデルへルーティングする

## 使いどころ

- 審査キューを持たずリアルタイムで本人確認したい旅行・宿泊業のチェックイン
- デジタル本人確認プラットフォームや政府機関の大量入国審査でのなりすまし検知
