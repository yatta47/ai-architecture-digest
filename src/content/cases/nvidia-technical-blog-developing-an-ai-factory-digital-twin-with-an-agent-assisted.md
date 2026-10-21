---
type: guidance
title: エージェント支援によるAIファクトリーのデジタルツイン構築
title_original: Developing an AI Factory Digital Twin with an Agent-Assisted Workflow
company: NVIDIA
industry: other
cloud: []
patterns:
- ai-agent
- context-engineering
- human-in-the-loop
components:
- NVIDIA Omniverse DSX Blueprint
- OpenUSD
- USD Content Agents
- SimReady
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/developing-an-ai-factory-digital-twin-with-an-agent-assisted-workflow/
published_at: '2026-10-21'
---

## 概要

Omniverse DSX Blueprintを基に、参照設計・サイト計画・要件文書をエージェントに与え、編集可能なOpenUSDのキャンパスモデルを作るワークフローを紹介する。固定電力枠でのキャパシティ計画に使い、技術者がレビューして反復する。

## 設計のポイント

- 写真だけでなく参照資産と要件文書で設計の根拠をエージェントに与える。
- 変更を加算的なUSDレイヤーに分離し元資産を保護する。
- 寸法チェックと技術者レビューを前提にする。

## 使いどころ

- AIファクトリー設計の初期検討。
- 複数分野(電気・冷却)の要件を揃えて代替案を比較する場面。
