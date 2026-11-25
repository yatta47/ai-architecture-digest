---
type: case
title: GymNationの会員ライフサイクルを担うマルチエージェント基盤
title_original: AI Agents Transform GymNation Member Experience
company: GymNation
industry: other
cloud: []
patterns:
- multi-agent-orchestration
- rag
- voice-agent
- ai-agent
components:
- LlamaIndex
- WhatsApp
outcome:
  type: revenue
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/case-study-gymnation-revolutionizes-fitness-with-ai-agents-powering-member-experiences
published_at: '2024-08-29'
---

## 概要

中東のジム事業者GymNationが、LlamaIndex上にRAG層とマスターエージェントが専門エージェントを統括する構成を作り、営業・予約・オンボーディングを自動化した。デジタルリードの成約率が20%向上し、4人のチームで複数エージェントを本番運用している。

## 設計のポイント

- 共通のRAG層を一つ用意し、複数エージェントで知識を共有する。
- マスターエージェントが機能別の専門エージェントを調整する。
- 関数呼び出しでCRMなど既存システムに接続し、チャットで得たリードから音声エージェントの架電へつなぐ。

## 使いどころ

- 会員制ビジネスで見込み客対応と予約を24時間自動化したい場合。
- 少人数チームが複数チャネルのエージェントを展開する場合。
