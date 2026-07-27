---
type: case
title: 'Copilotベースの「FPLコンパニオン」: 公式データで意思決定を支援する会話型AI'
title_original: Fantasy Premier League Companion gives managers a new tool for success
company: Premier League
industry: media
cloud:
- azure
patterns:
- rag
- data-federation
- ai-agent
components:
- Microsoft Foundry
- Azure OpenAI
- ChatGPT 5.4
- Copilot
outcome:
  type: productivity
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/source/emea/features/fantasy-premier-league-companion-gives-managers-a-new-tool-for-success/
published_at: '2026-07-27'
---

## 概要

プレミアリーグは、Microsoft FoundryとAzure OpenAI（ChatGPT 5.4）を用いた会話型AI「Fantasy Premier League Companion powered by Copilot」を2026-27シーズンに向けて投入する。試合データとFPL独自のゲームデータという2つのデータセットを統合し、移籍推奨や選手比較などの質問に自然言語で回答しつつ、最終的な意思決定は常にマネージャー自身に委ねる設計とした。回答は最新のニュースを反映してリアルタイムに更新される。

## 設計のポイント

- 『自動操縦にはしない』という方針を明確にし、常に複数の選択肢と根拠データを提示して最終判断はユーザーに委ねる
- 試合データ（得点・出場時間など）とFPL固有のゲームデータ（移籍数・キャプテン選出率など）という異なる2つのデータソースを統合して推奨を生成する
- 初心者向けの基本的な質問から上級者向けの高度な統計質問まで、同じ会話型インターフェースで段階的に応答レベルを合わせる
- ニュースや試合結果の変化をリアルタイムに反映し、同じ質問でも時点によって異なる回答を返せるようにする

## 使いどころ

- 深いドメイン知識がなくても複雑な統計データにアクセスしたいファンタジースポーツの新規ユーザー
- 特定の指標（シュート数など）に基づいて選手比較をしたい上級マネージャー
- 大量の公式データを持つが、その活用方法をユーザーに分かりやすく届けたいスポーツリーグ・メディア企業
