---
type: guidance
title: AIエージェントサンドボックスの実行基盤をトレースで検証してから移行を判断する設計
title_original: 'Trace before you migrate: Measuring Kubernetes bottlenecks in AI agent sandboxes'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- root-cause-analysis
components:
- Arize AX
- Phoenix
- Kubernetes
- Daytona
outcome:
  type: reliability
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/trace-before-you-migrate-measuring-kubernetes-bottlenecks-in-ai-agent-sandboxes/
published_at: '2026-07-09'
---

## 概要

AIエージェントはモデル呼び出しだけでなくファイル操作やシェル実行、サンドボックス起動など多くの処理を伴うが、多くのチームはモデル呼び出ししかトレースしておらず、Kubernetesが本当にボトルネックかどうかを誤診しやすい。記事はサンドボックスの作成・準備・コマンド実行・I/O・権限エラー・eval採点をエージェントの実行トラジェクトリのスパンとして計装することを提案し、ベンダーのベンチマークではなく自社のトレースに基づいてKubernetesか専用サンドボックスかを判断すべきだと説く。

## 設計のポイント

- モデル呼び出しに加えてサンドボックスの作成・準備・コマンド実行・I/O・権限エラー・eval採点をトレースのスパンとして計装する
- エージェントの応答遅延がモデルによるものかインフラのプロビジョニングや依存関係インストールによるものかを切り分けて計測する
- Kubernetesは制御プレーンや長時間稼働サービスには適するが、短命なエージェントサンドボックスの実行層としては構造的な摩擦が生じやすい
- 他社のベンチマーク数値は移行の根拠ではなく自社環境を計測するきっかけとして扱う

## 使いどころ

- コーディングエージェントやeval/RLワークロードなど要求されるサンドボックスの起動速度・分離境界が異なるチームの実行基盤選定
- エージェントの遅延原因がモデルかインフラかを切り分けたいプラットフォーム/オブザーバビリティチーム
- KubernetesからDaytonaのような専用サンドボックススケジューラへの移行を検討している組織の意思決定
