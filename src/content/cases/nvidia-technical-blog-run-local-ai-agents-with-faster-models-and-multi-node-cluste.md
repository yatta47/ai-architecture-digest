---
type: guidance
title: DGX Sparkでローカルエージェントを数分で起動するNemoClawインストールフロー
title_original: Run Local AI Agents with Faster Models and Multi-Node Clustering on NVIDIA DGX Spark
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- unified-runtime
- inference-optimization
components:
- NVIDIA DGX Spark
- NVIDIA NemoClaw
- NVIDIA OpenShell
- Hermes Agent
- OpenClaw
- Qwen3.6-35B
- Ollama
- vLLM
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/run-local-ai-agents-with-faster-models-and-multi-node-clustering-on-nvidia-dgx-spark/
published_at: '2026-06-11'
---

## 概要

NVIDIA DGX Spark上でオープンモデル・エージェントハーネス・セキュアなOpenShellランタイムを一括インストールするNemoClawの導入フローを解説。単一コマンドでOllamaとQwen3.6-35Bのセットアップまで完了し、デイリーニュースダイジェストやソフトウェア開発エージェントなど4種のテンプレートエージェントをすぐに試せるほか、複数台構成によるマルチノードクラスタ拡張にも対応する。

## 設計のポイント

- オープンモデル・エージェントハーネス(Hermes Agent/OpenClaw)・セキュアランタイム(OpenShell)の3要素を1つのインストールパッケージにまとめ、構築の手間を単一コマンドに圧縮する
- OpenShellのネットワークポリシーでツール権限を絞り込み、まず単一の狭いタスクで動作検証してから権限を広げる運用を推奨する
- ローカル推論により機密コンテキストをデバイス外に出さず、トークン課金なしでエージェントを運用できる構成にする

## 使いどころ

- クラウド依存や推論コストを避け、自分のハードウェア上で長時間稼働するエージェントを動かしたい開発者
- 機密性の高いコンテキストを外部に出せない環境でAIエージェントを試したいセキュリティ重視のチーム
