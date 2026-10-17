---
type: guidance
title: エージェント時代に向けたクラウドネイティブ基盤の進化の方向性
title_original: Evolving the cloud-native foundation for the next generation of AI
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- cost-optimization
components:
- Azure
outcome:
  type: speed
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/evolving-the-cloud-native-foundation-for-the-next-generation-of-ai/
published_at: '2026-10-15'
---

## 概要

Azureのプロダクトマーケティング責任者が、エージェントが承認待ちや長時間処理、リアルタイム対応など従来アプリと異なる挙動を示すことを踏まえ、クラウドネイティブ基盤がどう進化すべきかを論じた記事。処理に応じて計算・ストレージ・ネットワークを協調させるインフラ最適化、アプリ基盤、オープン技術の3観点で整理し、Basecamp ResearchのEDEN事例を挙げる。

## 設計のポイント

- AI処理は工程ごとに必要な資源（アクセラレータ、CPU、データアクセス）が異なるため、容量を増やすより処理に資源を合わせる。
- 計算・ストレージ・ネットワークを連携して設計し、性能・信頼性・コストを処理全体で均衡させる。

## 使いどころ

- エージェント導入に向けて既存クラウドネイティブ基盤の見直し方針を整理したい基盤担当者。
- AIワークロードのコストと性能の釣り合いを検討する意思決定者。
