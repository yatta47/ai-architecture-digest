---
type: case
title: 多様な形式の医療報告書から保険金額をリアルタイム推定するエージェント型保険金審査ボット
title_original: Revolutionizing Medical Insurance Analysis with Agentic Claim Estimation
company: Scaleport AI
industry: financial-services
cloud: []
patterns:
- document-processing
- ai-agent
- rag
components:
- LlamaIndex
- LlamaParse
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/revolutionizing-medical-insurance-analysis-with-agentic-claim-estimation
published_at: '2026-07-19'
---

## 概要

Scaleport AIは旅行保険大手Tripinsurance向けに、手書き・スキャンPDF・画像など多様な形式の医療報告書をLlamaParseの高度なOCRで解析し、除外条件チェック・妥当性評価・類似ケース検索・価格推定を行うエージェント型の保険金審査ボットを構築。処理時間を20〜40分から10分へ、50〜75%短縮し、処理件数を倍増させた。

## 設計のポイント

- 手書きノートや低品質スキャンでもテーブル・図表のフォーマットを保持したままOCR抽出し、事前定義フィールドにマッピングする
- 除外条件チェック・妥当性評価・類似ケース検索・価格推定という4つの判断ステップをエージェントの機能として分解している
- ベクトル検索とハイブリッド検索を組み合わせ、地域別の治療費推定など過去データに基づく判断を行う

## 使いどころ

- 非定型フォーマットの医療書類を大量かつ迅速に処理する必要がある保険金請求審査業務
- OCR精度が課題になっていた手書き・スキャン文書主体のクレーム処理プロセス
