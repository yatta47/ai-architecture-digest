---
type: case
title: クラウド脆弱性の調査から安全確認・修復まで行うTamnoonのエージェント「Tami」
title_original: How Tamnoon built AI-powered cloud security remediation with Amazon Bedrock
company: Tamnoon
industry: cross-industry
cloud:
- aws
- azure
- gcp
- multi-cloud
patterns:
- ai-agent
- guardrails
- human-in-the-loop
- root-cause-analysis
components:
- Amazon Bedrock
- CNAPP
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-tamnoon-built-ai-powered-cloud-security-remediation-with-amazon-bedrock/
published_at: '2026-10-14'
---

## 概要

CNAPP等が出す大量のセキュリティ指摘に対し、Tamiが所有者や依存関係を調査し、修復が安全かを判定して修正を生成・実行するエージェント型オーケストレーター。ガバナンスとガードレールを効かせ、90日で重大なクラウド露出を90%以上削減し本番障害はゼロだった。

## 設計のポイント

- 本番に触れる前に調査・優先順位付け・修復計画を済ませ、安全性の確信度で自動化の可否を決める
- 関連する指摘を根本原因でクラスタ化し、まとめて解消する
- 専門家の確認とガードレールを組み合わせて顧客環境への変更を統制する

## 使いどころ

- アラート過多で修復が滞るクラウドセキュリティチーム
- 本番影響を懸念して自動修復を導入できない組織
