---
type: announcement
title: リポジトリとトレースからエージェント評価を自動生成するスキル
title_original: Towards Automating Eval Engineering
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- ai-agent
- ci-cd
components:
- Harbor
- LangSmith
- langsmith-cli
- chat-langchain
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/towards-automating-eval-engineering
published_at: '2026-07-22'
---

## 概要

LangChainが、リポジトリ構造とエージェントの実行トレースから測定すべき能力を推定し、Harbor形式の実行可能な評価一式を生成するEval Engineering Skillを公開した。プロンプト・ツール・スキルなどのエージェント構成とAPI呼び出しの実挙動をトレースから読み取り、ユーザーとの対話を通じて評価案を1つずつ承認しながら構築する。ドキュメントQ&AエージェントのChat-LangChainで検証済みで、Instruction・環境(Dockerfile)・Verifierの3要素からなるタスクを生成する。

## 設計のポイント

- リポジトリを走査してプロンプト・モデル・ツール・スキル・フックなどエージェント構成全体をマッピングしてから評価案を提案する
- LangSmith等のトレースから実際のツール呼び出し(引数・結果・エラー)を収集し、本番挙動を再現した評価環境に反映する
- 一発生成ではなくユーザーへのインタビューを繰り返し、提案した評価方向性を1件ずつ選択・承認させることで採用率を高める
- コストが発生する/本番書き込みを伴うツール呼び出しはシミュレートし、エージェントとverifier双方のトラジェクトリを見比べて報酬ハッキングを検出しながら改善する

## 使いどころ

- 本番トレースから頻出する失敗パターンを収集し、再発防止用の評価に変換したいエージェント開発チーム
- プロンプト・ツール・モデルやエージェント構成の変更を横断的に比較する際の固定ターゲットとして評価を整備したい場合
- Verifierが意図した能力を正しく測れているか(reward hackingしていないか)を検証・改善したい場面
