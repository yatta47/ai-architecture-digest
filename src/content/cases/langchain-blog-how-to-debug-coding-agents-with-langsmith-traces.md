---
type: guidance
title: 複数のコーディングエージェントをLangSmithで統一トレース化しデバッグする方法
title_original: Your coding agents are a black box. Here's how to crack them open.
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- eval
- multi-agent-orchestration
components:
- LangSmith
- Claude Code
- Codex
- Cursor
- GitHub Copilot Chat
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/your-coding-agents-are-a-black-box-heres-how-to-crack-them-open
published_at: '2026-07-15'
---

## 概要

Claude Code・Codex・Cursorなど複数のコーディングエージェントはそれぞれ異なる形式でログを記録するため、失敗調査のたびにツールを行き来する必要があった。LangSmithは全エージェントのセッションを共通トレーススキーマにマッピングし、サブエージェントの引き継ぎやツール呼び出しを横断的に可視化・比較できるようにする。

## 設計のポイント

- 各エージェント固有のログ形式を共通のトレーススキーマにマッピングし、thread_idで一連のセッションを時系列に再構成できるようにする。
- 失敗トレースを最終diffの確認だけで終わらせず、評価データセットとして再利用し将来の回帰を検知する。
- レイテンシ・コスト・トークン使用量でフィルタし、コストガバナンスの起点として使う。

## 使いどころ

- 複数のコーディングエージェントを併用し障害調査のたびに異なるログ形式に悩まされているチーム。
- エージェントのフリート全体でどのワークフローが失敗しやすいか継続的に把握したい組織。
