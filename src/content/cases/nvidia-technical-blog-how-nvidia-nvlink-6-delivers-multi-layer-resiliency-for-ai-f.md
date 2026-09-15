---
type: case
title: 多層レジリエンシで大規模AIクラスタのパケットロスと障害復旧時間をゼロに近づける設計
title_original: How NVIDIA NVLink 6 Delivers Multi-Layer Resiliency for AI Factories
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- disaster-recovery
components:
- NVIDIA NVLink 6
- NVIDIA Vera Rubin NVL72
- NVIDIA Dynamo
- NMX Controller
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-nvidia-nvlink-6-delivers-multi-layer-resiliency-for-ai-factories/
published_at: '2026-09-15'
---

## 概要

NVIDIA NVLink 6は物理層でのForward Error CorrectionとPhysical Layer Retry、UPHY回復に加えクレジットベースのフロー制御でパケットロスをゼロにし、NMX Controllerの冗長化で管理系CPUリセット中もデータプレーンを維持する多層レジリエンシスタックを実現。NVIDIA DynamoのShadow Engine Recoveryは事前ウォームアップ済みレプリカでB200 GPUの推論復旧を283秒から7.3秒に短縮。

## 設計のポイント

- 物理層でのFEC+PLR+UPHY回復とリンク層でのクレジットベースフロー制御を組み合わせパケットロスを設計上ゼロにする
- 冗長スイッチトレイと分散NMX Controllerでゼロ単一障害点を実現し、管理系リセット中もデータプレーンを維持する
- 事前ウォームアップ済みレプリカプロセス(Shadow Engine Recovery)でコールドリスタートより桁違いに高速な障害復旧を行う

## 使いどころ

- 数万GPU規模の学習クラスタでトランジェントなリンク障害による集合通信の中断を避けたいAIファクトリー運用者
- 推論サービスのダウンタイムを最小化し継続的なリクエスト処理を維持したい大規模推論基盤チーム
