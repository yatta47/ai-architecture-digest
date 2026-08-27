---
type: guidance
title: コーディングエージェントとCOMPASSでロボットナビゲーションポリシーを機体横断に適応させる
title_original: How to Train a Cross-Embodiment Robot Navigation Policy with AI Agents
company: NVIDIA
industry: logistics
cloud:
- on-prem
patterns:
- ai-agent
- reinforcement-learning
- human-in-the-loop
components:
- NVIDIA Isaac Lab
- NVIDIA Isaac Sim
- NVIDIA Omniverse NuRec
- NVIDIA cuVSLAM
- X-Mobility
- Codex
- Claude Code
- Boston Dynamics Spot
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-train-a-cross-embodiment-robot-navigation-policy-with-ai-agents/
published_at: '2026-08-26'
---

## 概要

NVIDIAは、事前学習済みナビゲーションポリシーX-Mobilityを個々のロボット・環境向けに適応させるCOMPASSフレームワークを、コーディングエージェント駆動のワークフローとして提供する。エージェントが依存関係検証・シーン準備・スモークテスト・残差RL学習・チェックポイント評価をリポジトリ内スキルで自動実行し、シーン承認や学習開始などの節目には人間の承認ゲートを挟むことで、Boston Dynamics Spotなど新しい機体・環境ごとにゼロから作り直す再学習コストを抑える。

## 設計のポイント

- ベースポリシー（X-Mobility）を丸ごと再学習せず、機体固有の差分だけを補正する残差RL（residual RL）を学習することで適応コストを下げる
- 検証・準備・学習・評価という一連のパイプラインをリポジトリ付属のスキルとしてエージェントに実行させ、シーン承認・スモークテスト通過・チェックポイント昇格の3箇所に人間承認ゲートを設ける
- ベースポリシーと候補ポリシーを同一シード・同一ゴール・同一ロールアウト条件で比較する『条件を揃えた評価』により、改善が本物かを判定する
- 実機環境で互換オドメトリが無い場合はcuVSLAMによる視覚オドメトリで代替するなど、デプロイ時の依存を明示的に切り分ける

## 使いどころ

- 既存のナビゲーションポリシーを新しいロボット機体や新しい環境（倉庫・屋内シーン）へ再利用したいロボティクスチーム
- シミュレーションでの学習・検証・評価という反復作業をエージェントに自動化させつつ、要所は人間承認で安全に統制したいチーム
- 機体・環境ごとの再現可能なナビゲーション性能比較（到達率・転倒率・所要時間）を標準化したいチーム
