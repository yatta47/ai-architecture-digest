---
type: case
title: LangSmithのデータ管理を軸にした知識抽出タスクのLLMファインチューニング事例
title_original: Using LangSmith to Support Fine-tuning
company: LangChain
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- llmops
components:
- LangSmith
- HuggingFace
- OpenAI
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/using-langsmith-to-support-fine-tuning-of-open-source-llms
published_at: '2026-08-26'
---

## 概要

LangChainは知識グラフのトリプル抽出タスクを題材に、LangSmithでログから低品質な出力を抽出・修正して学習用データセットを構築し、LLaMA2-7b-chatとgpt-3.5-turboの両方をファインチューニングして評価した。4bit量子化とLoRA/qLoRAで単一GPUでも学習できるようにし、ファインチューニングとRAG/プロンプトの使い分けの考え方も整理した。

## 設計のポイント

- LangSmidthにログされた実行から低品質な出力を抽出・修正してデータセット化し、ファインチューニング用データの収集とクレンジングを効率化した
- 新しい知識を教える用途にはRAG/プロンプトを、特定タスクの型を教える用途にはファインチューニングを使うという使い分けの指針を採用した
- 7Bパラメータモデルを単一GPUに載せるため4bit量子化を行い、LoRA/qLoRAで学習対象パラメータを全体の約1%に抑えた
- オープンソースLLMとOpenAIのファインチューニングAPIの両方で同一タスクを試し、LangSmithで評価結果を横並び比較した

## 使いどころ

- タスク特化のLLMをコストを抑えて構築したいチーム（抽出・分類・text-to-SQLなど型が決まったタスク）
- 限られたGPUリソースでオープンソースLLMをファインチューニングしたい開発者
- ファインチューニング用データセットの収集・評価基盤を探しているチーム
