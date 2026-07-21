---
type: guidance
title: LLMの評価(eval)をpytest/Vitestの単体テストとしてCIに組み込む
title_original: 'Evals in CI: How to write your LLM evals as tests with Arize Phoenix'
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- ci-cd
components:
- Arize Phoenix
- pytest
- Vitest
- Jest
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/evals-in-ci-how-to-write-llm-evals-as-tests/
published_at: '2026-07-07'
---

## 概要

LLM/エージェントの評価(eval)を通常のソフトウェアテストと同じpytest/Vitest/Jestのワークフローで書けるようにするArize Phoenixの手法を解説。ハード不変条件はアサーションでCIをブロックし、LLM-as-judgeなどのスペクトラム評価はスコアとして記録・トレンド監視するという、2種類のチェックの使い分けを提案する。

## 設計のポイント

- 『唯一の正解がある不変条件』はアサーションとしてCIをブロックし、『スペクトラム上の品質』はスコアとして記録しトレンドで監視するという2種類のチェックを明確に分ける
- 各テストスイートを1つのデータセットに、各テストケースを1つのサンプルに、各実行を1つの実験にマッピングし、既存のテストフレームワークの資産(fixture・parametrize・watchモード)をそのまま流用できるようにする
- 全実行でLLMトレースを記録し、失敗時にコスト・レイテンシ・根拠となったコンテキストを遡って確認できるようにする

## 使いどころ

- LLMアプリ/エージェントの品質劣化をCIで継続的に検知したいチーム
- 既存のpytest/Vitest資産を流用しつつevalを始めたいエンジニアリング組織
