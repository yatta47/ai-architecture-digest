---
type: guidance
title: 仮想ファイルシステムでコーディングエージェントに安全なファイルアクセスを与える設計
title_original: Making Coding Agents Safe Using LlamaIndex
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- human-in-the-loop
components:
- LlamaParse
- LlamaIndex Agent Workflows
- Claude Agent SDK
- AgentFS
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/making-coding-agents-safe-using-llamaindex
published_at: '2026-07-19'
---

## 概要

コーディングエージェントに実ファイルシステムへの直接アクセスを許すと誤削除などのリスクがあるため、Turso製のSQLiteベース仮想ファイルシステムAgentFS上で全操作を行わせる設計を紹介している。読み書き編集をMCPサーバーの独自ツールに限定し、標準のRead/Write/Edit/GlobツールはPreToolUseフックで拒否することでガードレールを二重化している。

## 設計のポイント

- 実ファイルシステムではなくAgentFSの仮想コピー上で全操作を実行し、破壊的な操作からユーザーの実ファイルを保護する
- read_file/write_file/edit_file等をMCPサーバーのカスタムツールとして定義し、標準の組み込みファイルシステムツールを置き換える
- PreToolUseフックで標準ファイルシステムツール呼び出しを拒否し、ハルシネーションや指示逸脱によるガードレール回避を防ぐ
- PostToolUseフックで変更を実ファイルシステムに反映するかをユーザーに確認するhuman-in-the-loopを組み込む

## 使いどころ

- バックグラウンドで自律的に動くコーディングエージェントを、常時の人間監視なしで安全に運用したい場合
- 誤ったファイル削除・編集のリスクを抑えつつエージェントの自律性を保ちたい開発チーム
