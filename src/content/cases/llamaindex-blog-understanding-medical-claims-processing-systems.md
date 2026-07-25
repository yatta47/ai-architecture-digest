---
type: guidance
title: 医療請求の否認はコーディングではなく書類取り込み時のOCRに起因する
title_original: Understanding Medical Claims Processing Systems
industry: healthcare
cloud: []
patterns:
- document-processing
components: []
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/medical-claims-processing-systems
published_at: '2026-07-18'
---

## 概要

米国病院は年間2620億ドル相当の請求否認・過小支払いを計上しているが、その多くはコーディングミスではなくCMS-1500やUB-04のようなグリッド様式フォームを標準OCRが列単位で誤読することに起因する。ICD-10の1文字違いやボックス境界の誤認識が否認の原因になっているのに、請求担当者はそれを「コーディングの誤り」として扱ってしまい根本原因が見えなくなっている。

## 設計のポイント

- OCRの出力をICD-10/CPTコードのフォーマットパターンと照合し、構造的に無効な値をそのまま下流に流さない
- グリッド形式の明細表はボックス境界を認識した上で列を対応付け、隣接フィールドの混線を防ぐ
- 紙のEOBとANSI X12 835電子送金通知(ERA)のような異なる形式間の突合を自動化する

## 使いどころ

- 病院の収益サイクル管理(RCM)で否認率を下げたい医事課
- 放射線科・行動医療・麻酔科などコード密度の高い専門診療の請求処理
