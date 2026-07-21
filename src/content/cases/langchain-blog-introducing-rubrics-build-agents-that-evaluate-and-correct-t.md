---
type: announcement
title: Deep Agentsにルーブリック評価ループを追加するRubricMiddleware
title_original: 'Introducing Rubrics: Build Agents that Evaluate and Correct Their Work'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- multi-agent-orchestration
components:
- Deep Agents
- RubricMiddleware
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-rubrics-for-deepagents
published_at: '2026-06-25'
---

## 概要

LangChainはDeep Agentsに、実行完了前にグレーダー用のサブエージェントがルーブリック（成功基準のチェックリスト）に照らして出力を評価するRubricMiddlewareを追加した。基準を満たさない場合は各基準ごとの具体的なフィードバックが会話に差し戻され、満点になるか最大反復回数に達するまでエージェントが再試行を繰り返す。テスト合格や禁止パターン回避など、検証可能な成功基準を持つタスクに特に有効という。

## 設計のポイント

- 評価を担当するグレーダーは本体のエージェントとは別のサブエージェントとして分離し、ツール呼び出しや全体のトランスクリプト参照を通じて根拠に基づく判定を行わせる。
- グレーダーにはテスト実行やlintなど検証用のツールを渡すことで、抽象的な妥当性判断ではなく実行結果に基づく客観的な合否判定を可能にする。
- ルーブリックはエージェントのsystem_promptとは切り離し、invoke時に渡す独立した引数とすることで、『やり方』の指示と『できたかどうかの基準』を明確に分離する。
- max_iterationsで再評価ループの上限を設定し、満たされない場合でも無限ループにならないよう終了条件（成功・上限到達・失敗・グレーダーエラー）を明示する。

## 使いどころ

- テスト合格やコーディング規約遵守など、成功条件を明文化しやすいコード生成・リファクタリングタスクを任せる開発者に有効。
- レポート作成など『必要な章がすべて揃っているか』のようなチェックリスト型の成功基準がある文書生成タスクにも適用できる。
- 出力品質のばらつきを人手で毎回チェック・再実行する運用から、システム側で自動的に検知・修正するループへ移行したいチームに向く。
