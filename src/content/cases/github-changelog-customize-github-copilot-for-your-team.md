---
type: announcement
title: Copilotのチーム単位のプラグイン既定設定が一般提供
title_original: Customize GitHub Copilot for your team
company: GitHub
industry: cross-industry
cloud: []
patterns:
- policy-as-code
components:
- GitHub Copilot
- Agent Plugins
- Copilot CLI
- VS Code
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-18-customize-github-copilot-for-your-team
published_at: '2026-11-18'
---

## 概要

チームのメンテナーや組織オーナーが承認済みエージェントプラグインをチーム既定として選べるようになった。個人設定と組織ポリシーの中間層として、メンバーのセットアップの重複を減らす。

## 設計のポイント

- 個人設定と組織ポリシーの間にチーム層を置き、共通の出発点を配る。
- 組織・エンタープライズのポリシーを常に優先し、チーム既定では上書きさせない。

## 使いどころ

- チーム共通のエージェント環境を一括配布したい開発組織。
- 新メンバーのオンボーディングを簡素化したいチーム。
