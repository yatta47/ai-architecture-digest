---
type: announcement
title: オープンウェイトモデルKimi K3がGitHub Copilotで利用可能に
title_original: Kimi K3 is now available in GitHub Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
components:
- GitHub Copilot
- Kimi K3
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-06-kimi-k3-is-now-available-in-github-copilot
published_at: '2026-08-06'
---

## 概要

オープンウェイトモデルのKimi K3が、GitHub Copilotの利用量課金モデルとして一般提供された。Fireworks AI上でGitHubがホストし、VS CodeやJetBrainsなど主要エディタのモデルピッカーから選択できるが、Copilot BusinessおよびEnterpriseではデフォルト無効で管理者がポリシーを有効化する必要がある。

## 設計のポイント

- オープンウェイトモデルを既存のモデルピッカーに統合し、利用量課金として提供することでコスト効率的な選択肢を増やす
- 組織のポリシーでモデルごとに有効/無効を切り替えられるようにし、セキュリティ・コンプライアンス審査前は既定オフとする

## 使いどころ

- コーディングエージェント用途でコストパフォーマンスの高いモデルを選びたい開発者
- オープンウェイトモデルの利用可否を組織のガバナンスポリシーとして管理したいEnterprise管理者
