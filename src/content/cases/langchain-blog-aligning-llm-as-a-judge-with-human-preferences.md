---
type: case
title: 人間の修正をフィードバックするLLM-as-a-Judgeの自己改善評価器
title_original: Aligning LLM-as-a-Judge with Human Preferences
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- human-in-the-loop
- llmops
components:
- LangSmith
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/aligning-llm-as-a-judge-with-human-preferences
published_at: '2026-06-15'
---

## 概要

LangSmithはLLM-as-a-Judge型の評価器に、人間による修正結果をfew-shot例として自動的に蓄積し次の評価プロンプトへ反映する『自己改善』機構を追加した。これにより評価者プロンプトを手動でチューニングし続けなくても、人間の判断基準に評価が徐々に整合していく。

## 設計のポイント

- 人間による評価修正をそのままfew-shot例として保存し、以後の評価プロンプトに自動挿入する
- オンライン評価とオフライン評価の両方に同じ自己改善の仕組みを適用する
- 修正理由の説明文もあわせて保存し、プロンプトの文脈として活用できるようにする

## 使いどころ

- RAGの幻覚や正確性など、ルールベースでは測りにくい品質をLLMに評価させたいチーム
- 評価者プロンプトのチューニングに時間を取られたくない開発チーム
- 人間のレビューを評価システムの改善に継続的に還元したい運用フェーズのプロダクト
