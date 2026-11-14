---
type: opinion
title: 長期ゴール型エージェントは「フィードバックを得やすいスコープ」で設計する
title_original: 'Goal Engineering: How to Design Goals'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- context-engineering
components:
- LangChain
- Hone
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/goal-engineering
published_at: '2026-11-14'
---

## 概要

エージェントが自律的にゴールを追う時代では、スコープ設計が重要だという考察。書かれていない暗黙知は人間の専門家のフィードバックでしか渡せないため、フィードバックを集めやすいスコープとレビューUXに投資すべきと主張する。

## 設計のポイント

- エージェントの失敗の主因は文脈不足であり、特に未文書化の文脈は人間のフィードバックで補う設計にする。
- 最適化する指標（メトリクス）を明示し、方向違いによるトークンの浪費を防ぐ。
- エージェント成果物をレビューしやすいUXを整え、フィードバック収集の質と量を上げる。

## 使いどころ

- 広告最適化など主観的な判断を含む業務をエージェントに任せるチーム。
- 長時間走るゴール駆動型エージェントのスコープを決める設計者。
