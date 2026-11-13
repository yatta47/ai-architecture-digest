---
type: announcement
title: LangChainのシリーズC調達とエージェント基盤LangSmithの全体像
title_original: LangChain Raises $300M to Enable Every Company to Own Its Intelligence
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- eval
components:
- LangSmith
- LangGraph
- LangChain
- Deep Agents
- LangSmith Agent Server
- LangSmith Engine
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/series-c
published_at: '2026-11-13'
---

## 概要

LangChainが3億ドルのシリーズC調達を発表し、LangSmithをAgent Runtime・Agent Improvement・Agent Governanceの3本柱で構成するエージェント基盤として位置づけた。Workdayはエージェントの展開期間を5カ月から1日未満に短縮したとしている。

## 設計のポイント

- 実行・改善・ガバナンスを分けた3層でエージェント運用を整理している。
- フレームワーク非依存で、モデル選択とデータ・インフラの管理権を企業側に残す方針を取る。
- 観測と評価の結果から改善を自動化するエージェント(LangSmith Engine)を基盤内に持つ。

## 使いどころ

- 複数のエージェントを本番運用し、監視・評価・統制を一元化したい企業。
- エージェント展開のリードタイムを短縮したいプラットフォームチーム。
