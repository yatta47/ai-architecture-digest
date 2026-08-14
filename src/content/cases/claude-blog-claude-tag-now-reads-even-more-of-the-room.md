---
type: announcement
title: Claude TagがSlackチャンネル全体の文脈を見て自発的に発言するか判断
title_original: Claude Tag now reads even more of the room
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- memory-consolidation
components:
- Claude Tag
- Slack
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room
published_at: '2026-08-13'
---

## 概要

Slackに常駐するClaude Tagが、従来はメッセージ単体を分類器で判定して発言可否を決めていたのに対し、チャンネル全体の文脈・メモリ・常設指示を踏まえて「返信する/スレッドで着手する/既存の作業に紐付ける/沈黙する」の4択で判断するようになった。個別には無関係に見える2人の発言を組み合わせて着手すべき作業を見つけ出せるようになり、自発的な応答判定の精度が約30%向上したという。

## 設計のポイント

- 1メッセージ単体を判定する分類器を廃止し、チャンネル全体の会話履歴とメモリを踏まえて発言要否を判断する設計に変更した
- 『有用性・確信度・他に適任者がいるか』を軸にしたルーブリックで発言可否を採点し、不要な割り込みを避ける
- チャンネルごとに反応の閾値を学習し、価値を提供できないチャンネルでは自然と反応頻度を下げる(@メンションで即座に復帰)
- 自然言語の常設指示(『デプロイパイプラインの話題には積極的に参加して』等)でチャンネルごとの振る舞いを調整可能にする

## 使いどころ

- Slackで常時複数チャンネルに常駐させ、必要な時だけ発言してほしいAIアシスタント運用
- メンションなしでも関連する会話をつなぎ合わせて能動的に着手してほしいチーム
- 過剰な割り込みを避けつつ有用な場面では素早く反応してほしい社内コラボレーション用途
