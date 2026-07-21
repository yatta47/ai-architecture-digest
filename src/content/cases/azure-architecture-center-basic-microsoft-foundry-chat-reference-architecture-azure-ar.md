---
type: guidance
title: Microsoft Foundryでプロンプトエージェント型チャットを学習用に構築する基本リファレンスアーキテクチャ
title_original: Basic Microsoft Foundry chat reference architecture
industry: cross-industry
cloud:
- azure
patterns:
- rag
- ai-agent
components:
- Microsoft Foundry
- Foundry Agent Service
- Azure AI Search
- Azure App Service
- Azure OpenAI
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/basic-microsoft-foundry-chat
published_at: '2026-06-19'
---

## 概要

Microsoft FoundryとFoundry Agent Serviceを使い、Azure App Service上のチャットUIからAI Searchでグラウンディングデータを取得し、Azure OpenAIモデルへプロンプトを渡すRAG型チャットアプリの基本構成を示す。本番運用は想定せず、学習・PoC用途としてシンプルさとコスト効率を優先した構成で、本番化にはBaseline Foundry chatアーキテクチャへの移行を推奨している。

## 設計のポイント

- 宣言的に定義したプロンプトエージェントをFoundry Agent Serviceにホストさせ、チャット履歴管理やツール呼び出しのオーケストレーション、コンテンツセーフティをサービス側に委譲する。
- AI Searchをグラウンディング用の知識ストアとして位置づけ、RAGパターンでクエリ抽出・検索・生成の3段階を明確に分離する。
- 可用性ゾーンやオートスケールを意図的に省略し、学習・PoC用途におけるセットアップ時間の短縮とコスト最小化を優先する設計判断を明示する。

## 使いどころ

- Foundryエージェントを使ったチャットアプリケーションの作り方を短時間で学びたい開発者・アーキテクト。
- 本番投入前に、RAG構成のプロンプトエージェントで概念実証（PoC）を素早く回したいチーム。
- 将来的にBaseline構成へ移行する前提で、まず最小構成のリファレンス実装から着手したいプロジェクト。
