---
type: announcement
title: Copilot CLIがローカルOllamaモデルを検出して利用可能に
title_original: Discover local models in GitHub Copilot CLI
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- inference-optimization
components:
- GitHub Copilot CLI
- Ollama
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-07-discover-local-models-in-github-copilot-cli
published_at: '2026-10-07'
---

## 概要

Copilot CLIの/modelで起動中のOllamaのローカルモデルを検出し、確認後にセッションで使える。ツール呼び出しとストリーミング対応が条件で、自動追加はされない。

## 設計のポイント

- 検出しても自動追加せず、ユーザー確認を挟む。
- クラウドとローカルのモデルを同じ選択UIに並べる。

## 使いどころ

- 機密コードを外に出したくない開発者や、コストを抑えたい場面に効く。
