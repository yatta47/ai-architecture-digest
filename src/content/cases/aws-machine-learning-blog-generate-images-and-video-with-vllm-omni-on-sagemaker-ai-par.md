---
type: guidance
title: 同一DLCで画像生成とビデオ生成を使い分けるSageMaker AI基盤（FLUX.2×Wan VACE）
title_original: Generate images and video with vLLM-Omni on SageMaker AI – Part 2
industry: cross-industry
cloud:
- aws
patterns:
- generative-video-editing
- unified-runtime
- inference-optimization
components:
- Amazon SageMaker AI
- vLLM-Omni
- FLUX.2-klein
- Wan2.1-VACE
- Amazon S3
- Streamlit
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/generate-images-and-video-with-vllm-omni-on-sagemaker-ai-part-2/
published_at: '2026-09-28'
---

## 概要

同じvLLM-Omni DLCイメージから、リアルタイム推論の画像生成エンドポイント（FLUX.2-klein）と非同期推論の動画生成エンドポイント（Wan VACE）を使い分ける構成を紹介する。画像はアプリに同期応答し、時間のかかる動画生成はS3を介した非同期ポーリングで結果を取得する。

## 設計のポイント

- 同一コンテナイメージを使い回しつつ、SM_VLLM_MODEL環境変数の切り替えだけでモデルを差し替え、サービングスタックのばらつきを抑える。
- 即時応答が要る画像生成はリアルタイムエンドポイント、時間のかかる動画生成はSageMaker Asynchronous Inferenceでキューイングし、クライアントはS3の出力先をポーリングする。
- 生成画像をリサイズ・JPEG化してからVideo APIのマルチパートリクエストに埋め込み、モデル間の中間データをS3経由で受け渡す。

## 使いどころ

- テキストプロンプトから静止画を作り、それを動かして短尺動画に仕上げたいクリエイティブ生成ワークフロー。
- レイテンシ要件が異なる複数の生成モデルを1つの基盤上で併用したいAIプロダクト。
