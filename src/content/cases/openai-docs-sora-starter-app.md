---
type: guidance
title: Sora Video APIを使った動画生成サンプルアプリ
title_original: Sora Video API sample app
industry: media
cloud: []
patterns:
- generative-video-editing
components:
- Sora
- gpt-image-1
- OpenAI SDK
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://github.com/openai/openai-sora-sample-app
published_at: '2025-10-15'
---

## 概要

OpenAIのSora Video APIを使った動画生成・リミックスを試せるNext.jsのサンプルアプリ。テキストプロンプトや画像入力から動画を生成し、gpt-image-1で生成した静止画を入力参照として使うワークフローを提供する。

## 設計のポイント

- 動画生成ジョブの状態をポーリングし複数バリエーションを並行キューイングする
- 既存動画のリミックスと新規生成を同じ履歴データモデルで扱い比較を容易にする
- Responses APIでプロンプトを自動最適化するステップを組み込む

## 使いどころ

- Sora Video APIの挙動をすぐ試したい開発者
- 動画生成機能を組み込んだプロダクトのプロトタイプを作りたいチーム
- プロンプトから画像参照を作り動画のスタイルを制御したいクリエイター
