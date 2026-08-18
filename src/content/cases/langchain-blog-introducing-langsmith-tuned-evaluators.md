---
type: announcement
title: 本番トレースを自動評価するLangSmithのTuned Evaluators
title_original: Introducing LangSmith Tuned Evaluators, starting with Perceived Error
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- human-in-the-loop
components:
- LangSmith
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/introducing-langsmith-tuned-evaluators-starting-with-perceived-error
published_at: '2026-08-18'
---

## 概要

LangChainは本番のエージェント会話に自動で品質フィードバックを付与する『Tuned Evaluators』を提供開始し、第一弾として『Perceived Error(ユーザーが感じた失敗)』を検出する専用モデルをリリースした。フロンティアモデルによるLLM-as-judgeより高精度でありながら評価コストを最大82%(一部パートナーでは98%)削減し、プロンプト設計・ジャッジモデルの選定・運用をLangChainが一括で管理するマネージド評価として提供する。

## 設計のポイント

- 評価対象ごとに専用の事後学習済み判定モデルを用意し、汎用フロンティアモデルによるLLM-as-judgeより低コスト・高精度な評価を実現する
- プロンプト設計・モデル選定・バージョン管理・推論基盤の運用をすべてLangChain側が担うマネージド型にすることで、チームは評価器を選んでトレーシングプロジェクトに接続するだけでよい
- サンプリングではなく、人間-AIの応答ペアが2件以上かつアイドル期間を満たした対象トレース/スレッド全件を評価対象にすることで、明示的な低評価がない失敗も見逃さない
- 評価結果と説明をトレースに付与し、データセット拡充・CI連携・人間レビューへのルーティングなど既存の改善ワークフローにそのまま組み込めるようにする

## 使いどころ

- 会話型AIエージェントを本番運用しており、システムエラーや明示的な低評価が出ない『気づかれない失敗』を検知したいチーム
- 自前の評価基盤をゼロから構築する前に、まず品質のセーフティネットを即座に立ち上げたい立ち上げ期のチーム(Vanta社の事例)
- フラグが立ったトレースを人間レビューや評価データセットの拡充に回し、継続的にエージェントを改善したい運用チーム
