---
type: case
title: BMW Groupが数百のエージェントを数千人の開発者向けにガバナンスする構成
title_original: How the BMW Group governs hundreds of agents across thousands of developers
company: BMW Group
industry: manufacturing
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- policy-as-code
components:
- Amazon Bedrock AgentCore
- Strands Agents
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-the-bmw-group-governs-hundreds-of-agents-across-thousands-of-developers/
published_at: '2026-11-19'
---

## 概要

BMW R&Dの12,500人超の開発者向けに、数百のエージェントを安全・低コストで運用するため、LLM周りの実行層（エージェントハーネス）を標準化する構成を紹介する。単一のフレームワークに縛らず、相互連携できるエージェントを統治可能にする。

## 設計のポイント

- ハーネスで実行ループ・ツール呼び出し・メモリ・可観測性フックを共通化する。
- チームの自由な実験と、安全・コスト基準の全社統制を両立させる。
- フレームワークを問わず合成可能にして、AIの孤立した島を防ぐ。

## 使いどころ

- 大規模組織でエージェントの乱立を防ぎたい基盤チームに向く。
- 規制産業で品質とガバナンスを保ちたい場合に有効。
