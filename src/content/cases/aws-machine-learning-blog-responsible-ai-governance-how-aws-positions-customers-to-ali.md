---
type: guidance
title: ISO/IEC 42005に沿ったAIシステム影響評価の進め方
title_original: 'Responsible AI governance: How AWS positions customers to align with ISO/IEC 42005:2025'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- guardrails
- policy-as-code
components:
- Amazon Bedrock
- ISO/IEC 42005
- ISO/IEC 42001
- AWS Well-Architected Responsible AI Lens
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/responsible-ai-governance-how-aws-positions-customers-to-align-with-iso-iec-420052025/
published_at: '2026-10-06'
---

## 概要

AIシステム影響評価の国際規格ISO/IEC 42005:2025を、企業の既存リスク管理に統合する方法をAWSが解説した記事。評価のライフサイクル、再評価トリガー、記載すべき項目、統合型（Annex D）と単独テンプレート型（Annex E）の選択肢を整理している。

## 設計のポイント

- 軽量なトリアージで本評価の要否を先に判定し、リスクに応じて評価の深さを変える。
- 法務・セキュリティ・プライバシー等の既存レビューと統合して重複評価を避ける。
- 法令変更やシステム変更など再評価トリガーを事前に定義して継続的に見直す。

## 使いどころ

- AIガバナンスの仕組みを新規に立ち上げる推進担当者。
- ISO/IEC 42001認証取得を目指す組織が影響評価プロセスを整備する場面。
