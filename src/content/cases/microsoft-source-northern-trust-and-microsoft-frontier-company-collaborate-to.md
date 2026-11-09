---
type: case
title: Northern Trust：顧客オンボーディングの取引履歴変換を自動化するAIエージェント
title_original: Northern Trust and Microsoft Frontier Company collaborate to transform client onboarding through AI
company: Northern Trust
industry: financial-services
cloud:
- azure
patterns:
- ai-agent
- human-in-the-loop
- eval
- guardrails
components:
- Microsoft Foundry
- Microsoft Excel
- SharePoint
- Azure
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/source/2026/11/09/northern-trust-and-microsoft-frontier-company-collaborate-to-transform-client-onboarding-through-ai/
published_at: '2026-11-09'
---

## 概要

Northern TrustはMicrosoftのFDEチームと共同で、顧客の過去取引データを標準フォーマットへ変換するオンボーディングエージェントを構築した。データ準備時間を2.5週間から3日へ83%短縮し、初回通過のF1スコアは96.5%に達した。

## 設計のポイント

- アナリストがExcelやSharePoint上で出力を確認・承認できる、人手レビュー前提のワークフローにする
- 匿名化データのみを用い、F1スコア等の評価指標でヒルクライムする『eyes-off』方式で顧客データを保護する
- 承認済みのオンボーディング知識を蓄積するガバナンス層を置き、継続改善につなげる

## 使いどころ

- 大量の異種データを標準形式へ変換する金融機関のオンボーディング業務
- 機微データを開発側が直接見られない規制業種でのエージェント開発
- AI出力のレビューと例外処理を業務フローに組み込みたい場面
