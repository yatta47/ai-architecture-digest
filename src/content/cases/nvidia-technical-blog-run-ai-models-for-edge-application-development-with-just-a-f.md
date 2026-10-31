---
type: announcement
title: DGX Spark上でEdge-LLMを数コマンドで動かす組み込みAI開発環境
title_original: Run AI Models for Edge Application Development with Just a Few Commands
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
components:
- NVIDIA TensorRT Edge-LLM
- NVIDIA DGX Spark
- Jetson Thor
- trtedge CLI
- Nemotron
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/run-ai-models-for-edge-application-development-with-just-a-few-commands/
published_at: '2026-10-30'
---

## 概要

TensorRT Edge-LLMは軽量なC++推論ランタイムで、DGX Sparkでの開発からJetson Thorなどへの展開までを一貫して扱える。trtedge CLIでモデル取得とエンジンビルドを行い、OpenAI互換APIサーバーでローカルに試作でき、DSpark投機的デコーディングで生成速度が73.4から126.9トークン/秒に向上した。

## 設計のポイント

- モデル取得とTensorRTエンジンのビルドを1つのCLIにまとめて環境構築を短縮する。
- OpenAI互換APIでローカル提供し、既存のアプリ試作コードを流用する。
- 投機的デコーディングで、ピークメモリを抑えたまま生成速度を高める。

## 使いどころ

- 車載・ロボット・産業機器などメモリと電力に制約のあるエッジAIの試作チーム。
- 開発機から実機ターゲットまで同じ推論ランタイムで揃えたい組み込み開発者。
