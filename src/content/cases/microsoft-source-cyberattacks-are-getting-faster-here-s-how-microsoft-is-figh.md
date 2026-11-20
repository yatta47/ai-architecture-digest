---
type: announcement
title: 'Microsoft Perception: 赤・青・緑エージェントで回すエージェント型セキュリティ基盤'
title_original: Cyberattacks are getting faster. Here's how Microsoft is fighting AI with AI
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- multi-agent-orchestration
- ai-agent
- human-in-the-loop
- multi-model-routing
- context-engineering
components:
- Microsoft Perception
- Microsoft Defender
- Microsoft Sentinel
- Microsoft Entra
- Microsoft Purview
- Microsoft Intune
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/security/blog/2026/11/17/security-for-the-agentic-era-powered-by-microsoft-perception/
published_at: '2026-11-18'
---

## 概要

AIによる攻撃の高速化に対し、Microsoftはシグナル/センサー・コンテキスト・エージェントとハーネスの3層からなるサイバースタックを示した。Microsoft Perceptionが赤・青・緑チームのエージェントをプレイブックで協調させ、閉ループで検知から修復まで進める。

## 設計のポイント

- センサーとアクチュエータの層で信号取得と封じ込め・権限剥奪などの実行手段を分け、その上にエージェント用のコンテキスト層を置く。
- 役割別の専門エージェントをプレイブックとハーネスで束ね、タスクごとに適切なモデルを使い分ける。
- ガードレールと高影響アクションの承認は人間が持ち、自動トリガーで起動する範囲を限定する。
- AI利用コストのダッシュボードで支出とセキュリティ成果を結びつける。

## 使いどころ

- アラート量が多く、一次調査を自動化したいSOCチーム。
- エージェント自体のアクセス管理が必要なエンタープライズ。
- 攻撃シミュレーションから修復までを一貫して回したいセキュリティ部門。
