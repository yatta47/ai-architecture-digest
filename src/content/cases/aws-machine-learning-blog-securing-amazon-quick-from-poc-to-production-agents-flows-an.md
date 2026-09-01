---
type: guidance
title: Amazon QuickのAgent/Flow/Spacesを本番運用へ安全にスケールする設計パターン
title_original: 'Securing Amazon Quick from POC to production: Agents, Flows, and Spaces'
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- guardrails
- human-in-the-loop
- rag
components:
- Amazon Quick
- AWS CloudTrail
- AWS Secrets Manager
- AWS IAM Identity Center
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/securing-amazon-quick-from-poc-to-production-agents-flows-and-spaces/
published_at: '2026-09-01'
---

## 概要

Amazon Quickのダッシュボード・エージェント・フロー・Spacesを、パイロットから複数部門・数千人規模の本番運用へ拡張する際のセキュリティ設計を解説する。データセット分割・エージェント分離・ドキュメント分類・承認ゲートの4パターンを、権限設定だけに頼らずデータアーキテクチャ自体で安全性を担保する方針で構成する。

## 設計のポイント

- 機微な列をデータセット段階で物理的に除去し、権限設定のミスがあっても漏えいしない構造的な安全性を確保する
- 1エージェントにつき1つの用途特化データセットのみを接続し、意図しないスコープ外データへのアクセスを防ぐ
- ナレッジベースには機微文書を権限制御でなく除外という形で反映し、監査時に見えないことを保証する
- Flowの対外アクションの前段に人間承認ゲートを設け、自動化と統制を両立する

## 使いどころ

- BIツールのPOCを複数部門・大規模ユーザーへ展開する際にセキュリティレビューで止まりがちな組織
- 部署ごとに異なる権限レベルで同一データを扱う必要があるHR/財務など機微データ活用チーム
- エージェントやナレッジベースを含むBI基盤のガバナンス設計を求められるプラットフォームチーム
