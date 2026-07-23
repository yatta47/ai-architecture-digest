---
type: guidance
title: CLAUDE.mdでAIコーディングエージェントにプロジェクト文脈を持たせる設計ガイド
title_original: 'Using CLAUDE.md files: Customizing Claude Code for your codebase'
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
components:
- Claude Code
- MCP
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/using-claude-md-files
published_at: '2025-11-25'
---

## 概要

CLAUDE.mdはリポジトリのルートや親ディレクトリ、ホームディレクトリに配置できる設定ファイルで、Claude Codeにプロジェクトのアーキテクチャ・規約・ワークフローを永続的な文脈として与える。/initコマンドで初期版を自動生成し、以降はチームの実運用に基づいて反復的に洗練していくことが推奨される。ディレクトリ構造の見取り図やカスタムツール・MCPサーバーの使い方を記載することで、毎回同じ説明を繰り返さずにClaudeが適切な判断を下せるようになる。

## 設計のポイント

- CLAUDE.mdをリポジトリルート（チーム共有）・親ディレクトリ（モノレポ）・ホームディレクトリ（全プロジェクト共通）に階層的に配置し、適用範囲を使い分ける
- 主要ディレクトリ構成や依存関係、アーキテクチャパターンを簡潔なツリーで示し、Claudeにコードベースの見取り図を与える
- カスタムツールやMCPサーバーの使い方をコマンド例付きで明記し、Claudeが正しい社内ツールを呼び出せるようにする
- /initで生成した初期版はたたき台と位置づけ、チームの実際の運用に基づいてレビュー・改善したうえでバージョン管理にコミットし共有する

## 使いどころ

- 肥大化したコードベースで毎回同じアーキテクチャ説明や規約説明を繰り返したくない開発チーム
- モノレポや複数プロジェクトでコーディング規約・テスト方針をAIエージェントに一貫して守らせたいチーム
- Slack連携などのMCPサーバーや社内カスタムスクリプトをAIエージェント経由で活用したいチーム
