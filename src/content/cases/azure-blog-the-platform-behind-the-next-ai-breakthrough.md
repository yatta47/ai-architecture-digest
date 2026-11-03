---
type: opinion
title: エージェント時代のクラウド基盤：長時間動作ワークロードに必要なインフラ
title_original: The platform behind the next AI breakthrough
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
components:
- Microsoft Azure
outcome:
  type: productivity
source_id: azure-blog
source_name: Azure Blog
source_url: https://www.wired.com/sponsored/story/the-platform-behind-the-next-ai-breakthrough/
published_at: '2026-11-02'
---

## 概要

Microsoft提供の広告記事で、エージェントを数時間〜数日続く動的で予測しづらいワークロードと位置づけ、シリコン・計算・ストレージ・ネットワークを統合した基盤が必要だと論じる。具体的な実装詳細は乏しい。

## 設計のポイント

- エージェントは推論・検索・ツール実行・コード実行を行き来し進捗を保持する長時間処理として設計する
- モデルとインフラの両面の進化が持続的な業務遂行に要る

## 使いどころ

- エージェント基盤の要件を整理したい企画担当
- 長時間処理向けのクラウド選定の論点把握
