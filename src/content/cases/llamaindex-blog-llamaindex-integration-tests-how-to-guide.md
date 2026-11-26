---
type: guidance
title: Tonic ValidateとGitHub ActionsでRAGの回帰テストを行う
title_original: Implementing Integration Tests for LlamaIndex with Tonic Validate
company: Tonic.ai
industry: cross-industry
cloud: []
patterns:
- rag
- eval
- ci-cd
- llmops
components:
- Tonic Validate
- LlamaIndex
- GitHub Actions
- create-llama
- FastAPI
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/tonic-validate-x-llamaindex-implementing-integration-tests-for-llamaindex-43db50b76ed9
published_at: '2024-01-26'
---

## 概要

RAGの性能低下を変更時に検知するため、想定質問と回答の組をTonic Validateで評価し、GitHub Actionsの結合テストにする手順を解説する。

## 設計のポイント

- APIは回答に加えて検索した文脈も返し、検索と生成を別々に評価できるようにする。
- 想定QAセットを用意し、指標の低下を結合テストで検知する。

## 使いどころ

- 本番RAGを継続的に改修するチーム。
