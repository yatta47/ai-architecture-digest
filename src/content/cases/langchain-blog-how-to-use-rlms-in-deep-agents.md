---
type: case
title: LangChain Deep Agents、REPL上で動く再帰的サブエージェント委譲でコンテキスト崩壊を回避
title_original: How to Use RLMs in Deep Agents
company: LangChain
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- context-engineering
- parallel-execution
- reasoning-computation-separation
components:
- Deep Agents
- Claude Code
- GLM 5.2
- Nemotron
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-to-use-rlms-in-deep-agents
published_at: '2026-07-01'
---

## 概要

MIT CSAILが提案した再帰言語モデル(RLM)の考え方を取り入れ、LangChainはDeep Agentsに動的サブエージェント機能としてプログラム的なオーケストレーションを実装した。モデルがREPL上でコードを書いてサブエージェントを分岐・再帰的に呼び出すことで、長大な入力に対する逐次要約由来のコンテキスト崩壊を回避する。長文脈集計ベンチマークOOLONGでは、REPLを使わないエージェントに比べ128kトークンでスコアが0.44から0.79へ向上した。

## 設計のポイント

- コンテキストウィンドウ内でモデルに逐次カウントさせず、集計や反復処理などのオーケストレーションロジックはREPL上のコードとして実行し、モデルの一時的な文脈からコンテキスト崩壊のリスクを切り離す。
- サブエージェントへの処理委譲をツール呼び出しの逐次判断に任せず、for文などのコードで網羅させることで、モデルの判断に依存しない決定的なカバレッジを保証する。
- オーケストレーター役と各サブエージェント役に異なるモデル（フロンティアモデルとオープンウェイトモデルなど）を自由に組み合わせられる設計にし、コストと性能のバランスを用途ごとに最適化する。
- fan out and synthesize、classify and act、adversarial verification、generate and filter、tournament、loop until doneといった定型のプログラム的委譲パターンを語彙として整理し、タスクの形に応じて使い分けられるようにする。

## 使いどころ

- 数千件の通話記録から平均取引額を算出するような、単一のコンテキストウィンドウに収まらず逐次集計だとドリフトが生じる大規模データ集計タスク。
- 全件を漏れなく走査する必要がある分類・カウント処理など、モデルの自発的な判断だけでは網羅性を保証しにくいタスク。
- コスト最適化のためにフロンティアモデルとオープンウェイトモデルをオーケストレーター/サブエージェントで使い分けたいチーム。
- 文脈長が128kトークンを超えるあたりから精度が崩れたり処理を諦めてしまったりする、長文脈QA・分析ベンチマーク相当のワークロード。
