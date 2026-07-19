---
type: case
title: kagentが辿り着いたAIエージェント向け実行基盤「agent-substrate」
title_original: Is a Pod the right deployment unit for an AI agent?
company: Solo.io
industry: cross-industry
cloud: []
patterns:
- ai-agent
- unified-runtime
components:
- kagent
- Kubernetes
- agent-substrate
- gVisor
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/14/is-a-pod-the-right-deployment-unit-for-an-ai-agent/
published_at: '2026-07-14'
---

## 概要

Solo.ioのkagentプロジェクトは、AIエージェントを1体ずつKubernetes Podとして常駐させる設計が、短命でバースト的なエージェントの実行パターンと合わず無駄が生じることに直面。Pod上に「agent-substrate」という追加の制御プレーンを導入し、実行基盤(Worker)と論理的なエージェント(Actor)を分離した。

## 設計のポイント

- WorkerPool/ActorTemplateというKubernetesライクな抽象を導入し、PodはWorker(実行基盤)、Actorは論理的なエージェント単位として分離する。
- Actorはワーク到着時にWorkerへスケジュールされ完了後に解放される軽量な実行単位とし、Pod常駐によるリソース浪費を避ける。
- gVisorなどのサンドボックスでActor実行を隔離しつつ、Kubernetesのネットワーク・セキュリティ・スケジューリング機構をそのまま活用する。

## 使いどころ

- 大量の短命・バースト的なAIエージェントをKubernetes上で効率よく収容したいプラットフォームチーム。
- エージェントごとにPodを常駐させるとリソースが無駄になる規模のマルチエージェント基盤。
