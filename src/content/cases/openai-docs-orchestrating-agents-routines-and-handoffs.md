---
type: guidance
title: ルーティンとハンドオフによるマルチエージェントオーケストレーション
title_original: 'Orchestrating Agents: Routines and Handoffs'
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
components:
- OpenAI API
- Swarm
outcome:
  type: reliability
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/orchestrating_agents/
published_at: '2024-10-10'
---

## 概要

自然言語の指示手順とツール群を組み合わせた「ルーティン」と、あるエージェントから別のエージェントへ制御を委譲する「ハンドオフ」という2つの概念を導入し、複数のエージェントをシンプルかつ制御可能にオーケストレーションする方法を示す。サンプル実装としてSwarmリポジトリを提供する。

## 設計のポイント

- エージェントの振る舞いをシステムプロンプト＋関数ツールの組として定義し、条件分岐を含む手順(ルーティン)として表現する
- タスクの性質に応じて別のルーティン(エージェント)へ処理を明示的にハンドオフする関数を用意し責務を分離する

## 使いどころ

- カスタマーサポートのように複数の対応フロー(トリアージ→修正提案→返金)が絡む会話エージェントを構築する場合
- 単一の巨大プロンプトでは制御しきれない複雑なマルチフローを役割ごとのエージェントに分割したい場合
