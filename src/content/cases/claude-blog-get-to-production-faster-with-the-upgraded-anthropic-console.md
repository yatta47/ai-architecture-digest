---
type: announcement
title: Anthropic Consoleが刷新、プロンプト共同開発と評価フローを一元化
title_original: Get to production faster with the upgraded Anthropic Console
industry: cross-industry
cloud: []
patterns:
- llmops
- prompt-optimization
- eval
components:
- Anthropic Console
- Claude 3.7 Sonnet
- Workbench
outcome:
  type: speed
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/upgraded-anthropic-console
published_at: '2025-03-06'
---

## 概要

Anthropic Consoleが刷新され、プロンプトの作成・評価・改善とチーム間共有を1か所で行えるようになった。Claude 3.7 Sonnetの拡張思考（extended thinking）の予算制御にも対応し、プロンプトエンジニアリングから本番デプロイまでの時間短縮を狙う。

## 設計のポイント

- Workbenchで例示やツール統合を含むプロンプトを対話的に構築・テストできるようにする
- 自動テストケース生成と出力の並列比較により、データドリブンにプロンプトを評価・採用判断する
- 共有プロンプトライブラリを設けてコピペ運用によるバージョン管理の混乱やナレッジのサイロ化を防ぐ
- 拡張思考の最大トークン予算を設定可能にし、応答速度とコストのトレードオフを制御できるようにする

## 使いどころ

- 開発者・ドメイン専門家・PM・QAが同じプロンプトを共同編集し標準化したい組織
- 他モデル向けに書かれたプロンプトをClaude向けに最適化したい開発者
- 拡張思考のコスト・レイテンシと精度のバランスを調整したいチーム
