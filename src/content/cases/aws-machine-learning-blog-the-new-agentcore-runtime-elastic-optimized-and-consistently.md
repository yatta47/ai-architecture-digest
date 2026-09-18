---
type: announcement
title: 新AgentCore runtime：メモリを使用量に追随させコールドスタートを安定化
title_original: 'The new AgentCore runtime: Elastic, optimized, and consistently fast starts'
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- unified-runtime
- inference-optimization
components:
- Amazon Bedrock AgentCore
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/the-new-agentcore-runtime-elastic-optimized-and-consistently-fast-starts/
published_at: '2026-09-18'
---

## 概要

Amazon Bedrock AgentCore runtimeが刷新され、セッション終了までピーク時のメモリ確保を保持し続けていた従来方式から、使われなくなったメモリを即座に解放して課金に反映する方式へ変わった。あわせて環境スナップショットを再利用する起動方式により、コンテナサイズや同時実行数によらず一貫して高速なコールドスタートを実現する。

## 設計のポイント

- メモリはピーク確保のまま保持せず、コールドになった時点で解放し課金対象から外すことでバースト後の待機コストを減らす
- 起動のたびにブート・初期化をやり直す代わりに、準備済み環境のスナップショットを復元することでコールドスタート時間をイメージサイズや同時実行数に依存させない
- サーバーレスのスケールtoゼロと従量課金というモデルを維持したまま、対話型の短命セッションと長時間稼働するアンビエントなエージェントの両方に対応させる

## 使いどころ

- 数時間にわたり監督なしで稼働し続けるアンビエント／自律的なエージェントを運用するチーム
- ユーザーが入力待ちで一時停止したセッションの再開時に、一貫した低レイテンシな起動を求めるインタラクティブなエージェント
- コールドスタート回避のために予備環境を自前で維持するコストと複雑さを避けたいプラットフォームチーム
