---
type: guidance
title: モデルの進化に合わせて薄くするエージェントハーネス設計の3パターン
title_original: 'Agent Harness Design: 3 Patterns for Harnessing Claude''s Intelligence'
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- memory-consolidation
- multi-agent-orchestration
components:
- Claude Code
- Agent Skills
- Bash tool
- Text editor tool
- Memory tool
- Context editing
- Subagents
- Programmatic tool calling
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/harnessing-claudes-intelligence
published_at: '2026-04-02'
---

## 概要

エージェントハーネス（モデル周辺のツール・ループ・ガードレール）はモデルがまだできないことを前提に設計されるが、Claudeが賢くなるにつれその前提は古くなる。記事はbash/text editorのような汎用ツールを使う、ツール結果の取捨選択・スキルの段階的開示・記憶の管理をハーネス側ではなくClaude自身に任せるという3つの設計パターンを、SWE-benchやBrowseCompでの実測改善とともに提示する。

## 設計のポイント

- 独自ツールを作り込むより、bashとtext editorのようなClaudeが既によく理解している汎用ツールを土台にする（Agent Skills・programmatic tool calling・memory toolもこの2つの組み合わせから生まれている）
- コード実行ツールを与え、どのツール結果をコンテキストに流すか・フィルタするか・次の呼び出しにパイプするかをハーネスではなくClaude自身に判断させる（BrowseCompで45.3%→61.6%に向上）
- 全指示を事前にシステムプロンプトへ詰め込まず、スキルのYAMLフロントマターだけを常時ロードし本文はClaudeが必要な時にファイル読み込みで段階的に開示する
- compactionやmemoryフォルダを与え、何を要約し何を永続化するかをClaude自身に選ばせることで、外付けの検索基盤に頼らない長時間タスクの継続性を実現する（BrowseCompでOpus 4.6が同じcompaction設定で84%に到達）

## 使いどころ

- モデルのバージョンアップごとにハーネスを作り直したくない、Claudeの能力向上に自動的に追随できるエージェント基盤を作りたいチーム
- エージェント検索・コーディングエージェント・ゲームプレイなど、単一コンテキストウィンドウを超える長時間稼働エージェントの記憶管理を設計するチーム
- 巨大なテーブルやWebページの読み込みなど、ツール結果をそのままコンテキストに流すとコストやレイテンシが悪化するケースを最適化したいチーム
