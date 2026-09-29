---
type: guidance
title: AG-UIとエージェントスウォームで出力に適応するUIを作る
title_original: Build adaptive AI interfaces with the AG-UI protocol, agent swarms, and Nova Act on AWS
company: Amazon Web Services
industry: healthcare
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- human-in-the-loop
components:
- AG-UI protocol
- Strands Agents SDK
- Amazon Nova Act
- Amazon Bedrock
- AWS Lambda
- Amazon DynamoDB
- Amazon S3
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/build-adaptive-ai-interfaces-with-the-ag-ui-protocol-agent-swarms-and-nova-act-on-aws/
published_at: '2026-09-29'
---

## 概要

AIの出力が毎回変わるアプリで、固定レイアウトのUIでは対応しきれない問題に取り組む。AG-UIによる型付きイベントのSSEストリーミング、Strands Agentsのスウォームによる複数エージェントの合議、Nova Actによるレガシー画面操作を組み合わせ、医用画像レビューを例に示す。

## 設計のポイント

- エージェントとUIの契約をAG-UIの型付きイベントに標準化し、フレームワークを差し替えてもUI側を書き直さない。
- ピア型のスウォームで仮説を共有させ、合議の過程をUIに可視化して信頼性を高める。
- APIのないレガシーシステムはNova Actでブラウザ操作し、その様子をメインUIへストリーミングする。
- PHIを扱う場合は保存・通信の暗号化などの保護策を前提にする。

## 使いどころ

- AIの発見件数が案件ごとに大きく変わる画像診断・不正検知・法務レビューのUI開発者。
- 複数エージェントの議論過程をユーザーに見せたいプロダクトチーム。
- API連携できない既存業務システムをエージェントから操作したい組織。
