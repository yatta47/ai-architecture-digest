---
type: guidance
title: LM Studioでgpt-oss-20b/120bをローカル実行する手順
title_original: How to run gpt-oss locally with LM Studio
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
components:
- gpt-oss-20b
- gpt-oss-120b
- LM Studio
outcome:
  type: cost
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/articles/gpt-oss/run-locally-lmstudio/
published_at: '2025-08-07'
---

## 概要

コンシューマー向けPCやApple Siliconマシンでgpt-oss-20b/120bをローカル実行するためのデスクトップアプリLM Studioのセットアップ手順を解説する。llama.cppとApple MLXの両エンジンをサポートし、チャットからMCPサーバー連携まで扱える。

## 設計のポイント

- 20Bモデルは16GB VRAM級のコンシューマーGPU、120BモデルはマルチGPUや60GB以上のワークステーション向けと明確に住み分ける
- サーバー用途のGPU(H100等)向けにはvLLMガイドへ誘導し、LM Studioはあくまでコンシューマーハードウェア向けと位置づける

## 使いどころ

- APIコストをかけずにgpt-ossをローカルで試したい個人開発者
- オフライン環境やプライバシー制約下でLLMを動かしたいチーム
