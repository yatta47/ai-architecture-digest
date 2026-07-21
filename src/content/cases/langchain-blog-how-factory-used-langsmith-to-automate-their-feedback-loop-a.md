---
type: case
title: SDLC自動化AI『Factory』がLangSmithでフィードバックループを自動化しイテレーション2倍化
title_original: How Factory used LangSmith to automate their feedback loop and improve iteration speed by 2x
company: Factory
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- prompt-optimization
- human-in-the-loop
components:
- LangSmith
- AWS CloudWatch
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/customers-factory
published_at: '2026-06-16'
---

## 概要

SDLC自動化AIプラットフォームのFactoryが、自社エージェント『Droid』のフィードバックループをLangSmithで自動化。LLM呼び出しをCloudWatchログと紐付けて可観測性を確保し、Feedback APIでコメント単位のフィードバックをプロンプト改善に直結させることで、イテレーション速度を2倍、コードマージまでの時間を平均20%短縮した。

## 設計のポイント

- LLM呼び出しの各ステップをCloudWatchログと紐付け、エージェントパイプライン内の位置を正確に追跡できるようにする
- コメントへのポジティブ/ネガティブフィードバックをFeedback APIで各LLM呼び出しに直接紐付け、データセット化して継続的に分析する
- フィードバックから『なぜ悪い出力になったか』をLLM自身に推論させ、プロンプト改善のヒントを自動生成する

## 使いどころ

- 自社ホスティングが必須なセキュリティ要件の厳しい環境でLLM可観測性を導入したい場合
- 手動でのプロンプト改善サイクルを自動化しイテレーション速度を上げたい開発チーム
