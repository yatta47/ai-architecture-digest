---
type: guidance
title: エージェント挙動エンジニアリング（行動契約による検証）
title_original: Agentic behavior engineering - Azure Architecture Center
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- eval
- guardrails
- ai-agent
- human-in-the-loop
components:
- Azure Architecture Center
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/agentic-behavior-engineering
published_at: '2026-10-05'
---

## 概要

LLMの非決定性により従来のテストでは捉えにくいエージェントの挙動ドリフトに対し、仕様化・根拠付け・制御・検証・観測を行う方法論を提案する手引き。中心成果物は、実装と切り離して必須/禁止挙動を定義する「行動契約」。

## 設計のポイント

- 期待挙動を実装から分離した行動契約として明示し、変更の影響を継続検証する。
- 結論や行動の前に必要な証拠、不十分時の動作、承認・停止条件を契約に含める。
- 実行証拠を観測し、システム改善に使う。

## 使いどころ

- モデルやプロンプト変更時の挙動ドリフトを管理したいエージェント開発チーム。
- 企業のAI導入で統制と信頼性を設計する場面。
