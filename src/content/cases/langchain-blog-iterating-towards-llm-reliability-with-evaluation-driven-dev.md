---
type: case
title: Evaluation Driven DevelopmentでLLM信頼性を積み上げるDosuの開発フロー
title_original: Iterating Towards LLM Reliability with Evaluation Driven Development
company: Dosu
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
components:
- LangSmith
- Dosu
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/iterating-towards-llm-reliability-with-evaluation-driven-development
published_at: '2026-06-15'
---

## 概要

OSSメンテナンスAIアシスタントDosuが、Evaluation Driven Development(EDD)によってLLMロジックの変更影響を継続的に検証する開発フローを解説。プロンプトをGit管理しコードと同じレビュー基準を適用し、LangSmithの@traceableデコレータで本番トレースを可視化して失敗モードを評価データセットに追加していく。

## 設計のポイント

- 新機能→本番投入→失敗モード収集→オフライン評価に追加→再投入というEvaluation Driven Developmentのループを回す
- プロンプトをコードと同様にGit管理し、変更にコードと同じレビュー基準を適用する
- @traceableデコレータで既存関数にトレーシングを後付けし、数分でLLM呼び出し全体を可視化する

## 使いどころ

- OSSメンテナンスなど大量の多様な問い合わせを自動対応するAIチームメイトを運用する場合
- プロンプト変更の副作用(ある領域で改善しても別領域で劣化する)を継続的に検知したい場合
