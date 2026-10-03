---
type: announcement
title: GitHub Copilotで一部モデルを非推奨化、後継モデルへ移行
title_original: Selected models in GitHub Copilot deprecated
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
components:
- GitHub Copilot
- Gemini 3.5 Flash
- Gemini 3.6 Flash
- Kimi K2.7 Code
- Claude Opus 4.7
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-02-selected-models-in-github-copilot-deprecated
published_at: '2026-10-02'
---

## 概要

2026年10月2日付で、GitHub Copilotの全体験でGemini 3.5 Flash、Gemini 3.6 Flash、Kimi K2.7 Code、Claude Opus 4.7が非推奨になった。後継はGemini 3.8 Flash、Kimi K3、Claude Opus 5.5。Enterprise管理者はモデルポリシーで代替モデルを有効化する必要がある。

## 設計のポイント

- モデルの非推奨に備え、後継モデルを事前にポリシーで有効化しておく運用が要る。
- 利用モデルを固定せず、代替先を切り替えられる設計にしておく。

## 使いどころ

- Copilotを全社展開している管理者が、モデルポリシーを見直す場面。
- LLM依存のワークフローで、モデル廃止時の移行手順を整えるチーム。
