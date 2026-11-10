---
type: case
title: 'Novus Hi-Tech FleetGPT: テレマティクス向けマルチエージェント'
title_original: Transforming fleet analytics for Novus Hi-Tech through agentic AI
company: Novus Hi-Tech
industry: logistics
cloud:
- aws
patterns:
- multi-agent-orchestration
- voice-agent
- ai-agent
- text-to-sql
components:
- Strands Agents SDK
- Amazon Bedrock
outcome:
  type: quality
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/transforming-fleet-analytics-for-novus-hi-tech-through-agentic-ai/
published_at: '2026-11-09'
---

## 概要

Novus Hi-TechはAWS PACEと、運転警告の調査と運転手への音声連絡を自動化するFleetGPTを構築した。自然言語クエリ、自動調査、AI音声通話を備え、違反を46%、居眠り警告を55%減らした。

## 設計のポイント

- ロールごとの必要を分けて対応する。
- 警告の判断をエージェント化しオペレーター負荷を下げる。

## 使いどころ

- 大規模車両運行の安全管理
