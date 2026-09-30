---
type: announcement
title: Claude Managed AgentsとNVIDIA OpenShellによるエージェントの多層防御
title_original: Giving companies more control over their AI agents, with NVIDIA
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- defense-in-depth
- policy-as-code
- guardrails
components:
- Claude Managed Agents
- NVIDIA OpenShell
- NVIDIA Open Agent Safety Platform
- Claude
outcome:
  type: risk-compliance
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia
published_at: '2026-09-28'
---

## 概要

NVIDIAが発表したOpen Agent Safety Platformに合わせ、AnthropicはClaude Managed AgentsとオープンソースのNVIDIA OpenShellを組み合わせ、モデル外側でエージェントの行動を制限・監査する多層防御を提供する。Managed Agentsはエージェントループをサンドボックスと別サーバーで動かし、認証情報をボールトに保持してエージェントに見せず、監査証跡を残す。OpenShellはデフォルト拒否でツール・ファイル・ネットワーク・データへのアクセスをポリシーで強制し、全判定をログ化してポリシープルーバーで到達範囲を数学的に検証する。

## 設計のポイント

- エージェントループの実行サーバーと作業用サンドボックスを分離し、認証情報は別のボールトに保持してエージェントから見えないようにする。
- モデル内の安全策に加え、モデル外で独立に強制される複数の防御層を重ね、単一層に依存しない構成にする。
- デフォルト拒否のポリシーを外部ランタイムで強制し、許可・拒否の全判定をログに残して監査可能にする。
- 狭い権限から始めてログをレビューし、Claudeで最小権限に向けてルールを絞り込み、ポリシープルーバーで到達範囲を証明する。

## 使いどころ

- 独自データや業務システムにアクセスして代理でアクションを行うエージェントを本番導入する企業。
- エージェントの権限を最小化し、行動を監査・検証できる形でガバナンスを効かせたいセキュリティ・プラットフォームチーム。
- 自社インフラや任意のマネージドプロバイダ上のサンドボックスでエージェントを動かしたい組織。
