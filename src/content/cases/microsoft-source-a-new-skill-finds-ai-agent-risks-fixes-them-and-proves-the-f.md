---
type: announcement
title: エージェントのリスク発見から修正実証までを一括で回す評価・ガバナンススキル
title_original: 'Introducing run-assert-eval: Find the risk, fix it, prove it'
company: Microsoft
industry: cross-industry
cloud: []
patterns:
- eval
- guardrails
- policy-as-code
- ai-agent
components:
- run-assert-eval
- Clarity
- ASSERT
- Agent Control Specification
- VS Code
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://commandline.microsoft.com/run-assert-eval-responsible-ai-agent-risk-discovery-at-runtime/
published_at: '2026-09-25'
---

## 概要

Microsoftは、エージェントの脅威モデリング（Clarity）、評価（ASSERT）、実行時ポリシー生成（ACS）、再評価を1プロンプトで連結するスキルrun-assert-evalを公開した。課金サポートエージェントの例では、他顧客データ漏えいが基準実行で30.0%（12/40）だったのが、ポリシー適用後は5.9%（2/34）に低下した。

## 設計のポイント

- 振る舞い定義・テストケース・判定器を固定し、変更点をポリシーのみにして前後比較の妥当性を保つ。
- 要件に書かれていないリスクを、評価の前に脅威モデリングで洗い出して起点にする。
- 評価結果から実行時ポリシー（Rego）を生成・検証し、同じ評価を再実行して効果を実証する。

## 使いどころ

- エージェントを本番投入する前に安全性と有用性を前後比較で示したいチーム。
- 手作業でつないでいた評価→ポリシー→再評価のループを自動化したい責任あるAI担当。
