---
type: case
title: Data 360データグラフでAgentforceにP50 200ms未満の信頼できる顧客コンテキストを供給
title_original: How AI agents get trusted customer context with Data 360 data graphs
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- context-engineering
- data-federation
components:
- Salesforce Data 360
- Agentforce
outcome:
  type: speed
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-ai-agents-get-trusted-customer-context-with-data-360-data-graphs/
published_at: '2026-09-14'
---

## 概要

Salesforceのエンジニアリングチームは、断片化した顧客ID・製品・エンタイトルメント情報を統合するData 360データグラフを構築し、AgentforceのエージェントがテナントIDから一度のコールで信頼できる顧客コンテキストを取得できるようにした。アクセスパターンに基づいて適切な粒度のグラフに分割しインデックスを設計することで、パーソナライズされたエージェントコンテキストのP50パフォーマンスを約400msから200ms未満に改善。パーティション化されたアーキテクチャで顧客間のデータ混在を防ぎながら、6ヶ月で5つのデータグラフをリリースした。

## 設計のポイント

- アクセスパターンを先に理解し、大きすぎず小さすぎない適切な粒度でグラフを分割してインデックスを設計する
- パーティション化されたデータ空間で全体アイデンティティグラフとカスタマーサクセス向けのフィルタ済みビューを分離し、顧客間のデータ混在を防ぐ
- エージェントが未知の質問をしてくることを前提に、多対多関係をたどれるセマンティック/キーワード検索を組み込みグラフを異なる起点からも辿れるようにする

## 使いどころ

- 数十システムに散らばる顧客・製品・エンタイトルメント情報を統合しAIエージェントにリアルタイムで渡したい企業
- パーソナライズされたエージェント応答のためにミリ秒単位のレイテンシが求められるカスタマーサポート/カスタマーサクセス基盤
