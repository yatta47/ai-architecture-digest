---
type: announcement
title: VSS Blueprint 3.3による映像AIエージェントの構築自動化とVLM推論コスト削減
title_original: Lower the Cost of Building and Running Visual AI Agents with NVIDIA VSS Blueprint 3.3
company: NVIDIA
industry: manufacturing
cloud: []
patterns:
- video-intelligence
- ai-agent
- rag
- inference-optimization
components:
- NVIDIA Metropolis VSS Blueprint
- NVIDIA Cosmos
- NVIDIA Nemotron
- Model Context Protocol
- Kafka
- Redis
- Elasticsearch
- vLLM
- Cosmos NIM
- RTX PRO 6000 Blackwell
- Claude Code
- Codex
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/
published_at: '2026-09-29'
---

## 概要

NVIDIA Metropolis VSS Blueprint 3.3は、Cosmosなどの VLM、Nemotron等のLLM、RAG、MCPツールを組み合わせ、ライブ/録画映像を自然言語検索・Q&A・検証済みアラート・レポートに変換する。新しいBuild Vision Agentスキルは単一プロンプトから検証済みプロファイルを基に複数ワークフローを構成し、ボトリングラインのデモを30分未満でデプロイした。Adaptive EVSは変化のないパッチを動的に刈り込み、60分動画の要約でVLM入力トークンを80%削減、同一GPUでの同時ストリーム数を46%増やした。

## 設計のポイント

- デプロイをゼロから生成せず、4つの検証済み開発者プロファイルのうち最も近いものを基盤とし、要求された機能に必要な差分だけを追加する。
- Kafka・Redis・Elasticsearchなどの共有インフラは単一インスタンスに集約し、ワークフロー追加時の重複を避ける。
- 前フレームから変化のない視覚パッチのトークンを動的に刈り込み、活動のある瞬間にVLM処理をバッチ化して推論コストを下げる。
- コーディングエージェントのスキルとしてデプロイ・運用手順を提供し、自然言語の要求から構成と拡張を行う。

## 使いどころ

- 製造ラインの異常（溢れなど）検知・アラート検証・シフトレポートを映像AIで自動化したい工場。
- 倉庫やスマートシティで検出・アラート・検索・要約を組み合わせた映像エージェントを構築したいチーム。
- 多数のカメラストリームでVLM推論のGPUコストとトークン量を抑えたい運用者。
