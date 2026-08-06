---
type: guidance
title: コーディングエージェント向けAgent SkillsでAutomated Reasoningポリシーのライフサイクルを自動化
title_original: Agent Skills for Automated Reasoning policies in Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- guardrails
- eval
- policy-as-code
components:
- Amazon Bedrock Automated Reasoning checks
- Amazon Bedrock Guardrails
- Claude Code
- Kiro
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/agent-skills-for-automated-reasoning-policies-in-amazon-bedrock/
published_at: '2026-08-06'
---

## 概要

Amazon Bedrock Automated Reasoning checksのポリシー作成・レビュー・テスト・デバッグ・デプロイ・検証という6段階のライフサイクルを、Claude Codeなどのコーディングエージェントに組み込むAgent Skillsのスイートとして提供。SMT-LIBによるルール記述やAPIの制約といった学習コストの高い部分をスキルが肩代わりし、形式検証による数学的な正しさの保証を運用に乗せやすくする。

## 設計のポイント

- ポリシーのライフサイクルを1段階1スキルに分割し、各スキルにSKILL.md（判断基準）・references（詳細資料）・scripts（実行可能コード）を持たせる
- 誤判定の大半は『ルールの誤り』ではなく『自然言語から論理式への翻訳の誤り』であるという原則をデバッガースキルの診断ロジックに組み込む
- スクリプトに--dry-runを用意し、Amazon Bedrock APIに実際のリクエストを送る前に内容を確認できるようにする
- オープンなAgent Skills形式を使うことで、Claude Code・Kiro・Cursor・Codexなど複数のコーディングエージェントに同一スキルを配布できるようにする

## 使いどころ

- 人事規定やローン審査基準など、書かれたルールに厳密に従う必要がある業務でAIの回答を形式検証したいチームとして
- Automated Reasoningポリシーの作成・改訂をコンソール操作でなくコードレビュー可能な形で運用したいチームとして
- ガードレールに紐づくポリシーのビルド・テスト・デプロイをCI/CDやエージェント経由で再現可能にしたい場合として
