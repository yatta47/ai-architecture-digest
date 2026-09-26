---
type: announcement
title: Microsoft Foundryのモデル拡充・音声エージェント・継続的最適化
title_original: Ship agents faster with expanded model choice, voice agents, and continuous optimization
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- voice-agent
- multi-model-routing
- eval
- prompt-optimization
components:
- Microsoft Foundry
- Foundry Agent Service
- Microsoft Agent Framework
- GPT-6
- Claude Opus 5.5
- Fashable
outcome:
  type: speed
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/ship-agents-faster-with-expanded-model-choice-voice-agents-and-continuous-optimization/
published_at: '2026-09-24'
---

## 概要

MicrosoftはFoundryにGPT-6ファミリーとClaude Opus 5.5を追加し、音声エージェントと長時間実行の耐障害性をパブリックプレビューで提供した。本番トレースで評価と最適化を回す継続改善も打ち出した。Fashableは製品開発期間を数か月から数週間に短縮したという。

## 設計のポイント

- モデル・ハーネス非依存の基盤で、ワークロードごとにモデルを評価して選び直せるようにする。
- 音声を同じエージェント基盤のネイティブ機能とし、ツールやガバナンスを共有する。
- チェックポイントと永続レスポンスで、切断や障害後も長時間タスクを再開する。
- 本番トレースから評価して指示・ツール・モデルを改善するループを回す。

## 使いどころ

- モデルの入れ替えが頻繁で基盤を作り直したくない企業。
- 電話やTeams向けの音声エージェントを構築するチーム。
