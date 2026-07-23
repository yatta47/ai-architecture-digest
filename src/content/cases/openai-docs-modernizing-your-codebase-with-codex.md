---
type: guidance
title: Codex CLIでレガシーCOBOLシステムを段階的に近代化する手法
title_original: Modernizing your Codebase with Codex
industry: financial-services
cloud: []
patterns:
- ai-agent
- spec-driven-development
- human-in-the-loop
components:
- Codex CLI
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/codex/code_modernization/
published_at: '2025-11-19'
---

## 概要

OpenAIのCookbookが、COBOLベースの投資ポートフォリオシステムを例に、Codex CLIを使ってレガシーコードベースを近代化する手順を紹介している。AGENTS.mdやPLANS.mdで計画のルールを定め、1つのパイロットフローに絞って調査・設計・検証を進める「ExecPlan」中心のワークフローを提案している。エンジニアはアーキテクチャや業務ルールの判断に集中し、Codexが翻訳・リファクタ・ドキュメント/テストの同期といった作業を担う。

## 設計のポイント

- ExecPlan（pilot_execplan.md等）を『ホームベース』として、スコープ・進捗・意思決定ログを一元管理する
- AGENTS.md/PLANS.mdでリポジトリ固有のエージェント運用ルールと計画の型を事前に定義する
- 近代化対象を1つの現実的かつ範囲限定のパイロットフローに絞り込み、リスクを抑えて検証する
- レガシー版とモダン版を並行実行してアウトプットを比較するパリティ検証を設計プロセスに組み込む

## 使いどころ

- COBOL/JCLなどのレガシー資産を段階的にモダナイズしたい開発チーム
- 改修の監査可能性・再現性を重視するアーキテクトやリスク管理担当者
- AIエージェントに任せる作業範囲と人間がレビューすべき範囲を明確に切り分けたいチーム
