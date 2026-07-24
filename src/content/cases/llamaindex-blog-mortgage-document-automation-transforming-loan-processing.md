---
type: guidance
title: 住宅ローン審査文書処理を自動化するインテリジェントドキュメント処理
title_original: 'Mortgage Document Automation: Transforming Loan Processing'
industry: financial-services
cloud: []
patterns:
- document-processing
- human-in-the-loop
components: []
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/mortgage-document-automation
published_at: '2026-07-18'
---

## 概要

給与明細・銀行取引明細・納税申告書など多様な形式の住宅ローン関連書類を、レイアウト理解を伴うインテリジェントドキュメント処理で分類・抽出し、複数文書間の整合性検証と信頼度スコアリングを経て人手レビューに回すワークフローを解説。

## 設計のポイント

- 文書の種類ごとに異なる抽出・検証ロジックを適用するため分類ステージを最初に設ける
- 収入や融資額など複数文書間でのクロスドキュメント照合をルール化する
- 信頼度スコアが低い抽出結果のみ人手レビューに回すヒューマン・イン・ザ・ループ設計

## 使いどころ

- 審査文書の形式が多様でテンプレート方式が破綻している住宅ローン審査
- 監査証跡と規制順守が求められるローン処理チーム
