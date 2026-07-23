---
type: announcement
title: Claudeアプリ内でAI搭載アプリを構築・ホスト・共有できるArtifacts機能
title_original: Build and share AI-powered apps with Claude
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Claude
- Artifacts
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-powered-artifacts
published_at: '2025-07-25'
---

## 概要

Claude経由でAPIと対話するArtifactsを作成できるようになり、開発者はスケーリングのコストや複雑さを気にせずAI搭載アプリを構築・ホスト・共有できるようになった。利用者は自分のClaudeアカウントで認証し、APIキー管理も課金負担も開発者側に発生しない。

## 設計のポイント

- 利用者が自身のClaudeアカウントで認証し利用量が利用者自身のサブスクリプションに計上されるようにすることで、共有時の従量課金負担を開発者からなくす
- Claudeが実際に動くコードを生成しアプリを構成するため、開発者はコードを閲覧・改変・自由に共有できる

## 使いどころ

- APIキー管理や課金を気にせずAI搭載アプリを不特定多数に共有したい個人開発者
- スキルレベルに応じて内容を調整する学習ツールや、対話するNPCを持つゲームを作りたいクリエイター
