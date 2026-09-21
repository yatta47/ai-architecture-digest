---
type: announcement
title: GitHub CopilotにxAIのGrok 4.7が追加
title_original: Grok 4.7 is now available in GitHub Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
components:
- GitHub Copilot
- Grok 4.7
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-21-grok-4-7-is-now-available-in-github-copilot
published_at: '2026-09-21'
---

## 概要

xAIの推論モデルGrok 4.7が、エージェント型コーディングや複数ステップのワークフロー向けにGitHub Copilotのモデルピッカーへ順次展開される。Copilot Pro/Pro+/Max/Business/Enterpriseの各SKUで利用でき、EnterpriseとBusinessの管理者はモデルポリシーで有効化・無効化を制御できる。

## 設計のポイント

- 新モデルはデフォルトで自動有効化される運用にし、管理者が明示的に無効化しない限りロールアウトと同時に組織内で使えるようにする
- 利用量に応じた従量課金(プロバイダのリストプライス)をモデル単位で適用し、複数モデルを併存させたコスト管理を可能にする

## 使いどころ

- VS Code・Visual Studio・JetBrains・Copilot CLIなど複数のIDE/クライアントで、エージェント的な複数ステップのコーディングタスクに強いモデルを選びたい開発者
- 組織のCopilot管理者が、新しいモデルの利用可否をポリシーで段階的にコントロールしたい場合
