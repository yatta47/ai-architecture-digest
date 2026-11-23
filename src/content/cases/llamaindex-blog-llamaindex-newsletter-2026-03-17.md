---
type: announcement
title: 'LlamaIndexニュースレター(2026-03-17): エージェント型OCRとSkills対MCP'
title_original: LlamaIndex Newsletter 2026-03-17
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- rag
components:
- LlamaParse
- semtools
- SurrealDB
- Gemini Embedding 2
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2026-03-17
published_at: '2026-03-17'
---

## 概要

LlamaIndexの週次ニュースレター。Gemini Embedding 2を使った音声ナレッジベースのデモ、semtools v3.0.0、plan-act-verifyループによるエージェント型文書抽出、SkillsとMCPツールの使い分けガイドなどを紹介している。

## 設計のポイント

- ドメイン変化の速さに応じてSkills(自然言語指示)とMCP(決定的API)を使い分ける。
- plan-act-verifyとバウンディングボックスで抽出結果を検証可能にする。

## 使いどころ

- テンプレート保守なしで多様な文書を抽出したい場合。
- エージェントの拡張手段を選ぶ設計判断。
