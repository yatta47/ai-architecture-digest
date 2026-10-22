---
type: case
title: 非営利団体がAmazon Quickで経営層が直接データを探索する事例
title_original: How U.S. Hunger connects leaders and data using Amazon Quick
company: U.S. Hunger
industry: other
cloud:
- aws
patterns:
- business-intelligence-resilience
components:
- Amazon Quick
- SPICE
- SQL Server
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-u-s-hunger-connects-leaders-and-data-using-amazon-quick/
published_at: '2026-10-21'
---

## 概要

食料支援団体U.S. Hungerは、Amazon Quickで経営層が組織データを直接探索できるようにした。基幹データはSQL Serverから毎夜2時（東部時間）にSPICEへ取り込み、新たなデータ抽出を依頼せず疑問に沿って分析できる。共有定義に基づき、財務情報と支援世帯の状況を並べて見られる。

## 設計のポイント

- 技術チームがデータセットを準備し、経営層に必要な範囲だけを共有する。
- SPICEへの定期取り込みで、分析用のデータを日次で更新する。
- 部署で共有する定義を使い、同じ指標で議論できるようにする。

## 使いどころ

- 少人数で急成長しており、データ抽出の依頼待ちが意思決定の遅れになっている組織。
- 経営層がセルフサービスで質問を重ねたい非営利団体や中小組織。
