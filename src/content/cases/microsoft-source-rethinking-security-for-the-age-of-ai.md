---
type: announcement
title: エージェント型セキュリティ基盤「Project Perception」のマルチモデルCyber Stack
title_original: Rethinking security for the age of AI — Introducing Project Perception
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- multi-agent-orchestration
- multi-model-routing
- context-engineering
- ai-agent
components:
- MAI-Cyber-1-Flash
- MDASH
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/
published_at: '2026-07-27'
---

## 概要

Microsoftは、AIエージェントによる機械速度の攻撃に対抗するため、赤（攻撃経路発見）・青（リスク評価）・緑（是正措置）の3種のエージェントが閉ループで連携するエージェント型セキュリティシステム「Project Perception」を発表した。フロンティアモデルと専用サイバーモデル（MAI-Cyber-1-Flash等）を組み合わせたマルチモデルアーキテクチャで品質とコストを最適化し、脆弱性管理のMDASHでは業界ベンチマークCyberGymで96%のスコアと約50%のコスト削減を実現したという。同システムは2026年8月3日にパブリックプレビューが開始される。

## 設計のポイント

- Red/Blue/Greenの3種類の専門エージェントが発見・評価・是正を担う閉ループ構成で継続的にセキュリティ体制を改善する
- 単一の万能モデルに頼らず、タスクごとに品質・信頼性・レイテンシ・コストで最適なモデルを選ぶマルチモデルアーキテクチャを採用する
- 生のシグナルをエージェントがその都度収集・相関させるのではなく、トークン効率の良い『セキュリティコンテキスト』として事前に構造化して提供する
- シグナル/コンテキスト/モデル/エージェント/アクチュエータの各層をハーネスが調停するスタック構成にし、層ごとに交換可能にする

## 使いどころ

- 攻撃側の生成速度や自動化が高度化し、人手中心の検知・対応では追いつかなくなったSOC・セキュリティ運用チーム
- 24時間365日の稼働が前提となるためコスト効率と検知品質の両立が必要なセキュリティ運用
- ソフトウェア脆弱性管理など、特定のセキュリティタスクに特化したモデルで既存ワークフローの精度とコストを改善したい場面
