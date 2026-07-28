---
type: case
title: Unity AI Gatewayで実現するコーディングエージェントの予算統制
title_original: How Databricks manages its own coding agent spend with Unity AI Gateway Budgets
company: Databricks
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- cost-optimization
- llmops
components:
- Unity AI Gateway
- Claude Code
- Codex
- Cursor
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-databricks-manages-its-own-coding-agent-spend-unity-ai-gateway-budgets
published_at: '2026-07-28'
---

## 概要

Databricksは全社のコーディングエージェント（Claude Code、Codex、Cursor等）のトラフィックをUnity AI Gatewayに集約し、日次と月次で異なる目的の予算枠を分離することで暴走消費を防ぎつつエンジニアの生産性を落とさない統制を実現した。日次上限超過はSlack通知とセルフサービスでの引き上げで摩擦なく解消し、月次上限超過のみマネージャー承認を要する設計とした。

## 設計のポイント

- 暴走消費の防止（日次・小さい上限）と月次の異常消費統制（大きい上限）を別々の予算として分離し、単一の上限で両方を賄おうとしない
- 全エージェントのトラフィックを単一のゲートウェイに集約することで、ツールやモデルを問わず一箇所でポリシーを強制できるようにする
- 日次上限超過時はセルフサービスの引き上げ（承認不要）にし、月次上限超過のみ承認フローに回すことで大半のブロックを摩擦なく解消する

## 使いどころ

- 多数のエンジニアが複数のAIコーディングツールを併用しており、AI利用コストが急増している開発組織
- 予算超過時の承認待ちが開発体験を阻害している組織が、暴走防止と正当な大口利用を区別したい場合
