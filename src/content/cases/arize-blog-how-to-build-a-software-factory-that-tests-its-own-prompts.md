---
type: case
title: GitHub issueからリリースまでを担い、自分のプロンプトをテストするソフトウェアファクトリー
title_original: How to build a software factory that tests its own prompts
company: Arize
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- eval
- prompt-optimization
- ci-cd
components:
- Arize AX
- GitHub Actions
- Gemini
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-to-build-a-software-factory-that-tests-its-own-prompts/
published_at: '2026-10-22'
---

## 概要

GitHubのissueを起点に、仕様化・実装・CI・レビューなどの各工程にエージェントを置き、全工程をArize AXでトレースするソフトウェアファクトリーの試作例。CIやレビューが出す合否の判定を再利用し、プロンプトを本番前にテスト・改善する。

## 設計のポイント

- CI・レビュー・差し戻しなどが既に出す判定を、エージェント実行とプロンプトに紐づけて評価に使う。
- 人は issue の記述といくつかのゲートでの判断に集中させ、コードは書かせない。
- 工程ごとのトレースを取り、エージェントの観測性と評価を一体で整える。

## 使いどころ

- エージェントで開発工程を自動化し、出力の良し悪しの判断が詰まりになっているチーム。
- プロンプト変更を本番投入前に検証したいLLMOps担当。
