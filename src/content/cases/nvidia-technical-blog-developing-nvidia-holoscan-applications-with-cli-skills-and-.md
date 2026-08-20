---
type: case
title: NVIDIA Holoscanアプリ開発をAIコーディングエージェントとCLI/Skillsで加速
title_original: Developing NVIDIA Holoscan Applications with CLI, Skills, and AI Coding Agents
company: NVIDIA
industry: healthcare
cloud:
- on-prem
patterns:
- spec-driven-development
- ai-agent
components:
- NVIDIA Holoscan
- HoloHub
- Codex
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/developing-nvidia-holoscan-applications-with-cli-skills-and-ai-coding-agents/
published_at: '2026-08-19'
---

## 概要

NVIDIAは、リアルタイム内視鏡ツールセグメンテーションアプリケーションの開発を、AIコーディングエージェント（Codex/GPT-5.6）とHoloHubのCLI・開発Skills・ドキュメントを組み合わせて進めるワークフローを検証した。エンジニアが目標と制約を定義し、エージェントがHoloHub CLIで実装・テスト・ベンチマークを行い、エンジニアがレビューして次のイテレーションを指示するサイクルを繰り返す。アブレーション実験では、CLI・Skills・ドキュメント/サンプルを組み合わせた場合が最も効率よく高品質な開発ワークフローになった。

## 設計のポイント

- エージェントとエンジニアが同じHoloHub CLI（./holohubラッパー）を共通の実行インターフェースとして使うことで、エージェントの操作をエンジニアがそのまま検証・再現できるようにする
- 1回のプロンプトで全体を作らせず、不確実性とエビデンスに基づいて検証可能な小さなイテレーションに目標を分割し、各段階でコード・出力・テストをレビューしてから次を指示する
- agents.mdによるプログレッシブディスクロージャー方式のドキュメントと、holohub-app-lifecycle等の開発Skillsを与えることで、エージェントが既存の類似実装パターンを参照しながら実装できるようにする
- モデル重みの学習・変更は禁止するなど、再利用してよい範囲（モデル・データ）と実装させてよい範囲を最初のプロンプトで明確に切り分ける

## 使いどころ

- エッジで動くリアルタイムAIアプリケーションの開発に、AIコーディングエージェントを取り入れたいチーム
- 既存のCLI・ドキュメント・サンプルコード資産をエージェントに活用させ、開発速度と品質を両立させたいプラットフォームチーム
- 一発生成ではなく、エンジニアがレビューしながら段階的にエージェントの実装を進めたい開発プロセスを設計したい場合
