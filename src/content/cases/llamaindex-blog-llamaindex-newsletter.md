---
type: announcement
title: '2025年振り返り: LlamaAgents/LlamaSplit/LlamaSheetsなど文書AI基盤の年間まとめ'
title_original: LlamaIndex Newsletter 2025-12-30 (Year-End Edition)
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- context-engineering
components:
- LlamaParse
- LlamaAgents
- LlamaSplit
- LlamaSheets
- LlamaExtract
- AgentFS
- llamactl
- SemTools
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-12-30
published_at: '2026-07-19'
---

## 概要

LlamaIndexの2025年末特別号ニュースレター。ドキュメントエージェント一括デプロイ製品「LlamaAgents」、文書分割の「LlamaSplit」、スプレッドシート処理の「LlamaSheets」、安全なコーディングエージェント向け仮想ファイルシステム「AgentFS」など2025年の主要リリースを総括し、Pathwork・Cofounder AI・MavenBioなどの顧客事例も紹介している。

## 設計のポイント

- OCR中心の古い文書理解からエージェント型・マルチモーダルな文書理解へ移行し、パーススルー率を60-70%から90%以上に引き上げる
- ワンクリックでデプロイできるテンプレート(請求書処理・契約レビュー・保険金請求)を用意し導入の初速を上げる
- コーディングエージェントに仮想ファイルシステム(AgentFS)を与え、実ファイルを壊さずに安全に自律実行させる
- コンテキストエンジニアリングを重要テーマとして位置づけ、必要な文脈をLLMに的確に渡す設計を各製品に反映する

## 使いどころ

- 請求書・契約書・保険金請求など定型業務文書の処理を自動化したいバックオフィスチーム
- 大量ページのスプレッドシートやドキュメントをAI処理向けに整形したいデータ担当者
- コーディングエージェントを安全に業務環境で使いたい開発チーム
