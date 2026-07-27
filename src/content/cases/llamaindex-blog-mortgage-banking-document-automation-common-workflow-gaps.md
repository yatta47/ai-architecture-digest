---
type: guidance
title: 住宅ローン書類処理を証跡付きで自動化するエージェント型抽出
title_original: 'Mortgage Banking Document Automation: Common Workflow Gaps'
industry: financial-services
cloud: []
patterns:
- document-processing
- ai-agent
- human-in-the-loop
components: []
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/mortgage-banking-document-automation
published_at: '2026-07-21'
---

## 概要

住宅ローン審査における書類処理自動化は、各ステージ内ではなくステージ間のハンドオフで壊れやすく、OCRの読み取り精度が高くてもデータの出所（プロヴェナンス）を追跡できないと品質管理(QC)や規制対応で致命的な問題になると指摘する。エージェント型の抽出レイヤーに信頼度スコアリングとページ単位の引用を組み込み、抽出結果自体が出所を証明できる監査可能なデータにする設計を提案している。

## 設計のポイント

- 抽出結果にページ単位の引用（どの書類のどこから読み取ったか）を付与し、監査証跡として機能させる
- 信頼度スコアに基づいて人手レビューを疑わしい箇所だけに絞り込み、全件レビューを避ける
- ステージ間のハンドオフでデータの出所が失われないよう、抽出層をエージェント化して各ステージを横断的に検証する

## 使いどころ

- 住宅ローンの引受・クロージングなど、規制上の説明責任が求められる金融書類処理
- OCR自体は正確でも、データの出所を証明できないことがコンプライアンス上のリスクになる業務
