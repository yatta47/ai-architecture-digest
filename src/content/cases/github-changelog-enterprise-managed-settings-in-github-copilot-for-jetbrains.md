---
type: announcement
title: JetBrains版GitHub CopilotにMCPサーバー許可リストなどの企業管理設定が追加
title_original: Enterprise managed settings in GitHub Copilot for JetBrains
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- guardrails
- policy-as-code
components:
- GitHub Copilot
- JetBrains
- MCP
- OpenTelemetry
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-18-enterprise-managed-settings-in-github-copilot-for-jetbrains
published_at: '2026-08-18'
---

## 概要

GitHub Copilot for JetBrainsに、プラグインガバナンス、MCPサーバーの許可/拒否リスト、OpenTelemetryの一元設定、Bypass Approvals等の権限モード制御など、企業管理者向けの統制機能が追加された。管理側の設定値が開発者個人の設定より優先され、テレメトリの送信先や接続可能なMCPサーバーを組織全体で一貫して統制できる。

## 設計のポイント

- 許可/拒否リストでMCPサーバー接続先をエンタープライズ単位でホワイトリスト化し、承認外の外部ツール接続を防ぐ
- 管理者設定を開発者個人設定より優先させることで、テレメトリ送信先などのガバナンス要件を確実に適用する
- Bypass Approvals/Autopilotなど高権限の自律実行モードを組織側で無効化できるようにし、リスクの高い自動化を抑制する

## 使いどころ

- 複数IDEにまたがるAIコーディングエージェントのツール接続を一元統制したいセキュリティ・IT部門
- MCP経由の外部ツール接続を許可リスト方式で管理したいエンタープライズ組織
- AIエージェントのテレメトリを社内の観測基盤に確実に集約したい運用チーム
