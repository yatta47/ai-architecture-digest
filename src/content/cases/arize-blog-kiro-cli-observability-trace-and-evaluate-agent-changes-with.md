---
type: guidance
title: Kiro CLIとArize Skillsでコーディングエージェントの変更を検証するワークフロー
title_original: 'Kiro CLI observability: trace and evaluate agent changes with Arize Skills'
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llmops
- eval
- prompt-optimization
components:
- Kiro CLI
- Arize Skills
- Arize AX
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/kiro-cli-observability-arize-skills/
published_at: '2026-07-15'
---

## 概要

Amazonのターミナル型コーディングエージェントKiro CLIと、Arizeが提供するパッケージ済みワークフロー「Arize Skills」を組み合わせ、コーディングエージェントが加えた変更をトレース・データセット化・実験比較で検証してからマージする検証ループを構築する方法を紹介。

## 設計のポイント

- コーディングエージェント自身に計装追加・トレースエクスポート・データセット構築・実験実行までを自然言語指示で行わせる。
- 本番の失敗トレース(groundedness失敗やエラー終了など)からそのまま回帰用データセットを自動生成する。
- 変更前後のプロンプト/実装をデータセットに対する実験として比較し、マージ可否を定量的に判断する。

## 使いどころ

- コーディングエージェントによる変更を「diffを眺めて終わり」ではなく定量評価してから出荷したい開発チーム。
- コーディングハーネス自体のツール呼び出し・コスト・コンテキスト使用量を可視化したいチーム。
