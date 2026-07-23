---
type: guidance
title: サードパーティ成果物を検証してから使うクアランティン(検疫)パターン
title_original: Quarantine pattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/quarantine
published_at: '2025-12-23'
---

## 概要

サードパーティ製のコンテナイメージやOSSライブラリ、ベンダー提供のOSイメージなど外部から取得する成果物を『信頼できない』ものとして扱い、脆弱性スキャンなどの検証を経て初めて『信頼済み』として利用可能にするクアランティン(検疫)パターンを解説する。検証プロセスは開発プロセスとは独立して運用され、消費者側が明示的に呼び出すことで、汚染された成果物がサプライチェーンに混入するリスクを防ぐ。
