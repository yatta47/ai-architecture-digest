---
type: announcement
title: LangSmithのリグレッションテスト刷新、ベースライン比較とComparison View
title_original: Regression Testing with LangSmith
industry: cross-industry
cloud: []
patterns:
- eval
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/regression-testing
published_at: '2026-06-15'
---

## 概要

LangSmithのリグレッションテスト機能を刷新。複数の実験を横並びで比較するComparison Viewと、ベースラインに対する指標の増減を自動ハイライトする仕組みにより、AI特有の『常に100%正解するとは限らない』テスト結果から興味深いデータポイントに素早くドリルダウンできるようにした。

## 設計のポイント

- ベースラインの実行を設定し、指標が改善・悪化したデータポイントを自動でハイライトする
- 複数の実験結果を横並びで比較できるComparison Viewを用意し、差分のあるデータポイントだけに素早くドリルダウンできるようにする

## 使いどころ

- プロンプトやモデル変更のリグレッションを継続的に追跡したいチーム
- AI特有の『必ずしも100%正解しない』テスト結果を過去の実行と比較しながら改善したい場合
