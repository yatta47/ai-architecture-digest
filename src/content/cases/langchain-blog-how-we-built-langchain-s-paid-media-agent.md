---
type: case
title: マーケティング担当者として働くPaid Media運用エージェント
title_original: How we built LangChain's Paid Media Agent
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- human-in-the-loop
- decision-execution
components:
- LangChain Deep Agents
- LangSmith Sandbox
- pandas
- DuckDB
outcome:
  type: revenue
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/paid-media-agent
published_at: '2026-09-14'
---

## 概要

LangChainは有料広告運用を担うエージェントを構築し、コーディングエージェントを『知識労働者』として扱う設計思想でサンドボックス環境・業務データ・運用手順を与えた。計算やルールはコードに、判断はモデルに委ねることで、有料広告経由のパイプライン比率を0%から20%に伸ばしつつ、レポーティングワークフローを40倍安く13倍速く実行できるようにした。

## 設計のポイント

- 計算やソース・オブ・トゥルースのルールはコードで確実に実行し、モデルは結果の解釈と次の提案に専念させる
- 業務知識をシステムプロンプトに詰め込まず、Markdownのスキルとwikiとして分離し必要時に参照させる
- サンドボックスにソフトウェアと業務wikiを焼き込んだスナップショットから起動し、起動時間を短縮する
- キャンペーン変更の提案は人間の承認を経てから実行し、実行後に結果を検証するワークフローにする

## 使いどころ

- 少人数のマーケティングチームが複数の広告チャネルを横断して運用改善したい場合
- 定型分析やレポーティングにかかるモデル呼び出しコストを削減したい場合
- エージェントに実際の操作権限を与えつつ人間の承認フローを組み込みたい業務自動化
