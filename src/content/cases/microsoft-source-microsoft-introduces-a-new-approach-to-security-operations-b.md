---
type: announcement
title: エージェント時代のSOCを統合したMicrosoft Defenderの統合セキュリティ運用基盤(ISOC)
title_original: Reimagining the SOC for the agentic era in Microsoft Defender
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- defense-in-depth
- human-in-the-loop
components:
- Microsoft Defender
- Microsoft Sentinel
- Project Perception
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/
published_at: '2026-09-23'
---

## 概要

MicrosoftはSIEMと脅威防御を一体化した統合セキュリティ運用センター(ISOC)をMicrosoft Defenderのプレビューとして発表した。シグナル/センサー、コンテキスト、アクチュエーターを一つの基盤に統合し、人とエージェントが同じ土台で検知・調査・対処できるようにする。

## 設計のポイント

- シグナル・コンテキスト・アクチュエーターを別システムにせず単一基盤に統合し、エージェントがツール間の受け渡しで遅くならないようにしている。
- 検知から防御強化までを循環させる統合プロテクションループ(攻撃中断など)を製品にネイティブ実装し、利用者による組み立て・調整を不要にしている。
- エージェントは継続実行と規模を担い、人は優先順位付けと判断を担う役割分担にしている。

## 使いどころ

- 攻撃者のエージェント自動化に対抗したいSOCチーム。
- SIEMとXDRの分断でコンテキスト再構築に時間を取られているセキュリティ担当者。
- SOCにエージェントを段階的に導入したい組織。
