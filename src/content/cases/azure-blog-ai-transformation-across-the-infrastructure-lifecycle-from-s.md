---
type: case
title: AzureインフラのサプライチェーンでのLean before AIとマルチエージェント活用
title_original: 'AI transformation across the infrastructure lifecycle: From supply chain to fleet operations'
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- multi-agent-orchestration
- ai-agent
- human-in-the-loop
- parallel-execution
components:
- Azure
- multi-agent workflow
outcome:
  type: speed
source_id: azure-blog
source_name: Azure Blog
source_url: https://azure.microsoft.com/en-us/blog/ai-transformation-across-the-infrastructure-lifecycle-from-supply-chain-to-fleet-operations/
published_at: '2026-10-07'
---

## 概要

MicrosoftのAzureハードウェア部門は、プロセスを整理しデータ基盤を整えてからAIを載せる「Lean before AI」で、需要計画にマルチエージェントを導入した。数日かかった要因調査が数時間から20分未満になり、手作業は約50%、サイクルは最大75%減った。

## 設計のポイント

- 先に業務を単純化し、データ基盤と品質・権限統制を整えてからエージェントを置く。
- 需要変動の要因を複数エージェントが並列に調べ、順次の引き継ぎをなくす。
- 人が責任を持つ判断を明示し、人の判断を中心に残す。
- 計画、調達、物流のエージェントをつなぎ、学習ループを作る。

## 使いどころ

- 大規模な需給計画や調達業務にエージェントを導入する企業。
- 断片化した業務システムを横断した調査を短縮したい運用部門。
