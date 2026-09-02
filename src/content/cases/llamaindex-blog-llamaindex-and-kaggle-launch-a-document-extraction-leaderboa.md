---
type: announcement
title: LlamaIndexとKaggle、AIエージェント向け文書抽出ベンチマーク「ExtractBench」を公開
title_original: LlamaIndex and Kaggle launch a document extraction leaderboard for AI agents
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
- ai-agent
components:
- ExtractBench
- Kaggle
- ParseBench
- LlamaIndex Extract
- GPT-5.5
- Claude Opus 4.8
- Gemini 3 Flash
- Gemini 3.5 Flash
- Codex
- Claude Code
- Reducto
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-and-kaggle-launch-a-document-extraction-leaderboard-for-ai-agents
published_at: '2026-09-02'
---

## 概要

LlamaIndexはKaggleと共同で、370件・4,869ページの企業文書と8業務ドメインを対象に14の抽出システムを精度・知覚品質・表構造・文書長・コストの5軸で評価するオープンベンチマーク「ExtractBench」を公開した。フロンティアVLM、コーディングエージェント、専用抽出APIを同一スキーマで比較し、LLM-as-judgeを使わない決定論的なルールベース評価で、長文書ほど精度が落ちるモデルとエージェント型パイプラインの差を可視化している。

## 設計のポイント

- 文書全体を1回のモデル呼び出しで処理するのではなく、セクション分割・モデル振り分け・原文照合・低信頼フィールドの再試行を行うエージェント型パイプラインが長文書での精度劣化を防ぐことを示している。
- LLM-as-judgeを使わず決定論的なルールベース評価を採用することで、14システム・67文書種別にわたる再現可能な比較を実現している。
- 抽出値ごとに単語単位のバウンディングボックスを付与し、レビュアーが値の抽出元をドキュメント上で即座に特定できるトレーサビリティを重視している。

## 使いどころ

- 保険金請求や契約書などの長大なスキャン文書から構造化データを抽出し、人手レビューなしでエージェントに判断させたい企業。
- 複数の抽出システム（VLM・コーディングエージェント・専用API）を精度とページ単価コストの両面で比較検討したいチーム。
