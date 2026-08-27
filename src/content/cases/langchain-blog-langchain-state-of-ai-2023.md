---
type: opinion
title: LangSmithの利用データで見る2023年のLLMアプリ開発動向
title_original: LangChain State of AI 2023
company: LangChain
industry: cross-industry
cloud: []
patterns:
- rag
- llmops
- ai-agent
components:
- LangSmith
- OpenAI
- Azure OpenAI
- Anthropic
- Amazon Bedrock
- Hugging Face
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langchain-state-of-ai-2023
published_at: '2026-08-26'
---

## 概要

LangChainは自社の可観測性プラットフォームLangSmithの匿名化利用データ（2023年7月〜12月）を基に、LLMアプリ開発の実態を分析した。複雑なクエリのうち42%が検索（RAG）を伴い17%がエージェントの一部であること、LLMプロバイダーはOpenAIとAzure OpenAIが上位を占めること、コンポーネント合成のためのLangChain Expression Language（LCEL）の利用が急増していることなどを明らかにしている。

## 設計のポイント

- 自社製品の利用ログではなく可観測性プラットフォームの匿名化メタデータを使うことで、LangChain利用者に限らない業界横断の傾向を捉えられるようにした
- 複雑なクエリのうちどれだけが検索・エージェントを伴うかを定量化し、RAGが依然支配的でエージェントはまだ限定的という実態を示した
- LLMプロバイダー・OSSモデル提供元・ベクトルストアそれぞれの利用ランキングを分けて集計し、商用モデルとOSSモデルで異なる利用パターン（API利用 vs ローカル実行）を可視化した

## 使いどころ

- 自社のGenAI技術選定（LLMプロバイダー、ベクトルストア等）の参考に業界動向を知りたいチーム
- LLMアプリでのRAG/エージェント採用率など、意思決定に使える業界横断データを探している経営層・アーキテクト
