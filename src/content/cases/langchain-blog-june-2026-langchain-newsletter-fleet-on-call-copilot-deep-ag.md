---
type: announcement
title: LangSmithアップデート：オンコール対応コパイロットと仮想コンピュータ操作でエージェント運用を強化
title_original: 'Newsletter June 2026: LangChain Newsletter'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- eval
- llmops
components:
- LangSmith
- LangGraph
- Fleet
- Deep Agents
- Pipecat
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/june-2026-langchain-newsletter
published_at: '2026-06-26'
---

## 概要

LangChainは2026年6月のニュースレターで、LangSmithにアラート対応を代行するオンコールコパイロットや、隔離仮想コンピュータ上でのツール操作、音声トレースのデバッグUIなど複数の新機能を発表した。あわせてDeep Agentsが基準に基づき自己評価を繰り返すRubricMiddlewareや、コードからサブエージェントを起動して並列処理するProgrammatic Subagentsといったオープンソース機能も紹介されている。導入事例としてBoxとHarmonicが挙げられ、いずれもエージェント改善のイテレーション速度が3〜4倍になったと報告されている。

## 設計のポイント

- アラートのトリアージや一次対応の下書きはコパイロットに任せつつ、最終判断・送信は人間が確認するHuman-in-the-loopの設計にする
- エージェントにコード実行やAPI呼び出しをさせる際は、隔離された仮想コンピュータ環境に閉じ込めて安全性と権限管理を両立させる
- RubricMiddlewareのように基準ベースの自己評価をエージェントの実行ループに組み込み、基準を満たすまで反復させて品質を担保する
- サブエージェントの起動をインタプリタのコードから直接呼び出せるようにし、タスクを分割・並列実行してから結果を統合する

## 使いどころ

- 本番運用中のエージェントの障害トリアージや一次対応を効率化したいSRE・オンコール担当者
- 音声エージェントの応答品質をデバッグしたい開発者が、トレース上で問題のあった発話区間を素早く特定したい場面
- 複数ステップの調査・分析・レポート作成タスクをサブエージェントに分担させ並列処理したい開発チーム
- ローカルで動作確認したエージェントを本番スケールで安定運用したい、デプロイと監視を担う運用チーム
