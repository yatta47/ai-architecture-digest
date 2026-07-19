---
type: case
title: 金融デューデリジェンスAI「Hebbia Matrix」を支えるClaudeモデル評価と多段エージェント運用
title_original: 'Working at the frontier: How Hebbia builds AI for financial diligence that can''t miss a detail'
company: Hebbia
industry: financial-services
cloud: []
patterns:
- ai-agent
- document-processing
- multi-agent-orchestration
- eval
components:
- Claude Fable 5
- Hebbia Matrix
outcome:
  type: quality
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail
published_at: '2026-07-13'
---

## 概要

Hebbiaは資産運用会社や投資銀行、PEファーム、与信部門向けに、数千件の文書を横断して調査・デューデリジェンスを行うAIプラットフォーム「Matrix」を提供しており、自然文の依頼をメタプロンプティングでステップ分解しClaudeに各工程を実行させ、回答をグリッドの1セルごとに引用付きで表示する。新モデルは必ず金融特化ベンチマークで旧モデルと比較検証しており、Claude Fable 5は同社が計測した中で最大の精度向上を記録し、与信契約のコベナンツ分析からメモ作成までの多段タスクをエンドツーエンドで任せられるようになった。

## 設計のポイント

- 自然文の依頼を『メタプロンプティング』でステップに分解し、各回答をグリッドの1セルに紐づけて透明性・追跡可能性・操作性を確保する。
- 新しいモデルをリリースごとに金融特化のベンチマーク（文書QA・引用照合、エージェント実行を含む）で旧モデルと頭合わせ比較してから採用する。
- すべての回答を必ず原典文書への引用としてグラウンディングし、推測ではなく証拠ベースの回答であることを担保する。
- サブエージェント/ツール呼び出しを組み合わせ、長時間・多段階のオープンエンドな分析タスク全体を見失わずに保持する設計にする。

## 使いどころ

- 資産運用会社・投資銀行・PEファーム・与信部門など、大量の非構造化文書からリスクや財務条件を抽出し投資判断に活用する業務。
- モデル更新のたびに業務特化ベンチマークで精度回帰がないかを検証したいAI活用チーム。
