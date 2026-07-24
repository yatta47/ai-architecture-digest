---
type: announcement
title: Web横断・Google Workspace連携のエージェント型Research機能
title_original: Claude takes research to new places
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
components:
- Google Workspace
- Gmail
- Google Calendar
- Google Docs
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/research
published_at: '2025-04-15'
---

## 概要

Anthropicは、Web検索とGoogle Workspace(Gmail/Calendar/Docs)を横断してエージェント的に複数回の検索・推論を繰り返し、引用付きの包括的な回答を数分で生成する「Research」機能と、Google Workspace連携を発表した。Enterprise向けにはGoogle Docsを対象にRAG(検索拡張生成)によるカタログ機能も提供し、大量の社内文書から必要な情報を高精度に検索できるようにする。

## 設計のポイント

- Researchはあらかじめ計画を固定せず、直前の検索結果を踏まえて次に何を調べるかを動的に決めるエージェント型の反復検索フローを採用している。
- 取得した情報には必ず引用元へのインラインリンクを付与し、回答の検証可能性と信頼性を担保している。
- Enterprise向けのカタログ機能はセキュアなRAG技術で組織のドキュメントに特化したインデックスを構築し、正確なファイル名を知らなくても検索可能にしている。

## 使いどころ

- マーケティングチームが競合調査と社内の製品資料を組み合わせて製品発表計画を素早く作成したい場合。
- 営業チームが商談前にメール履歴やカレンダー、企業の最新情報から準備資料を自動生成したい場合。
- エンジニアが設計文書や外部API仕様、実装パターンを横断して技術検討を行いたい場合。
