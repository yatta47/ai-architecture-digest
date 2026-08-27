---
type: case
title: 資金・流動性・資本を横断してファイナンスに文脈を与えるAIコワーカー
title_original: How capital-markets finance protects balance-sheet returns
industry: financial-services
cloud: []
patterns:
- ai-agent
- context-engineering
- decision-execution
components:
- Databricks Genie
- FIBO
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-capital-markets-finance-protects-balance-sheet-returns
published_at: '2026-08-25'
---

## 概要

セルサイドの資金・流動性・資本消費・収益性はデスクP&L、資金調達カーブ、リスクエンジンなど別々のシステムから出てくるため、Databricks Genie Oneは金融業界オントロジー（FIBOなど）とガバナンス済みの業務定義を基盤に、数値の背後にあるデスク・ポジション・定義・元データをファイナンス部門が直接質問して追跡できるようにする。ある大手グローバル銀行では流動性レポーティングの規制データ処理時間が10時間から8分に短縮され、市場変化への対応が迅速になった。

## 設計のポイント

- FIBOのような業界標準オントロジーとガバナンス済みの業務定義を組み合わせ、フロントオフィス・トレジャリー・リスク・規制報告の間で数値の意味を統一的に読めるようにする
- AIコワーカーは分析結果の読み上げで終わらせず、資金・担保の再配分や数値の裏付け提示など次のアクションに直結する形で設計する
- 価格付け・資金調達・リスク・資本の意思決定権限は人間の責任者に残し、AIは問いと文脈と後続作業の速度を市場の動きに合わせる役割に限定する

## 使いどころ

- デスクが気づく前に資金・流動性の逼迫の兆候を追跡したいトレジャリー・ファイナンス部門
- 規制当局や監査人からの説明要求に即座に根拠データを提示したい資本市場のファイナンスチーム
