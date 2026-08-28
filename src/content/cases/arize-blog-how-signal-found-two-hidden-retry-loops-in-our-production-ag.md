---
type: case
title: Arize、自社のAIエンジニアリングエージェントAlyxに潜む2つの隠れたリトライループをSignalで発見
title_original: How Signal found two hidden retry loops in our production agent Alyx
company: Arize
industry: cross-industry
cloud: []
patterns:
- root-cause-analysis
- eval
components:
- Arize AX
- Arize Signal
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-signal-found-two-hidden-retry-loops-in-alyx/
published_at: '2026-08-27'
---

## 概要

Arizeは自社のAIエンジニアリングエージェントAlyxの本番トレースに、大量トレースをレビューして再発パターンをランク付きの調査に変換する管理エージェントSignalを適用した。ルートスパンがOKのまま227秒・192スパン・同一ツール43回呼び出しという『健全に見える』トレースの中に、状態遷移の重複更新やオプション空文字列の扱い誤りに起因する隠れたリトライループを発見し、いずれも小さな修正で解消した。

## 設計のポイント

- エラーではなく『振る舞い』としてバグを検知する仕組みを持つ。一件ずつのトレース確認ではスケールしないため、大量トレースを集約してランク付けする
- ルートスパンのステータスがOKでも、スパン数・実行時間・同一ツール呼び出し回数などの異常な振る舞いパターンを別軸で検知する
- 冪等でない状態遷移（重複更新）はエラーではなく成功のno-opとして扱い、モデルが誤った失敗シグナルを受け取らないようにする
- オプショナルなパラメータの空文字列は型付きツール境界でNoneに正規化し、意図しないバリデーション分岐に入らないようにする

## 使いどころ

- エラーとして表面化しない、リトライループのようなエージェントの異常挙動を検知したいAI運用チーム
- ツール呼び出しが『妥当に見える』が実際は無意味な繰り返しになっているケースを、トレース分析で発見したい場合
- 本番トレースの調査からコード修正PRまでの一連のワークフローを、担当者の手作業なしに近づけたい開発チーム
