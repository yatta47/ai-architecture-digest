---
type: announcement
title: Copilotエージェント操作を統制するエンタープライズ管理権限
title_original: Enterprise-managed permissions for GitHub Copilot agent operations
company: GitHub
industry: cross-industry
cloud: []
patterns:
- guardrails
- policy-as-code
- ai-agent
components:
- GitHub Copilot Business
- GitHub Copilot Enterprise
- GitHub Copilot CLI
- Visual Studio Code
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-09-enterprise-managed-permissions-for-github-copilot-agent-operations
published_at: '2026-09-09'
---

## 概要

GitHub Copilot Business/Enterpriseの管理者が、エージェントによるシェルコマンド実行・ファイル読み書き・ネットワークアクセスなどの操作について、ブロック・承認要求・自動許可を組織単位で一元設定できる管理権限機能が一般提供された。この制御はユーザーやワークスペース側の設定・自動承認・過去の承認では上書きできず、チームごとに異なるポリシーも適用できる。

## 設計のポイント

- エージェントの危険操作(シェル実行・ファイル編集・ネットワークアクセス)をカテゴリ単位でポリシー化し、ブロック/要承認/自動許可の3段階で制御する
- 組織側の管理ポリシーをユーザー設定や自動承認より優先させ、権限昇格を防ぐ多層防御構成にする
- チーム/組織ごとに異なるポリシーセットを適用できるようにし、エージェント運用の柔軟性と統制を両立する

## 使いどころ

- 多数の開発者がAIコーディングエージェントを使う組織で、危険操作を無効化せずにガードレールを敷きたい場合
- セキュリティ・コンプライアンス部門がエージェントの権限範囲を中央集権的に監査・統制したい場合
