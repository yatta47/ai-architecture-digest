---
type: guidance
title: スキル搭載エージェントの選択・遵守を分離して評価する手法
title_original: Evaluate skill-equipped agents with Strands Evals and Amazon Bedrock AgentCore
industry: cross-industry
cloud:
- aws
patterns:
- eval
- ai-agent
components:
- Strands Agents SDK
- Strands Evals SDK
- Amazon Bedrock AgentCore
- Amazon Bedrock AgentCore Evaluations
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/evaluate-skill-equipped-agents-with-strands-evals-and-amazon-bedrock-agentcore/
published_at: '2026-09-22'
---

## 概要

SKILL.mdで定義したスキルを組み合わせるエージェントは、最終出力だけを見ても「不適切なスキルを選んだ」失敗と「正しいスキルを選んだが手順を守らなかった」失敗を見分けられない。Strands EvalsとAmazon Bedrock AgentCore Evaluationsは、この2種類の失敗をスキル単位で切り分けて測定する評価指標を提供する。

## 設計のポイント

- Skill Selection Accuracyでタスクに対するスキル選択の妥当性を二値で評価する
- Skill Instruction Followingで選んだスキルの手順をどこまで遵守したかを5段階で根拠付きに評価する
- SkillInvokedによる決定的なロード確認と組み合わせ、既知のルーティング要件をもつ回帰テストを担保する
- スキルごとの結果が出るため複数スキルを跨ぐ実行でもどの選択・遵守判断がスコアを下げたか特定できる

## 使いどころ

- コンプライアンスチェックや文書処理など手順化された業務をスキル化しているエージェント運用チーム
- スキルの説明文が曖昧で誤ったスキル選択が起きていないか診断したい場合
- HRアシスタントのようにスキルごとに異なる遵守要件があるマルチスキルエージェントの品質保証
