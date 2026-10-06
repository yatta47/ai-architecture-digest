---
type: case
title: Agentforce Memory：エージェントの永続メモリ基盤
title_original: 'AI Agents Need Memory: Building Persistent Memory for Agentforce'
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- memory-consolidation
- context-engineering
- rag
components:
- Agentforce
- Agentforce Memory
outcome:
  type: productivity
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/ai-agents-need-memory-building-persistent-memory-for-agentforce/
published_at: '2026-10-05'
---

## 概要

ステートレスなエンタープライズAIエージェントが毎回文脈の説明を求める問題に対し、Salesforceが開発した永続メモリ機能Agentforce Memoryの設計の裏側を、アーキテクトへのQ&Aで語る。共通用語の確立、PoCからパイロットへの進化、意味検索・文脈管理・遅延・開発者体験・信頼のバランスを扱う。

## 設計のポイント

- メモリの共通言語を最初に決めてチーム間の認識を揃える。
- 意味検索と文脈管理で、必要な記憶だけをプロンプトに戻す。
- 遅延とユーザーの信頼を設計制約として扱う。

## 使いどころ

- 顧客対応エージェントに過去の会話と嗜好を引き継がせたい場面。
- エージェント基盤にメモリ機能を組み込む設計の参考。
