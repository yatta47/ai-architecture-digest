---
type: announcement
title: Copilotテレメトリのユーザー帰属と取得内容の細かな制御
title_original: Client telemetry user attribution and configurable capture
company: GitHub
industry: cross-industry
cloud: []
patterns:
- guardrails
- policy-as-code
- llmops
components:
- GitHub Copilot
- OpenTelemetry
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-12-client-telemetry-user-attribution-and-configurable-capture
published_at: '2026-10-12'
---

## 概要

マネージド設定のtelemetry.capture.identityで、プロンプトや応答を収集せずにユーザーへ活動を帰属できる。prompts・responses・toolArgumentsなど5種の取得クラスを個別に制御でき、すべて既定でオフである。

## 設計のポイント

- 識別情報と内容取得を分離する。
- 既定はすべてオフとし、監査に必要な分だけ有効化する。

## 使いどころ

- Copilot利用の監査と、機密情報収集の最小化を両立したい管理者。
