---
type: opinion
title: エージェントの権限境界はプラットフォームで担保すべきという主張
title_original: The boundary problem in agentic AI is a platform problem
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- policy-as-code
- defense-in-depth
components:
- Kubernetes
outcome:
  type: risk-compliance
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/29/the-boundary-problem-in-agentic-ai-is-a-platform-problem/
published_at: '2026-10-29'
---

## 概要

エージェントの権限は意図的に決められず、ツールや認証情報の追加で徐々に膨らむと指摘し、境界をエージェント自身の指示に任せず、誰も見ていなくても強制されるプラットフォーム基盤で守るべきだと論じる。プロンプトは意図の表明にすぎず、ツール結合が実際の権限を決めるという整理が核。

## 設計のポイント

- 境界の強制をプロンプトではなく、ツールバインディングや認証情報などの実効権限を決める基盤層に置く。
- 権限が決定なしに累積する前提で、ツールや委任の範囲を継続的に可視化・制約する。
- 確率的に振る舞うエージェントの逸脱を、決定論的な基盤の制御で受け止める。

## 使いどころ

- 本番で複数ツールや認証情報を持つエージェントを運用するプラットフォームチーム。
- エージェントのガバナンスをレビュー運用でなく仕組みで担保したい場面。
