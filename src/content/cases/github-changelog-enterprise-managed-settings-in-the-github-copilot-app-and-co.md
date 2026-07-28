---
type: announcement
title: エンタープライズ管理設定をGitHub CopilotアプリとクラウドエージェントにもConfig
title_original: Enterprise managed settings in the GitHub Copilot app and Copilot cloud agent
company: GitHub
industry: cross-industry
cloud: []
patterns:
- policy-as-code
- guardrails
- llmops
components:
- GitHub Copilot app
- Copilot cloud agent
- GitHub Copilot CLI
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-27-enterprise-managed-settings-now-apply-to-the-github-copilot-app
published_at: '2026-07-27'
---

## 概要

GitHub Copilotのエンタープライズ管理設定（managed-settings.json）が、これまでのCLIとVS Codeに加えCopilotアプリとクラウドエージェントにも適用されるようになった。プラグインの許可リストや承認プロンプトのバイパス可否などのガードレールを一箇所で定義すれば、全クライアントに一貫して強制される。

## 設計のポイント

- ガバナンスポリシーを単一の設定ファイルに集約し、対応する全クライアントで一貫して強制することで、統制が及ばないクライアントという抜け穴を作らない

## 使いどころ

- 複数のAIコーディングクライアントを横断してプラグインやコマンド実行の統制を一元管理したいエンタープライズ管理者
