---
type: guidance
title: Azureで生成AIワークロードを設計するためのAI技術概観(ML・深層学習・RAG・コンテキストエンジニアリング)
title_original: AI technology overview
industry: cross-industry
cloud:
- azure
patterns:
- rag
- context-engineering
components:
- Microsoft Foundry
- Microsoft 365 Copilot
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/ai-overview
published_at: '2026-07-02'
---

## 概要

Azureでアーキテクトが生成AI/機械学習ワークロードを設計する際に押さえるべき基礎概念(アルゴリズム、機械学習、深層学習、生成AI、言語モデル、Copilot、RAG、コンテキストエンジニアリング)を整理した概観記事。Well-Architected FrameworkのAIワークロードガイダンスへの入口として位置づけられる。

## 設計のポイント

- 低コード/no-code AI、HPC、非生成AI(従来型分析やルールベース自動化)はWell-Architected FrameworkのAIガイダンスの対象外と明示し、適用範囲を切り分ける
- 過去の実績データから未来を確度高く予測できるケースには機械学習、より複雑なパターン抽出が必要な場合は深層学習、というように課題の性質でアプローチを選び分ける
- Microsoft FoundryをOpenAI/Anthropic/Microsoft/xAI等のモデルカタログとエージェントホスティングを提供するPaaSと位置づけ、モデル選定の起点として使う

## 使いどころ

- Azure上でAI/MLワークロードの技術選定を始めるアーキテクトの入門資料
- 生成AI・言語モデル・RAG・コンテキストエンジニアリングなど用語を整理して社内共有したいチーム
