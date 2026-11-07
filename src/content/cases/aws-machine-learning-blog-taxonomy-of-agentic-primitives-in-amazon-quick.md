---
type: guidance
title: Amazon Quickのエージェント基本要素の分類(トリガー・エージェント・能力)
title_original: Taxonomy of agentic primitives in Amazon Quick
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- memory-consolidation
- context-engineering
components:
- Amazon Quick
- MCP
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-agentic-primitives-in-amazon-quick/
published_at: '2026-11-06'
---

## 概要

Amazon Quickで、エージェント作業をWhen/What/Who/Howの4問でトリガー、エージェント、ツール・スキル・ワークフローに分解した共通語彙を示す。エージェントは学習し続ける永続的な主体と定義し、スキルとワークフローを相互に変換できるとする。

## 設計のポイント

- トリガー(人・エージェント委任・スケジュール・イベント)を実行特性を決める独立要素として扱う。
- エージェントは指示・能力・学習済み文脈で構成し、LLMは差し替え可能なパラメータとする。
- ツール/スキル/ワークフローを自由度と決定性の軸で使い分け、スキルのワークフロー化(結晶化)も許容する。

## 使いどころ

- エージェント基盤の用語と設計単位を揃えたい製品チーム。
- 「Slack要約を毎朝」のような要求を新エージェントにせず既存エージェントへのトリガー追加で実現したい場面。
