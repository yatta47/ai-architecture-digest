---
type: announcement
title: セッション横断メモリとローカルモデル対応(GitHub Copilot for JetBrains)
title_original: Copilot memory and Ollama in GitHub Copilot for JetBrains
company: GitHub
industry: cross-industry
cloud:
- on-prem
patterns:
- memory-consolidation
- ai-agent
- multi-model-routing
components:
- GitHub Copilot
- GitHub Copilot for JetBrains
- Ollama
- MCP
- Codex
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-11-copilot-memory-and-ollama-in-github-copilot-for-jetbrains
published_at: '2026-08-11'
---

## 概要

GitHub Copilot for JetBrainsに、チャットセッションをまたいで情報を保持するCopilotメモリ、ローカルモデルをBYOKプロバイダとして使えるOllama連携、MCPサーバーアクセスや権限バイパスを一元管理するエンタープライズ管理設定が追加された。あわせてMCP実行・ターミナル・カスタマイズ・クラウドエージェントの信頼性も改善された。

## 設計のポイント

- Copilotメモリをチャットセッションをまたいで保持・想起できるようにし、毎回同じプロジェクト情報や好みを伝え直す必要をなくした。
- OllamaをBYOKプロバイダとして追加し、ローカル/自前ホストのモデルをIDE内のモデル選択にそのまま統合できるようにした。
- MCPサーバーアクセスや権限バイパスの挙動をエンタープライズ管理設定として集中管理できるようにし、組織単位のガバナンスを強化した。

## 使いどころ

- 開発チーム内でプロジェクトの前提や好みを毎回説明せずにエージェントに引き継ぎたいエンジニア。
- 自社ホストのモデル(Ollama等)をIDEのCopilot体験にそのまま組み込みたいセキュリティ重視の組織。
- 複数チームでMCPサーバーや権限設定を一元管理したいエンタープライズ管理者。
