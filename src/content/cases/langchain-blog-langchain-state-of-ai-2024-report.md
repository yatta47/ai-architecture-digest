---
type: opinion
title: LangSmith利用統計で見る2024年のAIエージェント化とLLM運用トレンド
title_original: LangChain State of AI 2024 Report
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- eval
- rag
components:
- LangSmith
- LangGraph
- LangChain
- OpenAI
- Ollama
- Groq
- Chroma
- FAISS
- Milvus
- MongoDB
- Elastic
- Mistral
- Hugging Face
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langchain-state-of-ai-2024
published_at: '2026-08-26'
---

## 概要

LangChainがLangSmithの利用データをもとに2024年のLLMアプリ開発動向をまとめたレポート。ツール呼び出しを含むトレースの割合が0.5%から21.9%に急増し、LangGraph採用組織も43%に達するなど、単純な質問応答から複雑なマルチステップのエージェント型ワークフローへの移行が進んでいることを示す。あわせてLLM-as-Judgeや人手フィードバックによる評価・改善サイクルの定着も報告している。

## 設計のポイント

- トレースをLLM呼び出し・リトリーバー呼び出し・ツール呼び出しなどのステップ単位で計測し、ワークフローの複雑化を定量的に把握する。
- ツール呼び出しを介してモデルが外部関数やリソースを自律的に呼び出せるようにし、エージェント的な振る舞いを実現する。
- Relevance・Correctness・Exact Match・HelpfulnessなどをLLM-as-Judgeで粗く自動評価し、品質の作り込みに使う。
- トレース/ラン単位で人手フィードバックを収集し、改善用のデータセットを継続的に蓄積する。

## 使いどころ

- マルチステップのエージェント型ワークフローを構築し、ステップ数とLLM呼び出し回数のバランスを最適化したいチーム。
- 自動LLM評価と人手フィードバックを組み合わせて出力品質を継続的に検証したいチーム。
- OSSモデル（Ollama, Groqなど）と商用プロバイダの使い分けを検討している組織。
- LangChain以外のフレームワークで構築しつつ、統一的な可観測性/トレーシングを必要とするチーム。
