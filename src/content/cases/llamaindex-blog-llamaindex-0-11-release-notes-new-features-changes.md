---
type: announcement
title: 'LlamaIndex 0.11: Workflows導入とコア軽量化'
title_original: LlamaIndex 0.11 Release Notes
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- event-driven
- ai-agent
- llmops
components:
- LlamaIndex
- Workflows
- Property Graph Index
- Pydantic
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-llamaindex-0-11
published_at: '2024-08-22'
---

## 概要

Python版LlamaIndex 0.11が公開され、イベント駆動のWorkflowsが非推奨となったQuery Pipelinesを置き換える。計測機能の強化、コアパッケージの42%縮小、Pydantic V2への移行などの変更と破壊的変更がある。

## 設計のポイント

- DAG型のパイプラインからイベント駆動の構成へ移す。
- 主要ライブラリを必須依存から外し、コアを小さく保つ。

## 使いどころ

- 0.10系から移行する開発者が破壊的変更を確認する場面。
- LLMアプリの監視・デバッグ性を高めたいチーム。
