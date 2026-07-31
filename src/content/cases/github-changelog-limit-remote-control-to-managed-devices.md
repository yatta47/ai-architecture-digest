---
type: announcement
title: GitHub CopilotのリモートコントロールをMDM管理デバイスに限定するポリシーを追加
title_original: Limit remote control to managed devices
industry: cross-industry
cloud: []
patterns:
- guardrails
- policy-as-code
components:
- GitHub Copilot
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-30-limit-remote-control-to-managed-devices
published_at: '2026-07-30'
---

## 概要

GitHubは、Copilotのリモートコントロールセッションをホストできるデバイスを管理者が制限できるenterprise managed setting「remoteControl」を追加した。組織ポリシーとデバイス単位の設定を組み合わせ、SSO必須化や無効化などをサーバー管理・MDM管理・ファイルベースの3経路で配布できる。

## 設計のポイント

- 既存の全体ポリシー（利用可否）とデバイス単位の設定（remoteControl）を階層化し粗い制御と細かい制御を両立する
- サーバー管理・MDM管理・ファイル配布という3つの適用経路を用意し組織の管理体制に合わせて選べるようにする

## 使いどころ

- AIエージェントのリモートセッションを管理対象デバイスのみに限定したいセキュリティ管理者
- SSOによる認可を必須化してCopilotの遠隔操作を統制したいエンタープライズ組織
