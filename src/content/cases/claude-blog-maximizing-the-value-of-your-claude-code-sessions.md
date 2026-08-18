---
type: guidance
title: Claude Codeセッションのトークンコストを最適化する運用術
title_original: Maximizing the value of your Claude Code sessions
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
- context-engineering
components:
- Claude Code
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions
published_at: '2026-08-14'
---

## 概要

Claude Codeのセッションはモデル・入出力トークン・プロンプトキャッシュの有無によってコストが変わるため、同じタスクでもトークンの使い方次第で費用が大きく異なる。タスクごとに/clearでコンテキストをリセットし、モデルやeffortレベルをセッション開始前に固定し、ファイルは@メンションで直接添付するなどの運用でキャッシュヒット率を高め、無駄なトークン消費を抑える。

## 設計のポイント

- タスクの切れ目で/clearを実行し、不要な過去コンテキストがモデルに再送されるのを防ぐ
- モデルとeffortレベルはセッション開始前に固定し、途中変更によるプロンプトキャッシュの破棄を避ける
- ファイルをパスで指示するのではなく@メンションで直接添付し、Read呼び出しや検索のトークンを節約する
- ノイズの多いコマンド出力はquietフラグやサブエージェント実行で会話に残さないようにする

## 使いどころ

- Claude Codeを日常的に使う開発者がトークンコストを意識してセッションを設計したい場合
- 長時間の対話でプロンプトキャッシュを維持し、再計算コストを避けたいチーム
- /contextや/compactを使って読み込み内容を可視化し、不要な情報を削ぎ落としたい場合
