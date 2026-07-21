---
type: case
title: 単一ReActエージェントはどこまでツール・指示を詰め込めるか検証したベンチマーク
title_original: Benchmarking Single Agent Performance
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- context-engineering
components:
- LangGraph
- LangSmith
- o1
- o3-mini
- Claude 3.5 Sonnet
- GPT-4o
- Llama 3.3 70B
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/react-agent-benchmarking
published_at: '2026-06-30'
---

## 概要

LangChainチームは、社内のメール対応エージェント（カレンダー調整とカスタマーサポートの2ドメインを担当）を題材に、単一のReActエージェントに与える指示とツールの数を増やしていくと性能がどう変化するかをベンチマークした。ツール呼び出しの軌跡とLLM-as-judgeによる出力評価の両面でスコアリングし、コンテキストとツール数の増加がいずれも性能を低下させることを確認した。o1・o3-mini・Claude 3.5 Sonnetはgpt-4oやLlama 3.3 70Bより頑健だが、o3-miniはコンテキストが増えると性能低下が大きいという結果も得られた。

## 設計のポイント

- エージェントの責務を『ドメイン』単位（指示+ツール群）に分割し、段階的に負荷を増やして劣化点を特定する
- ツール呼び出し軌跡の一致度とLLM-as-judgeによる出力品質の両方で合否を判定する
- 長い実行トラジェクトリを要するタスクほどコンテキスト増加による性能劣化が大きい点を踏まえてアーキテクチャを選ぶ
- モデル選定では単純な性能比較だけでなく、コンテキスト増加時の劣化耐性も評価軸に加える

## 使いどころ

- 単一エージェントに機能を継ぎ足す前に、どこまでツール・指示を持たせられるか事前検証したいチーム
- マルチエージェント化すべきか単一エージェントで十分かを判断する材料が欲しい設計者
- カスタマーサポートや社内アシスタントなど、複数ドメインを1つのエージェントに担わせる設計を検討している場合
