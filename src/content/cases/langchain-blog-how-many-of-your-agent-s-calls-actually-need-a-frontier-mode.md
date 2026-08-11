---
type: case
title: エージェント呼び出しの93%は軽量モデルで処理可能、NeMo Switchyardでコスト74%削減を実測
title_original: How many of your agent's calls actually need a frontier model?
company: LangChain
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- cost-optimization
- ai-agent
components:
- NVIDIA NeMo Switchyard
- NVIDIA Nemotron 3.5 Lightning
- Claude Opus 4.8
- Deep Agents
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/switchyard-agent-routing-benchmark
published_at: '2026-08-11'
---

## 概要

LangChainはDeep Agentsの評価スイート(145のマルチステップタスク)をNVIDIA NeMo Switchyardのエスカレーション型ルーティングに通し、フロンティアモデル(Claude Opus 4.8)へ実際にルーティングされたのはわずか7%のターンで、残り93%は30BパラメータのNemotron 3.5 Lightningで処理できることを計測した。ルーティングによりOpus単体運用比でコストを74%削減しつつ精度は6ポイントの低下にとどまったが、判定用の小型モデル(judge)がルーティング済みアームの支出の21.2%を占めるため、エスカレーション率だけでなくjudgeモデル自体の最適化も必要になる。

## 設計のポイント

- 全ターンを一律に最大モデルへ送るのではなく、まず軽量モデルで開始し悪化シグナルが連続したときのみ高性能モデルへ『片道』でエスカレーションする
- ルーティングの費用対効果は『judgeモデルのコスト÷2モデル間の価格差』で試算し、価格差が小さい場合はルーティングでは割に合わないと判断する
- ルーティングによる節約はタスクを賢いモデルに『寄せる』ことではなく、簡単なタスクを安いモデルに『逃がす』ことから生まれると理解する
- judgeモデルはプロンプトキャッシュの恩恵を受けにくいため、ルーティングコストの中でも別枠で最適化対象として扱う

## 使いどころ

- エージェントの呼び出しの大半が定型的な作業で、フロンティアモデルの精度が必ずしも必要ない場合
- モデルコストを削減しつつ許容できる精度低下幅を見積もりたいチーム
- 2つの候補モデルの価格差が十分大きい場合にのみルーティング投資を正当化したい場合
