---
type: announcement
title: Copilot内で画像を生成・編集する機能
title_original: Generate and edit images directly in Copilot
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
components:
- GitHub Copilot
- GPT Image 2.5 Flare
- VS Code
- Copilot CLI
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-28-generate-and-edit-images-directly-in-copilot
published_at: '2026-10-28'
---

## 概要

CopilotのチャットでGPT Image 2.5 Flareを使った画像生成・編集が公開プレビューになった。推論モデルが画像生成ツールを呼び出し、結果をプレビューしてワークスペースに保存する。

## 設計のポイント

- 推論モデルが専用の画像生成ツールを呼ぶツール連携で実装されている。
- 管理者がモデルポリシーで無効化でき、AI透かしは任意で付けられる。

## 使いどころ

- コーディング中に外部ツールへ移らず画像素材を用意したい開発者。
- 組織として生成画像の利用を統制したい管理者。
