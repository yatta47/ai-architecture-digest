---
type: case
title: 建設業の公共入札書類を自動分析するSoftIQのRFPエージェント「Przetargi.io」
title_original: 'Case Study: Tender/RFP Agent for Construction Sector with SoftIQ'
company: SOFTIQ
industry: other
cloud: []
patterns:
- document-processing
- rag
- multi-agent-orchestration
components:
- LlamaIndex
- LlamaParse
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/case-study-tender-rfp-agent-for-construction-sector-with-softiq
published_at: '2026-07-19'
---

## 概要

ポーランドのIT企業SOFTIQは、公共工事の入札書類（数百ページに及ぶ非構造化文書、図面等のマルチモーダル情報を含む）をLlamaIndex Workflowsで解析し、20〜30ページのエグゼクティブサマリー・リスク評価付きレポートを自動生成するエージェント型SaaS「Przetargi.io」を構築。入札分析時間を数時間から10分未満に短縮した。

## 設計のポイント

- 文書レイアウトの階層情報を保持したままセマンティックチャンキングし、レポート生成時に業界標準の構成を再現する
- 各セクションの生成をLlamaIndex Workflowsにカプセル化し、特定のビジネスプロセス（要約・リスク評価・推奨）ごとにChain of Thoughtで処理する
- 図面などの画像情報を含むマルチモーダル文書もマルチモーダル解析で扱えるようにしている

## 使いどころ

- キーワードマッチングによる入札案件の見落とし・誤検出を減らしたい建設業界の営業・入札担当
- 数百ページの非標準フォーマット文書を短時間でレポート化する必要がある公共調達関連業務
