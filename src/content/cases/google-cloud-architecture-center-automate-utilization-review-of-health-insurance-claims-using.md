---
type: guidance
title: 生成AIで医療保険の事前承認(PA)審査を自動化するユーティライゼーションレビュー基盤
title_original: Automate utilization-review of health insurance claims using generative AI
industry: healthcare
cloud:
- gcp
patterns:
- document-processing
- human-in-the-loop
- ai-agent
components:
- Document AI
- Firestore
- Cloud Storage
- Agent Platform
- Gemini API
- Agent Search
outcome:
  type: productivity
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/use-generative-ai-utilization-management
published_at: '2026-07-19'
---

## 概要

医療保険会社の事前承認(PA)申請書をDocument AIで構造化データに変換し、担当者がHuman-in-the-Loopで確認した上で、Gemini APIが臨床レビュー用のプロンプトと推奨判断を生成するユーティライゼーションレビュー(UR)自動化アーキテクチャ。ポリシー文書やケアガイドラインも検索対象として審査担当者に提示する。

## 設計のポイント

- フォーム抽出結果にフィールドレベル・文書レベルの信頼度スコアを付与し、Human-in-the-Loopアプリで人手確認・修正を挟む
- 生成したレビュー用プロンプトをUR担当者が確認・編集してから推奨生成モデルに渡すことで、AIの提案を人間の専門知識で補正する
- 臨床文書・ケアガイドライン・保険ポリシー文書を別々にインデックスし、UR担当者が横断検索できる検索アプリを提供する

## 使いどころ

- 事前承認申請の処理量が多く、審査担当者(看護師・医師)の負荷を下げたい健康保険会社
- AIの提案を最終判断前に必ず人間がレビューする必要がある、規制の厳しい医療領域の意思決定支援
