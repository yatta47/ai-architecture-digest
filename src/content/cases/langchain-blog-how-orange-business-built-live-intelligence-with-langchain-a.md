---
type: case
title: Orange BusinessのAIエージェント基盤Live Intelligence
title_original: How Orange Business built Live Intelligence on LangChain and LangSmith
company: Orange Business
industry: telecom
cloud:
- multi-cloud
patterns:
- ai-agent
- llmops
- llm-gateway
components:
- LangChain
- LangSmith
- LangSmith Fleet
- MCP
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-orange-business-built-live-intelligence-on-langchain-and-langsmith
published_at: '2026-10-13'
---

## 概要

Orange BusinessはStudio・Portal・Consoleの3構成の企業向けAI基盤Live Intelligenceを、約20ベンダーの評価の末LangChainとLangSmithで構築した。12万人の従業員と150社超の顧客が利用する。

## 設計のポイント

- モデル中立性とポータビリティを重視し、欧州のデータ主権要件に応じて配置できるようにしている。
- 開発者向けStudio、業務ユーザー向けPortal、管理者向けConsoleに役割分離している。
- 観測性・評価は自作せずLangSmithに任せ、12〜18か月の開発を回避した。

## 使いどころ

- データ主権要件のある企業のエージェント基盤選定。
- ガバナンス付きでノーコード/ローコードのエージェントを展開したい場面。
