---
type: announcement
title: エージェント型AI「Copilot Cowork」が一般提供、コスト管理機能を強化
title_original: Copilot Cowork is now generally available
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- multi-model-routing
- cost-optimization
components:
- Copilot Cowork
- Microsoft 365 Copilot
- Anthropic Opus 4.8
- Anthropic Sonnet 4.6
outcome:
  type: cost
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/
published_at: '2026-07-16'
---

## 概要

長時間・マルチツールの複雑なタスクを最後まで自律実行するCopilot Coworkが世界一般提供となった。クラウドホスト実行とマルチモデル設計により、比較テストではClaude Coworkより30〜40%低コストとされ、テナント／グループ／ユーザー単位の支出上限やアラート、利用状況レポートなど、利用量課金を前提としたコスト管理機能を新設した。

## 設計のポイント

- 1つのモデルに固定せず、タスクの複雑さに応じてモデルを切り替えるマルチモデル設計で、能力とコストのバランスを最適化する。
- タスクをlight/medium/heavyに分類し、4種類の利用者ペルソナごとの利用パターンを掛け合わせてコストを見積もるモデルを提供し、変動課金の予算計画を可能にする。
- 既定でオフにしておき、管理者がテナント単位で有効化とアクセス範囲、支出上限を決定できるようにすることでガバナンスを担保する。
- ファイルをローカル保存せずクラウド側で実行し続けることで、端末の電源状態に依存しない長時間タスクの継続性とセキュリティを両立する。

## 使いどころ

- 数週間かかっていたファイル横断比較やパイプライン精査などを自動化したいエンタープライズチーム。
- 利用量課金モデルでAIコストを可視化・統制したいIT管理部門。
- 複数の基盤モデルを状況に応じて使い分けたいが、モデル管理の複雑さを避けたい組織。
