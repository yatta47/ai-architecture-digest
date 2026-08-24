---
type: guidance
title: スキルもエージェントとして計測する—Arize AXによるコーディングスキルの効果測定
title_original: A skill is just an agent. So measure your changes.
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
components:
- Arize AX
- Arize Phoenix
- OpenInference
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/quantifying-skill-changes-arize-ax/
published_at: '2026-08-24'
---

## 概要

Arizeは、Claude CodeなどのコーディングエージェントにインストールするSkill(指示書)も「ハーネス+プロンプト」という意味で通常のエージェントと同じであり、トレース・評価・実験で変更の効果を定量的に検証できると説明する。ゴールデンデータセットとサンドボックス化された実験環境、トレースレベルの評価器(LLMジャッジ+コード評価器)を組み合わせ、スキル変更が実際に精度・速度・コストを改善したかを「勘」ではなく数値で判断する手法を、実際のマージ済みPRの数値とともに解説する。

## 設計のポイント

- スキルを「ハーネス+プロンプト」というエージェントと同一の構造として捉え、既存のエージェント評価手法(トレース+eval+実験)をそのまま適用する
- 同じ指示でも非決定的に異なる挙動を取るため、単発の手動確認ではなく複数回の実行を比較する実験設計で変更の効果とノイズを切り分ける
- LLMジャッジによる主観評価と、監視対象の挙動(自動計装の使用有無・セッション生成有無など)を機械的に確認するコード評価器を組み合わせてスコアリングする
- エージェントがベンチマークを「ズルして」通過しないよう、サンドボックス化された環境でテスト対象アプリをクリーンな状態に保つ

## 使いどころ

- 社内で配布しているコーディングエージェント向けSkill/プロンプトの改善が本当に効果があったかを検証したいチーム
- 非決定的なLLM挙動を前提にA/B比較や回帰検知をしたいプロンプトエンジニアリングのワークフロー
