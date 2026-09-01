---
type: announcement
title: VS CodeのCopilotエージェント機能拡張（2026年8月版）
title_original: GitHub Copilot in VS Code, August 2026 releases
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
components:
- GitHub Copilot
- VS Code
- Agent Host
- Claude
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-31-github-copilot-in-vs-code-august-2026-releases
published_at: '2026-08-31'
---

## 概要

VS Code 1.132〜1.135のアップデートで、複数のエージェントセッションを並べて比較・追跡できるAgentsウィンドウの強化、Agent Plugins 1.0によるポータブルなエージェントカスタマイズのインストール、Claude/Copilotのモデルプロバイダ切り替えなどが追加された。長い会話内のテキスト検索やMarkdown差分レビュー、複数言語対応のディクテーションなど、チャット・レビュー体験も改善している。

## 設計のポイント

- 同一のAgent Hostセッションを複数のVS Codeウィンドウから接続できるようにし、エージェントの作業状態を共有する
- Agent Plugins 1.0という標準規格でエージェントのカスタマイズをVS Code外のクライアントとも相互運用可能にする
- モデルプロバイダ（Anthropicサブスクリプション/Copilotサブスクリプション）をセッション単位で切り替え可能にする

## 使いどころ

- 複数のエージェントセッションを並行して走らせ比較したい開発者
- エージェントの変更内容をレビューしながら長い会話を追いたいチーム
- 社内で複数のエージェントクライアント（VS Code外）にカスタマイズを持ち込みたい組織
