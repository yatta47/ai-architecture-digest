---
type: case
title: 構造化された自己モデルで文脈を保持するChief of Staffエージェント
title_original: Building a Memory-Driven Agent with NVIDIA NemoClaw
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- memory-consolidation
- context-engineering
- human-in-the-loop
components:
- NVIDIA NemoClaw
- NVIDIA OpenShell
- NVIDIA Nemotron
- SQLite
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/
published_at: '2026-09-04'
---

## 概要

NVIDIA NemoClawで構築した記憶駆動型のChief of Staffエージェントは、人・案件・優先度・作業パターンをMarkdownの「自己モデル」として保持し、義務や修正履歴はSQLite台帳に分離して記録する。Agent Memory Benchmarkでは、エージェント型RAGベースラインに対し全体精度が82.8%から90.9%に、時間経過で変化した事実の追跡が60.0%から100%に向上した。

## 設計のポイント

- 派生知識（自己モデル）と根拠（元のメッセージ）を分離し、誤りが証拠・記憶更新・検索・推論のどこで起きたか切り分けられるようにする
- 知識（人・案件・優先度）と判断（優先順位・無視されたか）を別レイヤーに保存し、判断を元メッセージに書き込まない
- ユーザーが明示した優先度を短期的な緊急性より優先するインテントゲートを設け、階層サイズや順位付けはコードで決定的に強制する
- ユーザーの修正を追記専用の監査ログに記録し、繰り返しパターンから可読・編集可能な選好ポリシーを更新する

## 使いどころ

- メッセージ・決定・案件が日々変化する中で文脈を保持し続けたいエンタープライズ向けエージェント
- エージェントの判断根拠を人が検証・修正でき、誤った記憶が固定化しないようにしたい場合
- ファイル・プロセス・ネットワークアクセスをサンドボックス化しつつ認証情報を分離したいエージェント基盤
