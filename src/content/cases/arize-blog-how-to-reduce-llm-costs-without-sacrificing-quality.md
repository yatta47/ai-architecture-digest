---
type: guidance
title: トレースからLLMコストと品質を同時に最適化する手法
title_original: How to reduce LLM costs without sacrificing quality
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
- eval
components:
- Arize AX
- OpenTelemetry
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-to-reduce-llm-costs-without-sacrificing-quality/
published_at: '2026-08-31'
---

## 概要

Arizeは、LLMコストを『トークン単価×トークン使用量』に分解し、モデル呼び出し・ツール・リトライを含む処理全体をトレースしてスパン単位でコストを可視化する手法を紹介している。コストと品質を同じトラフィック・期間で突き合わせる4象限のマトリクス（高コスト×低品質は削減、高コスト×高品質は温存など）を使い、変更のたびに固定データセットと品質基準で検証することで、安易なモデル切り替えによる品質劣化を防ぐ。

## 設計のポイント

- モデル呼び出し・検索・ツール・リトライを含む処理全体をOpenTelemetry互換でトレースし、スパン単位でコストと品質評価結果を紐づける
- 入力・出力・キャッシュ・推論トークンごとに単価を設定し、コストの発生源となっているスパンを特定してから原因（コンテキスト肥大化・リトライ・ツール応答過多など）を切り分ける
- コストと品質を同一トラフィックで4象限に整理し、『高コスト×低品質』のパターンだけを優先的に削減対象にする
- 最適化のたびに固定データセットと同じ品質バーで検証し、コスト削減が品質を犠牲にしていないことを確認する

## 使いどころ

- 本番運用中のLLMアプリケーションで、請求額の増加要因（モデル・リトライ・コンテキスト肥大化など）を特定したいSRE/MLOpsチーム
- コーディングエージェントのトークン消費が大きく、安価なモデルへの切り替えが本当にコスト削減になるか検証したい場合
- コスト削減の施策が品質低下を招いていないかを継続的に監視したいプロダクトチーム
