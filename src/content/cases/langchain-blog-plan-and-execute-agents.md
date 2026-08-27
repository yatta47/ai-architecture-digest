---
type: case
title: 計画立案と実行を分離したPlan-and-Executeエージェントアーキテクチャ
title_original: Plan-and-Execute Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
components: []
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/plan-and-execute-agents
published_at: '2026-08-26'
---

## 概要

LangChainは、ReActベースの逐次的な「Action Agent」がタスクの複雑化に伴いプロンプトが肥大化し信頼性が下がる課題に対応するため、まず全体の計画を立ててから各ステップを個別に実行する「Plan-and-Execute」型のエージェント実行器を導入した。計画担当（プランナー）と実行担当（エグゼキューター）にLLMの役割を分離することで、それぞれの信頼性を高めつつ、将来的に軽量なモデルへの置き換えも可能にする設計になっている。

## 設計のポイント

- タスク全体の計画立案（プランナー）とステップごとの実行（エグゼキューター）を別のLLM呼び出しに分離し、それぞれの役割に集中させることで信頼性を高めた
- プランナーの出力をパーサーでステップのリストに変換し、エグゼキューター（Action Agent）がステップごとに必要なツールを選んで実行する2層構造にした
- 役割分離により将来的に小型・高速・安価なモデルへ置き換えやすくなるという拡張性を見込んだ設計にした
- LLM呼び出し回数が増えるという明確なコストトレードオフを認識した上で、複雑で長期的なタスクの信頼性向上を優先する判断をした

## 使いどころ

- 単純なReAct型エージェントではプロンプトが肥大化・不安定化するような複雑で長期的なタスクを扱いたいチーム
- プランニングと実行を役割分離してモデルコストを最適化したいエージェント設計
