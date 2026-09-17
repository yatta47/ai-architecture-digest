---
type: case
title: 合成データで鍛える産業安全AIの人物検知モデル
title_original: Enhancing industrial safety AI with synthetic data on Amazon SageMaker AI
industry: manufacturing
cloud:
- aws
patterns:
- synthetic-data-generation
- cost-optimization
components:
- Amazon SageMaker AI
- Amazon Rekognition
- Qwen-Image-Edit-2509
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/enhancing-industrial-safety-ai-with-synthetic-data-on-amazon-sagemaker-ai/
published_at: '2026-09-17'
---

## 概要

重機周辺の危険な人物検知モデルは、危険すぎて撮影できない希少な事故寸前シーンの学習データ不足が課題となる。Amazon SageMaker AI上の拡散モデル(Qwen-Image-Edit-2509)で実写画像に人物を合成挿入し、Amazon RekognitionのDetectLabels APIで自動的にバウンディングボックスをラベル付けする2段階パイプラインにより、手動アノテーションや危険な撮影を行わずに人物検知のmAP50を最大160%改善した。

## 設計のポイント

- 完全な合成シーン生成ではなく実写画像への人物挿入編集にすることで、背景の忠実性を保ちドメインギャップを回避する。
- Rekognition DetectLabelsによる自動ラベリングとNMSによる重複除去で、1枚あたり3〜5ドルかかる手動アノテーションコストを削減する。
- 4基のGPUに分散した拡散モデル推論はデバイス間通信がボトルネックになるため、H100など単一の高VRAM GPUへの集約でコストを最大10分の1に抑える計画を示す。
- エッジ配置される軽量な検知モデル向けに、希少な高リスククラスのデータを重点的に増強する設計とする。

## 使いどころ

- 農業・建設・鉱業など自律機械を扱う現場で、人物と重機の危険な位置関係を検知するAIモデルを訓練したいチーム。
- 子供や作業員を危険な位置に立たせる撮影が倫理的・安全上できない、稀少な事故寸前シーンのデータ拡張が必要な場合。
- トラクターやフォークリフトなどエッジデバイスに搭載する軽量モデルで、希少クラスの検知精度を底上げしたいケース。
