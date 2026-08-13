---
type: guidance
title: Teamsのグループチャットでエージェントが空気を読むためのUXパターン
title_original: 'Building agents for Teams: Managing the noise of collaboration'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- Microsoft Teams SDK
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://devblogs.microsoft.com/microsoft365dev/building-agents-for-teams-managing-the-noise-of-collaboration/
published_at: '2026-08-13'
---

## 概要

Teamsのグループチャットにおいて、エージェントが会話のノイズを増やさずに参加するための3つのインタラクションパターン（絵文字リアクション、スレッド返信、引用返信）を解説。人間同士の暗黙の社会的合図をエージェントにも実装することで、常に発言せずとも価値を提供できるようにする。

## 設計のポイント

- 作業中/完了を絵文字リアクションの差し替えで示し、チャットに新規メッセージを増やさずに状態を伝える
- チャンネルでの議論はスレッド内で返信し、本流の会話を汚さないようにする
- 数時間後に完了する非同期タスクは、元メッセージへの引用返信で文脈を結び付ける

## 使いどころ

- Teamsなどのグループチャットに常駐するボット/エージェントを設計する開発者
- 多人数が同時に会話する場でエージェントの発言が会話のノイズにならないようにしたいプロダクトチーム
