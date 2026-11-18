---
type: announcement
title: GitHub CopilotでGPT-6.2 AstraとSolが一般提供
title_original: OpenAI's GPT-6.2 Astra and GPT-6.2 Sol now available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-model-routing
components:
- GitHub Copilot
- GPT-6.2 Astra
- GPT-6.2 Sol
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-17-openais-gpt-6-2-astra-and-gpt-6-2-sol-now-available
published_at: '2026-11-17'
---

## 概要

GitHub CopilotでOpenAIのGPT-6.2 AstraとSolが一般提供された。エージェント型コーディングとコードレビュー向けで、早期テストでは前世代より実問題の検出が増えトークン使用が少ないとされる。管理者はモデルポリシーでアクセスを制御できる。

## 設計のポイント

- 用途別（端末作業中心／深いレビュー中心）にモデルを提供する。
- モデルポリシーで組織単位に有効化を管理する。

## 使いどころ

- エージェント型コーディングとレビュー品質を高めたい開発組織。
