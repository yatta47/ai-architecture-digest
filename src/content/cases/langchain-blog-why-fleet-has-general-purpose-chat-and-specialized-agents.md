---
type: guidance
title: アドホックなチャットと反復業務用Specialized Agentsを使い分けるFleetの設計
title_original: Why Fleet Has Both General Purpose Chat and Specialized Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- memory-consolidation
components:
- Fleet
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/why-fleet-has-both-general-purpose-chat-and-specialized-agents
published_at: '2026-06-16'
---

## 概要

LangChainのFleetは、アドホックな一回限りの作業向けの汎用チャットと、反復業務向けに指示・ツール・メモリ・トリガーを固定したSpecialized Agentsを使い分ける設計を採る。有用なアドホックタスクは後からSpecialized Agentへ昇格でき、メモリの永続性がジョブ単位で管理される点が両者の最大の違い。

## 設計のポイント

- アドホックな作業は汎用チャット、反復的な作業は指示・ツール・メモリを固定したSpecialized Agentに分離する
- Specialized Agentはサブエージェントに文脈集約作業をオフロードし、メインエージェントのコンテキストを汚さない
- エージェントのメモリをジョブ単位で永続化し、毎回同じ前提を再説明させない

## 使いどころ

- 毎週の定型レポートや受信トレイ管理など反復業務を自動化したいチーム
- 一度きりの調査やアドホックな横断作業をすぐ試したい場合
