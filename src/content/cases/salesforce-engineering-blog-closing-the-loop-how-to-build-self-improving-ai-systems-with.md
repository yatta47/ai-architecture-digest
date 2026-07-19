---
type: case
title: レビューコメントから学習し自己改善するスキル生成エージェント
title_original: 'Closing the Loop: How to Build Self-Improving AI Systems with Automated Feedback Loops'
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- ci-cd
- human-in-the-loop
components:
- Claude Sonnet
outcome:
  type: productivity
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/closing-the-loop-how-to-build-self-improving-ai-systems-with-automated-feedback-loops/
published_at: '2026-07-17'
---

## 概要

Salesforceのエンジニアリングチームは、コーディング規約を教え込むメタスキル生成エージェント「creating-sf-skill」を構築し、PRレビューで繰り返されるコメントを自動収集してスキルの改善提案PRを作るフィードバックループを実装した。トリガー精度・構造検証・LLM-as-Judgeの3層評価でリグレッションを防ぎながら、レビューコメントの再発頻度が減衰していく自己収束型のシステムを実現している。

## 設計のポイント

- トリガー精度（動的評価）・構造検証（決定的スクリプト）・LLM-as-Judge（意味理解）の3層評価を役割分担させ、それぞれが検証できない領域を補い合う設計にする。
- 週次バッチで直近PRのレビューコメントを収集し、頻度×深刻度でパターンを優先度付けすることで、単発の指摘ではなく繰り返し発生する「暗黙の要求仕様」だけを拾い上げる。
- 1ループあたり最大5件・100行までと変更量を制限し、評価ゲートで退行を検知したら即座に適用を中止することでブラスト半径を抑える。
- 生成された修正は自動マージせず、参照PRつきの説明文を添えたドラフトPRとして人間レビューに委ねる。

## 使いどころ

- 社内のコーディング規約やレビュー基準をエージェントに繰り返し教え込んでいるチーム。
- 生成AIが作るアーティファクト（スキル・テンプレート・設定ファイルなど）の品質を継続的に検証し改善したい開発基盤チーム。
- レビュー負荷を減らしつつ、暗黙知を組織の資産として蓄積したいプラットフォームチーム。
