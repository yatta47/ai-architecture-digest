---
type: guidance
title: AIエージェントが操作できるインタラクティブなデータ可視化言語「Flint-interactive」
title_original: 'Flint-interactive: a language for creating interactive data visualizations'
company: Microsoft
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Flint-interactive
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://www.microsoft.com/en-us/research/blog/flint-interactive-a-language-for-creating-interactive-data-visualizations/
published_at: '2026-10-22'
---

## 概要

エージェントが生成するチャートを静的なものに留めず、クリック、絞り込み、ズーム、チャート間連携で探索できるようにするFlint-interactiveを紹介する。低レベルのコードでなく高レベルのセマンティックイベントと更新オペレーターで記述し、コンパイラが依存関係を処理する。

## 設計のポイント

- エージェントには低レベルの描画コードでなく高レベルのイベントと更新オペレーターを書かせ、生成コストと失敗を減らす。
- コンパイラが相互作用ロジックとビジュアルの依存関係を扱い、信頼性を確保する。
- チャート、文章、表、アプリ状態を連動させる。

## 使いどころ

- チャット内でデータ探索できるエージェントを作る開発者。
- インタラクティブなデータストーリーやダッシュボードの自動生成。
