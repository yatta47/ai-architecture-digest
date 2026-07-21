---
type: guidance
title: Claude Codeのモデル選択と『Effort Level』の仕組み(トークン生成の裏側)
title_original: Choosing a Claude model and effort level in Claude Code
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
- inference-optimization
components:
- Claude Code
- Claude Sonnet
- Claude Fable 5
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-model-and-effort-level-in-claude-code
published_at: '2026-07-07'
---

## 概要

Claude Codeにおける『モデル選択』と『Effort Level』が実際に何を制御しているかを、トークナイズ・重み・自己回帰生成の仕組みから解説する。モデル選択はどの固定重みで応答するかを決め、Effort Levelはファイル読み込み数や検証の深さなど『どれだけ作業するか』を制御する、という区別を示す。

## 設計のポイント

- 定型作業には小さいモデル、複雑・曖昧なタスクには大きいモデルを使うという単純な使い分けを基本方針にする
- モデル/Effortはタスクごとに毎回変えるのではなく、作業の種類に応じたデフォルトから出発し全体的な好みとしてチューニングする
- 『十分な文脈を与えても間違えた』場合はより高性能なモデルへ、『ファイルを読み飛ばした/テストを実行しなかった』場合はEffort Levelを上げる、という切り分けを判断基準にする

## 使いどころ

- コストと精度のバランスを取りながらClaude Codeを日常的に使う開発者
- モデル選択とEffort Levelの違いを理解してチームの利用ガイドラインを作りたいテックリード
