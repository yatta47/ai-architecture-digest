---
type: case
title: AI SREを評価する前に既存エージェントへKubernetes文脈を与える検証
title_original: Before you evaluate an AI SRE, give your existing agent context
company: Radar (Skyhook.io)
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- context-engineering
- root-cause-analysis
- eval
components:
- Claude Code
- Amazon EKS
- Amazon Bedrock
- SREGym
- Radar MCP
outcome:
  type: speed
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/21/before-you-evaluate-an-ai-sre-give-your-existing-agent-context/
published_at: '2026-10-21'
---

## 概要

同じエージェントとモデルで50件のK8s障害を、素のkubectlと読み取り専用MCPの文脈ツールで比較した。正答は45対46と同程度だが、2分以内の正答が60%から86%に増え、平均診断時間は191秒から64秒に短縮した。

## 設計のポイント

- 現在の障害・変更履歴・関連リソース・エラーログを整理して返すMCPツールを用意する。
- ツール呼び出し回数が減りトークン消費も下がりやすい。
- 判断力の限界は変わらないため、製品導入前にベースラインを測る。

## 使いどころ

- AI SRE製品の導入前評価。
- インシデント対応の初動時間を短縮したい運用チーム。
