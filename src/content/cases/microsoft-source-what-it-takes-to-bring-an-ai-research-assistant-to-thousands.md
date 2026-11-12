---
type: case
title: Novoの臨床試験データエージェントをFoundryのホステッドエージェントへ再構築
title_original: From custom infrastructure to hosted agents
company: Novo Nordisk
industry: healthcare
cloud:
- azure
patterns:
- ai-agent
- eval
components:
- Microsoft Foundry
- Hosted agents
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://commandline.microsoft.com/from-custom-infrastructure-to-hosted-agents/
published_at: '2026-11-11'
---

## 概要

Novo Nordiskの臨床試験データ二次分析エージェントを、Microsoft Foundryのホステッドエージェントとして再実装した。運用モデルが簡素になり、セッション分離が強化され、トレースから評価・最適化へ直結できる。

## 設計のポイント

- 独自基盤からホステッド実行に移し、運用負荷を下げる。
- セッション単位の分離を強める。
- トレース・評価・最適化・ガバナンスを同一基盤で連携させる。

## 使いどころ

- 臨床・研究データを扱う規制業種のエージェント。
- 自前のエージェント基盤を運用している企業。
- トレースから改善サイクルを回したいチーム。
