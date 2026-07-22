---
type: announcement
title: Claude APIスキルがCodeRabbit・JetBrains・Resolve AI・Warpにバンドル
title_original: Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp
industry: cross-industry
cloud: []
patterns:
- prompt-optimization
- inference-optimization
- llmops
components:
- Claude API
- Claude Code
- CodeRabbit
- JetBrains
- Resolve AI
- Warp
- Claude Opus 4.7
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-api-skill
published_at: '2026-04-29'
---

## 概要

Claude Codeで最初に導入された「claude-api skill」が、CodeRabbit・JetBrains・Resolve AI・Warpにバンドルされ、どの開発ツールを使っていてもプロダクションレベルのClaude API実装知識を得られるようになった。エージェントパターンの選び方やモデル世代間のパラメータ変更、プロンプトキャッシュの適用箇所などをスキルが把握しており、モデル移行やキャッシュヒット率改善を対話的にガイドする。

## 設計のポイント

- エージェントパターンの選定・パラメータ変更・キャッシュ適用箇所などのAPI知識をスキルとしてパッケージ化し、複数の開発ツールへ横展開する
- SDKやモデルの変更に追従して知識が自動更新される設計にし、開発者が個別に移行ガイドを追わなくて済むようにする

## 使いどころ

- 複数のIDEやツールを横断してClaude API実装のベストプラクティスを浸透させたいプラットフォーム提供者
- 新しいモデル世代へのマイグレーションを素早く安全に行いたい開発チーム
