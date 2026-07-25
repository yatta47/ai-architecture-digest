---
type: announcement
title: LlamaParse v2ローンチとAIチーフオブスタッフ「Cofounder」事例
title_original: LlamaIndex Newsletter 2025-12-23
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- rag
components:
- LlamaParse
- LlamaSplit
- AgentFS
- Gemini 3 Flash
- OpenAI Codex
- Gmail
- Slack
- Linear
- Notion
- GitHub
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-12-23
published_at: '2026-07-19'
---

## 概要

LlamaIndexの週刊ニュースレター。設定を簡素化し最大50%のコスト削減を実現した「LlamaParse v2」の正式ローンチ、安全なコーディングエージェント向けAgentFSのOpenAI Codex対応拡大、そしてGeneral Intelligence CompanyがGmail/Slack/Linear/Notion/GitHubから30分ごとに継続取り込みを行うAIチーフオブスタッフ「Cofounder」をLlamaIndexで構築し、マネージドRAGより低コストで運用している事例を紹介している。

## 設計のポイント

- 複雑な設定モードの代わりにFast/Cost Effective/Agentic/Agentic Plusの4段階ティアに単純化し、自動モデルルーティングで運用負荷を下げる
- 複数の業務ツール(Gmail/Slack/Linear/Notion/GitHub)から30分間隔で継続的にドキュメントを取り込み、常に最新の文脈を保つ
- 仮想ファイルシステム(AgentFS)でコーディングエージェントの実行環境を隔離し、対応プロバイダをOpenAI Codex/Ollama等にも拡張する

## 使いどころ

- 複数の社内ツールからの情報を継続的に集約してAIチーフオブスタッフ的に使いたい経営陣・PMO
- マネージド型RAGサービスよりコストを抑えて独自の文書取り込み基盤を運用したいチーム
- 安全にコーディングエージェントを様々なLLMプロバイダで実行したい開発者
