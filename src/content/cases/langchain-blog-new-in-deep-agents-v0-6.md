---
type: announcement
title: Deep Agents v0.6が実現する低コストモデル運用と長時間実行エージェントの効率化
title_original: New in Deep Agents v0.6
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- context-engineering
- prompt-optimization
components:
- Deep Agents
- LangGraph
- LangSmith Context Hub
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/deep-agents-0-6
published_at: '2026-06-03'
---

## 概要

Deep Agents v0.6は、モデル層・エージェント層・スケール・時間経過という4つの軸でパフォーマンスを高める複数の機能を導入した。ハーネスプロファイルによりKimiやQwen、DeepSeekなどのオープンウェイトモデルでもクローズドなフロンティアAPIより20倍以上低コストで本番品質の性能を引き出せるほか、Delta Channelによりチェックポイントストレージを最大100倍削減し、コードインタープリタによるプログラム的なツール呼び出し（PTC）でモデルとの往復回数を減らす。あわせて型付きストリーミングとContextHubBackendによる永続的なスキル・ポリシー・メモリ管理も追加された。

## 設計のポイント

- コードインタープリタをエージェントループ内蔵の実行環境として提供し、ツール呼び出しの結果を一旦ランタイム状態に保持してから必要な部分だけをモデルに返すプログラム的ツール呼び出し（PTC）を可能にする
- モデルごとのツール呼び出し形式やプロンプト慣習の違いを吸収するハーネスプロファイルを導入し、オープンウェイトモデルでもハーネス側のチューニングだけでベンチマークスコアを10〜20ポイント押し上げる
- メッセージやツール呼び出し、サブエージェント、カスタムイベントを型付きで購読できるストリーミングプリミティブにより、フロントエンドが必要な情報だけを取得できるようにする
- スキル・ポリシー・メモリをLangSmith Context Hubにバージョン管理された形で保存し、あるセッションでの学習を次のセッションに引き継げるようにする

## 使いどころ

- クローズドなフロンティアモデルのAPIコストを抑えつつ本番品質のコーディングエージェントを運用したいチーム
- サブエージェントを使った再帰的な調査・要約ワークフローを、モデルとの往復を最小化しながら構築したい場合
- エージェントの実行状況やツール呼び出しをリアルタイムにフロントエンドへ反映するUIを構築したい開発者
- 長時間セッションにわたるチェックポイントストレージコストを抑えつつ、エージェントの再開性や監査可能性を維持したい基盤チーム
