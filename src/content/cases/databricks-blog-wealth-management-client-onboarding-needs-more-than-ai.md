---
type: guidance
title: ガバナンス付きケース文脈でウェルスマネジメントのオンボーディングを回すエージェント構成
title_original: Wealth management client onboarding needs more than AI
company: Databricks
industry: financial-services
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- document-processing
- context-engineering
components:
- Databricks Data + AI Platform
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/wealth-management-client-onboarding-needs-more-ai
published_at: '2026-10-30'
---

## 概要

書類抽出やKYCスクリーニングを個別に速くしても、システム間で証跡や案件状態が分断されるとオンボーディングは滞る。バージョン管理されたケース文脈をAIエージェントと人のレビュー担当が共有し、統制と追跡性を保ったまま全体を調整する構成を提案する。

## 設計のポイント

- 証跡・例外・判断履歴を案件単位で一元化し、引き継ぎ時の再構築をなくす。
- エージェントを監督付きで動かし、ガバナンスと人間の判断を残す。
- サイクルタイム、手作業回数、承認から入金までの時間で効果を測る。

## 使いどころ

- CRM・KYC・カストディなど複数システムをまたぐ金融機関のオンボーディング部門。
- タスク単位のAI導入で全体の待ち時間が減らない業務の改善担当者。
