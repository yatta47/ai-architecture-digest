---
type: guidance
title: RayとAnyscaleでEC2上の分散AIワークロードを拡張
title_original: Scale distributed AI workloads with Ray and Anyscale on Amazon EC2
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- parallel-execution
- cost-optimization
components:
- Ray
- Anyscale
- Amazon EC2
outcome:
  type: cost
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/scale-distributed-ai-workloads-with-ray-and-anyscale-on-amazon-ec2/
published_at: '2026-11-12'
---

## 概要

マルチモーダルAI/MLパイプラインをRayとAnyscaleでEC2上に展開する方法を示す。3つのコンピュート選択肢、工程ごとの異種インスタンス適合によるコスト最適化、コード変更なしの本番スケールを扱う。

## 設計のポイント

- Ray Coreの分散プリミティブを基盤に、AIライブラリを重ねる。
- パイプライン工程ごとにインスタンスタイプを変えてコストを抑える。
- 単一インスタンスから分散環境へコードを書き換えず拡張する。

## 使いどころ

- テキスト・動画・音声を扱うパイプラインを分散化したいAIエンジニア。
- 学習・微調整・推論のコストを一元管理したい基盤チーム。
