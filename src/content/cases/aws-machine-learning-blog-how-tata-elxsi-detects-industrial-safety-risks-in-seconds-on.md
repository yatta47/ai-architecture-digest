---
type: case
title: エッジとクラウドを分離したリアルタイム産業安全監視基盤IRIS
title_original: How Tata Elxsi detects industrial safety risks in seconds on AWS
company: Tata Elxsi
industry: manufacturing
cloud:
- aws
patterns:
- video-intelligence
- event-driven
components:
- AWS IoT Greengrass
- Amazon S3
- Amazon Kinesis Data Streams
- Amazon SageMaker AI
- NVIDIA Jetson AGX Orin
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-tata-elxsi-detects-industrial-safety-risks-in-seconds-on-aws/
published_at: '2026-09-22'
---

## 概要

Tata Elxsiは既存のカメラ網を録画専用から予防的な安全監視に転換するIRISを構築し、検知に15〜45分かかっていた不安全状態をリアルタイムに近い速度で検知できるようにした。エッジで映像を絞り込み、安全に関わるフレームとメタデータのみをクラウドへ送ることで、生映像をクラウドに流さずに済む設計にしている。

## 設計のポイント

- エッジでモーション検知と一次モデルでフィルタリングしクラウドへ送るフレーム量を70〜80%削減した
- 画像パス（S3）とメタデータパス（Kinesis）を分離しストリーミングイベントを1KB未満に保った
- PPE検出・立入禁止区域監視・行動分析をモデルファミリーごとに独立したSageMakerエンドポイントで提供しスケーリングを分離した
- データレジデンシーと低遅延のためムンバイリージョンで完結させる構成にした

## 使いどころ

- 既存のカメラインフラはあるが映像を実時間で活用できていない工場・倉庫・物流拠点
- シフトをまたいだ安全ポリシー遵守のばらつきを継続的な自動監視で均したい安全管理チーム
- カメラ台数の増加に比例して監視コストが増えない仕組みを求める場合
