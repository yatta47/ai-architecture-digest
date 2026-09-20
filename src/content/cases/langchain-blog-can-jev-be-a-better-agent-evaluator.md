---
type: case
title: 型付き回答を返す「System One」モデルJevでエージェント評価を高速・低分散化する
title_original: Can Jev Be a Better Agent Evaluator?
company: LangChain
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- ai-agent
components:
- LangSmith
- Deep Agents
- Jev
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/jev-agent-evals-langsmith
published_at: '2026-09-20'
---

## 概要

LangChainはDeep Agentsで構築したエージェントの実行結果をLangSmithのデータセットとして固定し、TypeSafe AIの「System One」モデルJevを新しいタイプのエージェント評価器としてGPT-5.6 Luna/Terra・Claude Sonnet 4.6によるLLM-as-a-judgeと比較検証した。Jevは自然文を生成せず選択・スコア・確率などの型付き回答を直接返す設計により、連続スコアの分散が既存LLM審査員より92〜913倍小さく、平均0.44秒・1回$0.00035という最速・最安の評価を実現し、二値の合否判定では人間オラクルと全件一致した。

## 設計のポイント

- LLM-as-a-judgeを自然文生成モデルに任せず、Choice/Score/Noulのような型付き質問に特化した決定モデルに置き換えることで、評価という決定タスクに最適化する。
- 同一のエージェント実行結果をLangSmithのデータセットとして固定し、複数の評価器に同一入力を100回繰り返し与えることで分散と精度を分離して計測する。
- 精度（人間オラクルとの一致）と再現性（同一入力に対する分散）を別軸で評価し、分散が低いだけでは正確さを保証しない点を踏まえて解釈する。
- 複数の型付き質問（選択・スコア・確率）を同じエージェント状態に対して並列に評価できる構成にする。

## 使いどころ

- LLM-as-a-judgeのレイテンシ・コスト・非決定性がボトルネックになっている継続的なエージェント評価パイプラインを運用するチーム。
- 本番トレースを大量かつ低コスト・低分散に継続監視したいLLMOps/Observability担当者。
- コードベース評価では捉えきれない開放的なエージェント応答を、型付き決定タスクとして扱いたいエージェント開発者。
