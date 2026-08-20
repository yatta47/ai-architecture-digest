---
type: guidance
title: NVIDIA SkillEvaluator：エージェントSkillの効果を三層評価で定量化する
title_original: Evaluating AI Agent Skill Performance with NVIDIA SkillEvaluator
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
components:
- NVIDIA SkillEvaluator
- Harbor
- Claude Code
- Codex
- Cursor
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/evaluating-ai-agent-skill-performance-with-nvidia-skillevaluator/
published_at: '2026-08-18'
---

## 概要

NVIDIAは、エージェント向けSkill（ツールの使い方や手順をまとめた能力記述）が実際にエージェントの成果を改善しているかを測るオープンソースの評価レイヤーSkillEvaluatorを公開した。静的チェック・埋め込み類似度によるSkill間の重複検出・隔離サンドボックスでのSkillあり/なし実タスク比較という3段階評価を行い、30以上のNVIDIA製品にまたがる300以上の検証済みSkillをベンチマークした結果、正確性・発見可能性・有効性・効率の各観点で平均31ポイント（セキュリティ除くと39ポイント）のSkill Liftが確認された。

## 設計のポイント

- 公開前にTier1（構造・セキュリティの静的チェック）、Tier2（埋め込み類似度によるSkill内外の重複検出）、Tier3（隔離サンドボックスでの実タスク比較）という三層評価を経てから配布する
- Tier3では同一プロンプト・モデル・タスク入力・採点基準のまま、Skillのインストール有無だけを変数にして2つの独立したエージェントハーネスで実行し、差分をSkill Liftとしてポイント化する
- Correctness/Discoverability/Effectiveness/Efficiency/Securityの5軸でスコアリングし、Securityは改善ではなく『Skill導入でリグレッションが起きていないか』を検証する目的に限定する
- 評価用データセット生成から実行・採点までをオープンソースのHarborフレームワークとCLIで一気通貫にし、ユーザー側のワークフローを簡素化する

## 使いどころ

- 自社のツール/ライブラリ向けにエージェント用Skillを作成しており、実際に効果があるか定量的に検証したいプラットフォームチーム
- 複数のエージェントハーネス（Claude Code、Codex、Cursorなど）にまたがってSkillの効果が一貫しているか確認したい場合
- トークン消費や実行ステップ数の無駄を減らすため、Skill導入の効果測定を継続的なCIプロセスに組み込みたいチーム
