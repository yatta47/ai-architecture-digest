---
type: guidance
title: 人のレビューをエージェント評価の基盤にする考え方
title_original: Why human insight is a strategic advantage for building better agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- human-in-the-loop
- llmops
components:
- LangSmith
- Annotation Queue
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/human-insight-strategic-advantage-agents
published_at: '2026-11-04'
---

## 概要

エージェント評価では、専門家が良し悪しの基準を定め、会話全体の文脈でレビューし、そのフィードバックを評価データへ再利用する3原則を示す。LangSmithのアノテーションキューで、スコアとコメントをLLMジャッジの較正やゴールデンデータセットに活かす。

## 設計のポイント

- 自動評価が怪しいトレースを選び、人が理由付きで判断する。
- 単一ステップでなくスレッド全体を見て文脈で評価する。
- 人のスコアでLLMジャッジとオンライン評価を較正する。

## 使いどころ

- ドメイン固有の品質基準を持つエージェントの評価体制を作るとき。
- LLMジャッジの精度を上げたいとき。
