---
type: guidance
title: エージェント評価（eval）の始め方と種類の整理
title_original: The Most Common Questions About Agent Evals, Answered
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
components:
- LangSmith
- Harbor
- Terminal-Bench
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/common-questions-about-agent-evals
published_at: '2026-10-15'
---

## 概要

LangChainがエージェント評価のよくある質問に答えた。実トレースから10〜20件の小さなデータセットを作ってベースラインを取り、開発前のオフライン評価と本番のオンライン評価を併用し、失敗をデータセットに戻す流れを示す。

## 設計のポイント

- コード評価を優先し、できない所だけLLM審査員を使い、人手で両方を確認する
- 多段のエージェントはスレッド・軌跡・最終状態を評価する
- 本番で見つけた失敗をデータセットに追加する

## 使いどころ

- エージェントの品質確認を始めたいがテスト方法が定まっていないチーム
