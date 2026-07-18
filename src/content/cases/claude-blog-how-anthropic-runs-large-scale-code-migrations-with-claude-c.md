---
type: guidance
title: AIエージェントで大規模コードマイグレーションを回す6ステップの進め方
title_original: How Anthropic runs large-scale code migrations with Claude Code
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- parallel-execution
- eval
- ci-cd
components:
- Claude Code
- Claude Fable 5
- Claude Opus 4.8
data_sources:
- ソースコード
- テストスイート
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/ai-code-migration
published_at: '2026-07-16'
---

## 概要

Anthropicが大規模なコードマイグレーション（別言語への移植）をClaude Codeで実行する手法を、2つの実例をもとに解説した手引き。BunのZig→Rust移植（2週間弱で100万行、既存テスト100%通過）と、PythonからTypeScript 16.5万行への週末での移植を題材に、従来は数年・数百万ドル規模だったプロジェクトが数週間で回せるようになった要因と6ステップのプロセスを示す。

## 設計のポイント

核心は「コードを直すのではなく、コードを生み出すプロセス（ループ）を直す」こと。まず元コードと移植先を同一基準で評価できる『強い判定器（judge）』を用意して終了条件を定義し、外部呼び出しで表現できるテストを両者で走る形に書き換えたうえで敵対的エージェントで検証する。作業をファイルやクレート単位に並列分解し、テストスイートを客観的なリファリーとして使い、コンパイル/テストの失敗をそのまま次のキュー項目に、エッジケースへの対処を後続エージェントが従うルールに変えることで、ドリフトの逃げ場をなくす。

## 使いどころ

言語の乗り換えが望ましいと分かっていても、並行保守やパリティ未達のリスクで長年先送りされてきた移植プロジェクトに効く。テストスイートという客観的な検証基盤を持つ大規模コードベースを、より小さく・速く・安全な言語へ移したいチームに向く。
