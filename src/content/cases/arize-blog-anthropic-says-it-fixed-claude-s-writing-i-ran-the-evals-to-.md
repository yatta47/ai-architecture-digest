---
type: opinion
title: Opus 5.5の文章の癖をevalで検証する
title_original: Anthropic says it fixed Claude's writing. I ran the evals to check.
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
components:
- Arize AX
- Claude Opus 5.5
- Claude Opus 5
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/anthropic-says-it-fixed-claudes-writing/
published_at: '2026-09-29'
---

## 概要

Anthropicが「Opus 5.5で文章が改善した」と述べた点を、Arize AXのevalループで検証した記事。20本の固定ブリーフで比較したところ、エムダッシュは1,000語あたり12.9回からほぼゼロになり、その他のClaude臭い表現も半減したが、完全には解消していないと結論づけている。

## 設計のポイント

- 入力を固定したデータセットで実験を回し、変更点をモデルだけに絞って比較する。
- 人手のアノテーションから評価器を作り、注釈との一致を見ながら反復する。
- エムダッシュ計数のような決定的な指標と、LLMによる判定を併用する。

## 使いどころ

- モデル更新の主張を自社の課題で確かめたい開発チーム。
- 文章生成の品質を継続的に測りたい担当者。
- 評価の基本ループを学びたい人。
