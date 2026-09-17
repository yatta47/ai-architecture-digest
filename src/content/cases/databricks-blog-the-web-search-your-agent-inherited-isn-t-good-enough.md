---
type: case
title: 複数ハーネスに散らばるエージェント実装をOmnigentで一本化しNimbleでWeb検索を強化
title_original: The web search your agent inherited isn't good enough
industry: cross-industry
cloud: []
patterns:
- unified-runtime
- llm-gateway
- ai-agent
- cost-optimization
components:
- Omnigent
- Nimble Search API
- Databricks Foundation Model APIs
- Unity Catalog
- Delta Lake
- Claude Code
- Codex
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/web-search-your-agent-inherited-isnt-good-enough
published_at: '2026-09-17'
---

## 概要

あるエンジニアはアカウント動向を監視するエージェントをClaude Code・Codex・素のAPI呼び出しの3系統で別々に作り込んでいたが、ハーネスごとにツール宣言やWeb検索結果が食い違い、コストやガバナンスを横断的に把握できなかった。Databricksが提供する抽象化レイヤー「Omnigent」でエージェント定義を一本化し、モデル呼び出しをFoundation Model APIsに集約、Web検索スロットにNimbleを差し込むことで、ベンチマーク精度を46%から71%に向上させつつ検索コストを半減させた。

## 設計のポイント

- モデル・ツール・ポリシーをハーネス非依存の単一定義として持ち、複数の実行環境（Claude Code、Codex、API）に同じ定義を展開する
- モデル呼び出しをFoundation Model APIs経由に統一し、コスト計測・監査・ガバナンスを一元化する
- 各ハーネス標準搭載のWeb検索をそのまま使わず、用途特化のWeb検索プロバイダをスロットとして差し替え可能にする
- 検索エージェントが有効な情報源と取得経路を学習・再利用することでトークンコストを継続的に下げる

## 使いどころ

- 同じエージェントロジックを複数のコーディングハーネスで重複開発してしまっているチーム
- Web検索結果の粒度や網羅性がハーネスによってばらつき、営業シグナル収集などの精度が安定しないケース
- エージェントのコスト・監査ログをハーネス横断で一元管理したい組織
- JavaScriptレンダリングやページネーションの裏に隠れた情報まで継続的に収集したいドメイン特化のリサーチ用途
