---
type: announcement
title: Windows上のローカルモデルとクラウドを使い分けるCopilot
title_original: Bringing local models and sandboxed tools to Windows and GitHub Copilot
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- multi-model-routing
- inference-optimization
- defense-in-depth
components:
- GitHub Copilot
- Microsoft Execution Containers
- Project HydraFusion
- NVIDIA RTX
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://commandline.microsoft.com/local-models-sandboxed-tools-github-windows/
published_at: '2026-10-07'
---

## 概要

GitHub Copilotがタスクごとにオンデバイス推論とクラウドモデルを自動で使い分ける機能を予告。エージェント実行を守るMXCサンドボックスも紹介する。

## 設計のポイント

- タスクに応じてローカルとクラウドの推論を自動で振り分ける。
- エージェント実行はサンドボックスで境界を定める。

## 使いどころ

- コストや遅延、データ持ち出しを抑えたい開発者環境に効く。
