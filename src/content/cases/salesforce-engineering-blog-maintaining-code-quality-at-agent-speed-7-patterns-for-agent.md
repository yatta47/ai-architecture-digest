---
type: case
title: Salesforce Agent Fabricチームが実践する、エージェント生成コードを高速に信頼するための7つの設計パターン
title_original: 'Maintaining Code Quality at Agent Speed: 7 Patterns for Agentic Engineering'
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- ai-agent
- ci-cd
- guardrails
- eval
components:
- Salesforce Agent Fabric
outcome:
  type: quality
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/maintaining-code-quality-at-agent-speed-7-patterns-for-agentic-engineering/
published_at: '2026-06-17'
---

## 概要

AIコーディングエージェントの生成速度がボトルネックでなくなった結果、Salesforceのエンジニアリング組織では「どれだけ速く書けるか」ではなく「どれだけ速く信頼できるか」が課題の本質になったと指摘する。Agent Fabricチームは、検証をコード生成そのものより難しい一級の設計制約として扱い、テストの作成者と採点者を分離する、プロンプトではなくパイプライン上の品質ゲートで規約を強制する、エージェント固有の失敗モードを学習して設計に織り込むなど、7つのパターンから成るエンジニアリングモデルを確立した。

## 設計のポイント

- 同じエージェントがコードとテストの両方を書くとテストの合格がコードの正しさを保証しなくなるため、テストの作成者（エージェント）と採点者（独立した正しさの定義）を意図的に分離する。
- 「モックを使うな」のような規約はプロンプトで伝えるだけでは順守が安定しないため、パイプライン上の自動品質ゲートとして強制し、違反した変更はビルドを失敗させる。
- エージェントの典型的な失敗パターン（ゲートの文言だけを満たす迂回策など）をカタログ化し、単一のゲートではなく複数の仕組みで意図そのものを検証できるように設計する。

## 使いどころ

- AIコーディングエージェントの導入でコード生成量が急増し、レビュー・テスト・CI/CDが追いつかなくなっているエンジニアリング組織。
- エージェントに『モックを使うな』などの規約を守らせたいが、プロンプトだけでは順守が安定しないチーム。
- 複数のエージェントを並行稼働させながら、コードの信頼性を担保する仕組みを設計したいプラットフォームチーム。
