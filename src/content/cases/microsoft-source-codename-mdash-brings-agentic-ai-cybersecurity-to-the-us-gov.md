---
type: case
title: 100以上のAIエージェントによる多モデル脆弱性スキャン基盤MDASH
title_original: Codename MDASH brings agentic AI security scanning to US government
company: Microsoft
industry: public-sector
cloud:
- azure
patterns:
- ai-agent
- multi-agent-orchestration
- multi-model-routing
- defense-in-depth
components:
- Azure Government
- Microsoft Defender
- Microsoft Foundry
- MAI model family
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/microsoft-cloud/blog/us-government/2026/09/08/codename-mdash-brings-agentic-ai-security-scanning-to-us-government/
published_at: '2026-09-08'
---

## 概要

Microsoftはソースコードの脆弱性を発見するエージェント型スキャナ「codename MDASH」をAzure Governmentに展開し、米国政府機関にプレビュー提供を開始した。100以上の専門エージェントが並行して脆弱性候補を検出し、別のエージェント群が到達可能性・危険性を議論して精査することで誤検知を抑え、CyberGymベンチマークで96.55のスコアを達成している。

## 設計のポイント

- 検出エージェント群と検証（賛否を議論する）エージェント群を分離し誤検知を絞り込む2段構成にする
- 特定モデルに縛られないハーネス設計にし新モデル登場時に差し替えるだけで性能とコストを改善できるようにする
- 複数モデルの意見の一致・不一致自体を確信度のシグナルとして利用する
- FedRAMP High認定のAzure Governmentと分離することで機密性の高いソースコード解析を認可済み境界内に収める

## 使いどころ

- ミッションクリティカルなソフトウェアの全量を人手でレビューしきれない政府機関のセキュリティチーム
- 既存の検出パターンでは見逃す複雑なサプライチェーン上の脆弱性を優先度付けして洗い出したい組織
- 脅威アクターのAI活用に対抗するため脆弱性発見と修正のスピードを上げたい防御側
