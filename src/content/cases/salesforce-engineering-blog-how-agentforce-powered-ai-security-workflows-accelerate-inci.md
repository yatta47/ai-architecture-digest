---
type: case
title: Salesforce Security CenterがAgentforceで長時間稼働のセキュリティ調査基盤に進化
title_original: How Agentforce-powered AI security workflows accelerate incident response
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- guardrails
components:
- Agentforce
- Salesforce Security Center
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-agentforce-powered-ai-security-workflows-accelerate-incident-response/
published_at: '2026-08-12'
---

## 概要

SalesforceがAgentforce搭載のSecurity Centerを、単発の会話型AIから長時間稼働するステートフルなインシデント調査プラットフォームへ拡張した事例。自然言語でのテレメトリ調査・remediation追跡・監査を可能にし、AIによるAI評価パイプラインでLLMの非決定性を検証しながらエンジニアリング速度を2〜3倍に高めた。

## 設計のポイント

- 会話型インターフェースだけでは長時間に及ぶインシデント対応（トリアージ〜解決）を支えられないと判断し、状態管理・remediation追跡・監査機能を持つ調査プラットフォームへ拡張する
- LLM同士でLLMの挙動を検証するAI駆動評価パイプラインを構築し、厳密な文言一致ではなく意図した調査挙動との整合性を判定することでテストのスループットを10〜20倍に高める
- テレメトリシステムごとに異なるデータモデルを吸収する拡張可能な調査データモデルを設計し、特定の脅威タイプに密結合しないアーキテクチャにする

## 使いどころ

- 分散したセキュリティテレメトリを横断して調査するアナリストの負荷を減らしたいセキュリティ運用チーム
- 非決定的なLLM挙動を高頻度にリグレッションテストしたいAIプロダクトチーム
