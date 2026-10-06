---
type: opinion
title: LLM判定なしでエージェントのトレースから検出できる失敗
title_original: What agent traces can tell you without an LLM judge
company: Arize
industry: cross-industry
cloud: []
patterns:
- eval
- ci-cd
- llmops
components:
- Arize Phoenix
- tracelint
- OpenInference
- LangGraph
outcome:
  type: quality
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/agent-traces-without-llm-judge/
published_at: '2026-10-06'
---

## 概要

エージェントの失敗には、トレースだけで証明できるもの（スキーマ違反、失敗結果を副作用に再利用等）がある。OSSのlintツールtracelintがOpenInferenceトレースにこれを決定的に検査し、CIの終了コードで返す考え方を紹介する。

## 設計のポイント

- 「意図の解釈が要るか」で判定をLLM評価と決定的チェックに振り分ける。
- ツールの性質（副作用の有無）を宣言し、トレースと突き合わせて検査する。
- 進捗なしの反復呼び出しは確定バグでなく候補として提示する。

## 使いどころ

- エージェントの挙動回帰をCIで安価に検出したい開発チーム。
- LLM判定のコストと揺れを減らしたい評価基盤。
