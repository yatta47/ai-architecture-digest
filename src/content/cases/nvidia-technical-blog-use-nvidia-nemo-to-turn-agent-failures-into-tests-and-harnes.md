---
type: case
title: エージェントの失敗をテストとハーネス修正に変えるNeMo
title_original: Use NVIDIA NeMo to Turn Agent Failures into Tests and Harness Fixes
company: NVIDIA
industry: manufacturing
cloud: []
patterns:
- eval
- ai-agent
- prompt-optimization
components:
- NVIDIA NeMo Compass
- NeMo Eval Author
- NemoClaw
- OpenShell
- Hermes Agent
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/use-nvidia-nemo-to-turn-agent-failures-into-tests-and-harness-fixes/
published_at: '2026-11-03'
---

## 概要

トレースから繰り返し起きる失敗を抽出するNeMo Compassと、評価を作るNeMo Eval Authorで、ハーネス（SOUL.mdなど）を更新し、開発・保留タスクで再評価する1サイクルを示す。Dassault Systèmesの例では不正なツール呼び出しが142件から0件に、評価スコアは相対28%向上、ツール呼び出しは35%減った。

## 設計のポイント

- トレースIDに結びつけた失敗の優先度付けを行う。
- 失敗から評価を作り、保留タスクでも回帰を確認する。
- 最適化の対象をプロンプト・ツール・ルーティングなどハーネス全体にする。

## 使いどころ

- ドメイン特化エージェントの品質改善を継続運用するとき。
- ツール呼び出しの誤りを減らしたいとき。
