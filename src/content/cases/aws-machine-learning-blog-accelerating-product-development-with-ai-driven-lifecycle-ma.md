---
type: guidance
title: AWS Quickの6エージェントで製品開発の上流工程を人間承認付きで回すAI-PDLC
title_original: Accelerating product development with AI-driven lifecycle management (AI-PDLC) in AWS Quick
industry: cross-industry
cloud:
- aws
patterns:
- multi-agent-orchestration
- human-in-the-loop
- spec-driven-development
- context-engineering
components:
- AWS Quick
- Agent Client Protocol
- Kiro
- Claude Code
- Slack
- Jira
- Salesforce
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/accelerating-product-development-with-ai-driven-lifecycle-management-ai-pdlc-in-aws-quick/
published_at: '2026-11-11'
---

## 概要

AWS Quick上の6つの専門エージェントで、顧客課題の発見から優先順位付け、PR/FAQ、仕様、プロトタイプまでを一貫して進めるAI-PDLCの構成を解説する。Orchestratorが単一の会話で各段階を進め、人間の承認を通過しないと次へ進まない。生成した仕様はACP経由でKiroやClaude Codeなどのコーディングエージェントへ引き渡す。

## 設計のポイント

- 利用者は Orchestrator とだけ対話し、専門エージェントへの振り分けは Orchestrator が実行時に行う。
- 全段階に人間の承認ゲートを置き、判断は人、下書きと構造化はエージェントに分担する。
- 成果物を prototype_spec.md に集約し、各要求を元の課題・優先度・PR/FAQ まで追跡できるようにする。
- ACP（オープンな JSON-RPC 2.0）でコーディングエージェントに引き渡し、ベンダーロックインを避ける。

## 使いどころ

- Slack・Jira・Salesforce などに散在する顧客シグナルから開発判断を行いたい製品チーム。
- 仕様の根拠を残したままコーディングエージェントへ引き継ぎたい場面。
