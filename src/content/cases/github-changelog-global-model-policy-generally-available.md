---
type: announcement
title: GitHub Copilot、組織単位のデフォルトモデルポリシーを一般提供開始
title_original: Global model policy generally available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- policy-as-code
- llm-gateway
components:
- GitHub Copilot
- GitHub Copilot Business
- GitHub Copilot Enterprise
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-26-global-model-policy-generally-available
published_at: '2026-08-26'
---

## 概要

GitHubは、Copilot BusinessおよびEnterpriseプランの一般提供モデルに対する組織全体のデフォルト有効化ポリシーの適用を9月1日にかけて順次展開する。未設定のモデルは動的に組織ポリシーへ追従する一方、管理者が個別モデルに対して行った明示的な有効/無効設定は維持され、オープンウェイトモデルやデータ保持契約対象外のモデルはポリシーに関わらずデフォルト無効のままとなる。

## 設計のポイント

- 『デフォルトポリシーに委任』という動的状態を導入し、新規追加モデルも管理者がポリシーを変更するたびに自動追従させる
- 管理者による個別モデルへの明示的なオン/オフ設定は常に優先し、ポリシー変更で上書きしない
- オープンウェイトモデルやデータ保持契約の対象外モデルは、ポリシー設定によらず既定で無効化しコンプライアンスリスクを抑える

## 使いどころ

- 多数の新モデルが次々追加される中で、どのLLMを従業員に使わせるかを組織単位で一元統制したいIT/セキュリティ管理者
- データ保持要件などのコンプライアンス制約を満たしつつ、モデル追加のたびに個別設定する手間を省きたいエンタープライズ組織
