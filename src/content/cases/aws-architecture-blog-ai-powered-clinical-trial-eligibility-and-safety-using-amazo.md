---
type: guidance
title: 臨床試験の適格性・安全性判定を支援するマルチエージェント構成
title_original: AI-powered clinical trial eligibility and safety using Amazon Bedrock AgentCore
industry: healthcare
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
- guardrails
components:
- Amazon Bedrock AgentCore
- AWS HealthLake
- Amazon Bedrock Knowledge Bases
- Amazon Bedrock Guardrails
- Amazon Bedrock AgentCore Evaluations
- MCP Gateway
- Amazon CloudWatch
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/ai-agents-for-clinical-trial-screening/
published_at: '2026-08-19'
---

## 概要

臨床試験の登録遅延（1日あたり推定50万ドルのコスト）を解消するため、AWS HealthLakeでFHIR化した患者データをAmazon Bedrock AgentCore上の3つの専門エージェント（事前スクリーニング・詳細スクリーニング・サイト/登録）が段階的に評価し、根拠付きの推奨を提示する参照アーキテクチャを示す。最終判断は常に臨床医が行い、Bedrock Guardrailsで PII/PHI保護とグラウンディングを担保する。

## 設計のポイント

- 知識グラフでEHR・検査・投薬歴などの断片的データを患者・分子・エンドポイントの関係として統合し、都度の結合クエリを回避する
- スクリーニングを事前判定・詳細判定・登録手続きの3エージェントに分割し、それぞれをAgentCore Runtimeのセッションメモリで連携させる
- Guardrailsで PII/PHIフィルタリング・コンテンツ安全性・根拠グラウンディングを一律に適用し、エージェント出力を検証可能にする
- 全アクションを不変の監査証跡に記録し、最終決定権を臨床医に残すヒューマン・イン・ザ・ループを設計に組み込む

## 使いどころ

- 治験のスクリーニング業務で膨大なチャートレビューを効率化したいソリューションアーキテクトやスタディチーム
- プロトコルが複雑化する精密腫瘍学・バイオマーカー主導の適格性判定を扱う施設
- AI判断の説明可能性と人間の最終承認を両立させたいヘルスケア領域のエージェント設計
