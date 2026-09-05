---
type: announcement
title: 長時間の自律コーディングタスク向けモデルGPT-6 AstraがGitHub Copilotで一般提供
title_original: GPT-6 Astra is generally available in GitHub Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-model-routing
components:
- GitHub Copilot
- GPT-6 Astra
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-04-gpt-6-astra-is-generally-available-in-github-copilot
published_at: '2026-09-04'
---

## 概要

OpenAIの新モデルGPT-6 AstraがGitHub Copilotで一般提供された。長時間にわたる自律的なコーディング・エージェントタスク向けに設計されており、途中でプランニングと検証を繰り返し、診断とベリファイをまとめて行い、完了を宣言する前に自ら結果を確認する点が特徴で、従来モデルより少ないステップ数で長期タスクの性能を上げている。

## 設計のポイント

- タスク完了を宣言する前に自らの成果を検証するセルフチェックのループをモデルの挙動に組み込む
- 診断とベリファイをバッチ処理することで、長時間タスクを少ないステップ数で完了させる

## 使いどころ

- 長時間・複数ステップにまたがる自律的なコーディング/エージェントタスクを任せたい開発者
- VS Code・CLI・IDEなど複数クライアントで同じ自律型モデルを使い分けたいエンタープライズ
