---
type: announcement
title: VS Code CopilotのAgentsウィンドウが刷新、マルチハーネス・サブエージェント管理を強化
title_original: GitHub Copilot in Visual Studio Code — July 2026 releases
company: GitHub
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- multi-agent-orchestration
components:
- GitHub Copilot
- Visual Studio Code
- Claude
- Codex
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-30-github-copilot-in-visual-studio-code-july-2026-releases
published_at: '2026-07-30'
---

## 概要

VS Code 1.127〜1.131(2026年7月)のリリースで、Copilotの「Agentsウィンドウ」が刷新。Gitワークツリーを使った複数ハーネス(Copilot/Claude/Codex)セッションの分離実行、サブエージェントの状態追跡、1セッション内での複数チャット分岐など、エージェント運用機能が大幅強化された。

## 設計のポイント

- 各エージェントセッションをGitワークツリーで分離し、並行実行時のファイル競合を防ぐ
- 1つのセッション内に複数の関連チャットを持たせ、フォークして別アプローチを試しつつ元の文脈を保持できるようにする
- サブエージェントごとにモデル・経過時間・実行中のツール呼び出しを可視化し、親の会話を失わずに個別確認できるようにする
- BYOKモデルをAgentsウィンドウでも使えるようにし、エディタとエージェント実行の両方でモデル選択の一貫性を保つ

## 使いどころ

- 複数のAIコーディングエージェント(Copilot/Claude/Codex)を並行運用する開発チーム
- 大規模な変更を複数アプローチで試しながら比較検討したい開発者
- サブエージェントを使う複雑なタスクの進行状況を管理したいエンジニア
