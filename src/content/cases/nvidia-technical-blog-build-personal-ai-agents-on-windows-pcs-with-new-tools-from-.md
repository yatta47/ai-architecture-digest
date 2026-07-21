---
type: announcement
title: NVIDIAとMicrosoft、Windows PC向けオンデバイスAIエージェント基盤（MXC/OpenShell/RTX Spark）を発表
title_original: Build Personal AI Agents on Windows PCs with New Tools from Microsoft and NVIDIA
company: NVIDIA / Microsoft
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- inference-optimization
- defense-in-depth
- unified-runtime
components:
- NVIDIA RTX Spark
- Surface RTX Spark Dev Box
- Microsoft eXecution Containers (MXC)
- NVIDIA OpenShell
- NVIDIA NemoClaw
- Hermes Agent
- H Company Holo 3.1
- OpenClaw
- llama.cpp
- vLLM
- LM Studio
- ComfyUI
- NVIDIA DGX Spark
- NVIDIA DGX Station
- GeForce RTX
- NVIDIA RTX PRO
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/build-personal-ai-agents-on-windows-pcs-with-new-tools-from-microsoft-and-nvidia/
published_at: '2026-06-25'
---

## 概要

NVIDIAとMicrosoftはCOMPUTEX 2026とMicrosoft Build 2026で、Windows PC上でオンデバイスAIエージェントを安全かつ高速に動かすための新ツール群を発表した。セキュリティ面ではMicrosoft eXecution Containers（MXC）とそのランタイムであるNVIDIA OpenShellにより、エージェントのファイル・システムアクセスを制限しプロンプトインジェクションのリスクを抑える。性能面ではRTX Sparkハードウェアや、投機的デコーディング（MTP）・並行カーネル実行（PDL）などの推論最適化により、llama.cppで最大2倍、vLLMで最大2.6倍のスループット向上を実現している。

## 設計のポイント

- MXCをOSレベルのポリシー層とし、Windowsのネイティブな分離機構に処理を委譲することで、エージェントによるファイル・システムアクセスを制限しプロンプトインジェクションの被害範囲を抑える設計
- OpenShellをMXC上に構築されたランタイムとして提供し、ポリシー管理・推論ルーティング・PII匿名化などのエージェント運用機能を一つの統合レイヤーにまとめる
- MTP（投機的デコーディング）は既存モデルへの追加学習なしに適用でき、PDL（依存カーネルの並行実行）と組み合わせることで推論スループットを底上げする
- 専用ハードウェア（RTX Spark）とOS・開発者エディション（Surface RTX Spark Dev Box）を一体で用意し、ツール群をプリロードすることでオンデバイスエージェント開発のセットアップ障壁を下げる

## 使いどころ

- 個人開発者やクリエイターが、コーディングやビデオ編集など日常タスクを支援するオンデバイスAIエージェントを構築したい場面
- 常時稼働（24/7）で動くエージェントを、個人ファイルやネイティブアプリと安全に統合しながらサンドボックス化したい場合
- ローカルのRTX/DGXなどのGPU環境でllama.cppやvLLMを用いてエージェント向け推論性能を最大化したい開発者
- 画面を見てクリック操作を行うComputer Use型のエージェントをローカルモデルで動かしたいケース
