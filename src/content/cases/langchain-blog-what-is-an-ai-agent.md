---
type: opinion
title: 『エージェント度』というスペクトラムでLLMシステムの自律性を捉える
title_original: What is an AI agent?
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- LangGraph
- LangSmith
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/what-is-an-agent
published_at: '2026-06-15'
---

## 概要

LangChainのHarrison Chaseは『エージェントかどうか』を二元的に論じるのではなく、LLMがどれだけ制御フローを決定するかで『エージェント度』のスペクトラムとして捉えるべきだと提案する。Router・State Machine・Autonomous Agentという段階を示し、エージェント度が上がるほどオーケストレーション基盤・耐久実行・観測性・評価の重要性が増すと論じる。

## 設計のポイント

- システムをRouter・State Machine・Autonomous Agentという自律性の段階として捉え、必要な設計投資を見積もる
- エージェント度が高いほど分岐とループを一級に扱えるオーケストレーションフレームワークが必要になる
- 長時間実行を前提にバックグラウンド実行と耐久実行（durable execution）を設計に組み込む
- 自律性が上がるほど、途中状態を観測・介入できる仕組みと専用の評価フレームワークが必要になる

## 使いどころ

- LLMシステムをどこまで自律的に設計すべきか判断したいアーキテクト
- エージェント基盤への投資（観測性・評価・オーケストレーション）の優先度を決めたいチーム
