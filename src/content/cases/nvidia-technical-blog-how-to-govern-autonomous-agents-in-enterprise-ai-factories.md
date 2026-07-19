---
type: guidance
title: 'Secure Agent Workspace: エンタープライズ自律エージェントのガバナンス設計'
title_original: How to Govern Autonomous Agents in Enterprise AI Factories
industry: cross-industry
cloud:
- on-prem
- azure
patterns:
- ai-agent
- guardrails
- policy-as-code
- human-in-the-loop
components:
- NVIDIA OpenShell
- Red Hat OpenShift Virtualization
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-govern-autonomous-agents-in-enterprise-ai-factories/
published_at: '2026-07-09'
---

## 概要

AIエージェントが数時間にわたり自律的にコード検査やシステム操作を行うようになる中、NVIDIA Secure Agent Workspace Reference Designはユーザー端末を『提示層』、管理されたワークスペースを『実行層』として分離し、ID・ネットワーク・ポリシー・監査を一貫して統制する。管理VMの払い出し、SSO、ネットワーク遮断、人間承認、集中ログという第一段階に続き、サンドボックス実行や署名済みポリシー配布などランタイム内統制を第二段階として追加する。

## 設計のポイント

- ユーザーのラップトップやIDEを提示層に留め、実際のエージェント実行は会社管理のVM内に隔離する
- システムに変更を加える重要なアクションは必ず人間承認を経由させ、シークレットは資格情報プロキシ経由の短命トークンとして扱う
- エージェントの権限は署名済みポリシーバンドルで中央管理し、実行前に毎回ルールの有効性を継続検証する
- 全ログをOCSF形式で一元集約し監査可能な状態を保つ

## 使いどころ

- 全社員に常時稼働の自律エージェントアクセスを提供したいが統制も必要な大企業
- コード変更やチケット更新など実行結果が大きいアクションに人間レビューを組み込みたいエンジニアリング組織
