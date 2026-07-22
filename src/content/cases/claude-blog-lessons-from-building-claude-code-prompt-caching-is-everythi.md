---
type: guidance
title: Claude Codeのハーネス設計から学ぶ:プロンプトキャッシュを崩さない実装パターン
title_original: 'Lessons from building Claude Code: Prompt caching is everything'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- context-engineering
- prompt-optimization
- inference-optimization
components:
- Claude Code
- Claude Opus
- Claude Haiku
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything
published_at: '2026-04-30'
---

## 概要

Claude Codeのエンジニアリングチームが、プロンプトキャッシュのヒット率を最大化するために積み重ねてきた設計原則を共有する記事。静的な内容を先頭・動的な会話内容を末尾に固定して共有プレフィックスを最大化し、プロンプト本文の書き換えではなく次メッセージでの追記で情報を更新し、Plan Modeやtool searchのdefer_loadingのようにツール定義自体は変えずに機能を切り替える、といった具体策を解説している。

## 設計のポイント

- 静的なシステムプロンプト・ツール定義を先頭、動的な会話内容を末尾に配置しキャッシュの共有プレフィックスを最大化する
- 情報更新はプロンプト本体の書き換えではなく次のメッセージへの追記(system-reminder等)で行い、キャッシュミスを避ける
- セッション途中でモデルやツールセットを変更せず、モデル切り替えが必要な場合はサブエージェントに委譲する
- モード切り替え(Plan Mode等)はツール集合を変えずEnterPlanMode/ExitPlanModeのようなツール自体で表現し、キャッシュを維持する

## 使いどころ

- 長時間稼働するエージェント型プロダクトでレイテンシとコストを削減したいエンジニアリングチーム
- 会話が長く続くLLMアプリでキャッシュヒット率を維持するハーネス設計を検討している場合
