---
type: case
title: Salesforce、SageMaker推論コンポーネントのマルチAZ配置でAgentforceの高可用性を確保
title_original: 'Spreading the load: How Salesforce met Multi-AZ HA with SageMaker Inference Components'
company: Salesforce
industry: cross-industry
cloud:
- aws
patterns:
- gpu-fleet-reliability
- inference-optimization
- cost-optimization
components:
- Amazon SageMaker AI
- SageMaker Inference Components
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/spreading-the-load-how-salesforce-met-multi-az-ha-with-sagemaker-inference-components/
published_at: '2026-08-28'
---

## 概要

SalesforceはAgentforceのGPU推論コストをSageMaker Inference Components(IC)による複数モデルの共有GPU配置で8倍削減したが、デフォルトの配置ロジックではAZ間の偏りが生じ、2AZ必須というコンプライアンス要件を満たせなかった。新しいSchedulingConfigのAvailabilityZoneBalanceとPlacementStrategy(SPREAD)を使い、コピーをAZ間で均等配置しつつ、単一インスタンス障害からも分離する構成に変更した。

## 設計のポイント

- PlacementStrategyをSPREADにし、同一モデルのコピーをできるだけ多くのインスタンスに分散して単一障害点を避ける
- AvailabilityZoneBalanceのMaxImbalanceでAZ間コピー数の許容差を制御し、HAクリティカルなモデルはCopyCount1を避ける
- ScaleInPolicyをCONSOLIDATION戦略にして、スケールイン後もAZバランスを保ちながらアイドルインスタンスを解放する
- スケールアウト/インの際もSchedulingConfigの制約を保持し、モデル更新時もマルチAZ配置を維持する

## 使いどころ

- GPU共有によるコスト最適化と、2AZ以上でのコンプライアンス要件を両立させたい規制業界のML推論基盤
- 多数の小型モデルを1つのSageMakerエンドポイントに同居させ、単一インスタンス障害の影響範囲を限定したい場合
- 頻繁なスケールイン/アウトを行う推論ワークロードでAZバランスを維持したい運用チーム
