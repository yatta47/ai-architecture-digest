---
type: case
title: Adobe FireflyのGPU学習基盤をAmazon Managed Prometheusで28倍高速に監視する
title_original: 'Adobe Firefly: Simplified observability with Amazon Managed Prometheus'
company: Adobe
industry: media
cloud:
- aws
patterns:
- gpu-fleet-reliability
- llmops
components:
- Amazon EKS
- Amazon Managed Service for Prometheus
- Amazon Managed Grafana
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/adobe-firefly-simplified-observability-with-amazon-managed-prometheus/
published_at: '2026-08-13'
---

## 概要

Adobe FireflyのGPU学習基盤（Amazon EKS上で数千ノード・数万GPU規模）が抱えていた自己運用Prometheusのクエリ性能限界を、Amazon Managed Service for Prometheusへの段階移行で解決した事例。既存基盤と並行してmanaged scraperを導入し、クエリ性能を最大28.8倍高速化、監視可能な時間窓を6時間から24時間に拡大した。

## 設計のポイント

- 既存の自己運用Prometheusを置き換えず、Managed Service for Prometheusのmanaged scraperを並行導入して段階移行する
- GPU健全性・ジョブレベル・Pod/ノード状態などクリティカルな指標だけを厳選し、まず2Mタイムシリーズを移行して効果を最大化する
- エージェント不要のremote write構成で既存ワークフローへの変更を最小限に抑える

## 使いどころ

- 数千GPU規模の分散学習ジョブを運用し、高カーディナリティなメトリクスのクエリ性能に課題を抱えるMLインフラチーム
- 自己運用監視基盤の運用負荷を減らしつつ、長時間ジョブの全ライフサイクルを可視化したいプラットフォームチーム
