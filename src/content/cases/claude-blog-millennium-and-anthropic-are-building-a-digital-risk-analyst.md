---
type: case
title: 投資運用会社が人間監督下で動くデジタルリスクアナリストをClaudeで構築
title_original: Millennium and Anthropic are building a digital risk analyst with Claude
company: Millennium
industry: financial-services
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- guardrails
components:
- Claude
- Claude Code
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/millennium-and-anthropic-are-building-a-digital-risk-analyst-with-claude
published_at: '2026-08-06'
---

## 概要

Millenniumは、Anthropicと共同で「デジタルリスクアナリスト」を開発している。これはリスクマネージャーの監督下で資産クラス横断のリスクエクスポージャーに関する知見を提示するAIチームメイトで、自社データとClaudeの推論能力を組み合わせ、判断の根拠をログに残し、サンドボックスで検証したうえで人間の専門家が承認する運用になっている。

## 設計のポイント

- AIが出した所見は必ず人間のリスクマネージャーが検証・承認する運用にし、判断の主体を人間に残す
- 推論過程をログとして残し、監査可能性を確保する
- AIの提案アクションを本番実行前にサンドボックス環境でテストする

## 使いどころ

- 大量の資産クラス・ポジションにまたがるリスク変動要因を毎日説明する必要がある投資運用会社
- AIの判断を業務に組み込みつつ、規制・監査要件から人間の最終承認を外せない金融機関
