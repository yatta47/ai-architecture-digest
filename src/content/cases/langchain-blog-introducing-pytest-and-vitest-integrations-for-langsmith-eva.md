---
type: announcement
title: 既存のpytest/vitestテスト資産をそのままLLM評価基盤にするLangSmith連携
title_original: Introducing Pytest and Vitest integrations for LangSmith Evaluations
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
components:
- LangSmith
- Pytest
- Vitest
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/pytest-and-vitest-for-langsmith-evals
published_at: '2026-08-26'
---

## 概要

LangSmithはPytestおよびVitest/Jestとの統合を提供し、既存のテスト実行フローのままLLMアプリの評価（eval）を実行できるようにした。テストケースの入出力・スコア・フィードバックをLangSmithに記録することで、単純な合否判定を超えて非決定的なLLM出力の品質推移を追跡し、チームで結果を共有できるようにしている。

## 設計のポイント

- LLMアプリの評価を既存のpytest/vitestのテスト実行フローにそのまま統合し、追加の学習コストなく導入できるようにした
- 合否だけでなく入出力・スコア・フィードバックをLangSmithに記録し、非決定的な出力の品質推移を時系列で追えるようにした
- LLMによる意味的な正誤判定（LLM-as-judge）をテストコード内に組み込み、自動採点できるようにした

## 使いどころ

- 既存のソフトウェアテスト基盤にLLM評価を組み込みたいチーム
- 非決定的なLLM出力の品質回帰を継続的に監視したいプロダクト
- ドメインエキスパートと評価結果を共有しながら改善したいチーム
