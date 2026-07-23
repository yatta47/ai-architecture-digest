---
type: announcement
title: OpenAI ChatKitで作るエージェントチャットUIのスターターテンプレート
title_original: OpenAI ChatKit Starter Templates
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- ai-agent
- unified-runtime
components:
- ChatKit
- Agent Builder
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-chatkit-starter-app
published_at: '2025-10-06'
---

## 概要

OpenAIがChatKitを使った最小構成のリファレンス実装として2種類のスターターアプリを公開した。ひとつは自前でホストするChatKit統合、もうひとつはAgent Builderのホスト型ワークフローと連携するManaged ChatKit統合で、どちらもチャットベースのエージェントUIを素早く立ち上げるためのテンプレートとなっている。

## 設計のポイント

- 自己ホスト型とマネージド型の2パターンを分離したテンプレートとして提供し、統合方式の違いを比較検討しやすくしている
- ChatKitをフロントエンドのチャットUI層として切り出し、バックエンドのエージェントロジック（Agent Builderのワークフロー）と疎結合にしている
- Python・TypeScript・JavaScriptなど複数言語のサンプルを含めることで、既存スタックへの組み込みやすさを重視している

## 使いどころ

- 自社プロダクトにAIチャットエージェントのUIを素早く組み込みたい開発チーム
- Agent Builderで構築したホスト型ワークフローをそのままチャット画面として公開したい場合
- ChatKitの自己ホスト運用とマネージド運用のどちらが自社要件に合うか検証したいチーム
