---
type: announcement
title: GitHub Copilot、cloud agent・Chat・Mobileを単一の『エージェントセッション』体験に統合
title_original: Upcoming changes to GitHub Copilot policies and billing
company: GitHub
industry: cross-industry
cloud: []
patterns:
- unified-runtime
- ai-agent
components:
- GitHub Copilot
- Copilot cloud agent
- GitHub Copilot code review
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-28-upcoming-changes-to-github-copilot-policies-and-billing
published_at: '2026-08-28'
---

## 概要

GitHubはCopilot Business/Enterpriseのサインアップ再開に伴いシート単位の前払い課金へ移行するほか、Copilot cloud agent・github.com上のCopilot Chat・GitHub Mobile版Copilot Chatをサンドボックス基盤上の単一のエージェントセッション体験へ統合する。統合後はチャットデータの保持期間が28日から契約期間全体に延び、Copilotコードレビューのデフォルト実行レベルもLiteからBalancedへ変更される。

## 設計のポイント

- 複数チャネル（Web/Mobile/cloud agent）に分かれていたAIエージェント体験を単一のセッションモデルへ統合する
- 統合後のデータ保持ポリシー変更（28日→アカウント存続期間）を明示し、既存ポリシーとの互換性をオプトインで維持する
- レビュー効果レベルなどのデフォルト値変更を事前告知し、組織/リポジトリ単位で明示的に上書きできる猶予期間を設ける

## 使いどころ

- 複数チャネルに分散したAIエージェント機能のポリシー管理を一本化したいEnterprise管理者
- Copilotのシート課金・データ保持ポリシー変更が既存の契約や監査要件に与える影響を事前に把握したい組織
