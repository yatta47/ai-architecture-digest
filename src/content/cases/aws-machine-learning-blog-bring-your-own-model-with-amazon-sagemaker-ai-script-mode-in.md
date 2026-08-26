---
type: guidance
title: SageMaker SDK v3のModelTrainer/ModelBuilderで実現するコンテナ非依存の独自モデル学習・配信
title_original: 'Bring your own model with Amazon SageMaker AI: Script mode in SDK v3'
industry: cross-industry
cloud:
- aws
patterns:
- unified-runtime
- fine-tuning
components:
- Amazon SageMaker AI
- Amazon SageMaker Python SDK v3
- Amazon ECR
- Amazon S3
- DJL Serving
- Hugging Face Accelerate
- Stable Diffusion 3.5
- MLflow
- AWS Deep Learning Containers
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/bring-your-own-model-with-amazon-sagemaker-ai-script-mode-in-sdk-v3/
published_at: '2026-08-26'
---

## 概要

Amazon SageMaker Python SDK v3は、フレームワークごとに分かれていたEstimator/Model系クラスをModelTrainer（学習）とModelBuilder（デプロイ）という単一APIに統合した。SourceCodeオブジェクトによりローカルの学習・推論コードをジョブ実行時にコンテナへ同期する方式となり、コンテナイメージの再ビルドなしにコード変更を反映できる。scikit-learnのRandom ForestとStable Diffusion 3.5のLoRAファインチューニングという2つの実例で、この仕組みを解説している。

## 設計のポイント

- SourceCodeオブジェクト（source_dir + command/entry_scriptで指定）を使い、学習・推論コードをコンテナイメージから分離し実行時にジョブへ同期することで、コード変更のたびにDockerイメージを再ビルドせずに済む設計にしている。
- 学習用コンテナはランタイムとフレームワークライブラリのみを含む最小構成とし、アルゴリズム固有のコードはsource_dirに置くことで、同じコンテナを複数のモデル・実験で使い回せるようにしている。
- ModelTrainerとModelBuilderという単一クラスにより、scikit-learn・PyTorch・Stable Diffusion・独自C++推論バイナリなど異なるフレームワークでも同一のAPIで学習・デプロイを扱えるようにしている。
- 自前でビルドしたイメージ、AWS Deep Learning Container、サードパーティイメージのいずれも学習コンテナとして利用可能にし、必要に応じてSageMaker上のフルマネージドMLflowで実験・メトリクス・モデル成果物を追跡できるようにしている。

## 使いどころ

- 学習・推論スクリプトを頻繁に変更しながら、そのたびにコンテナイメージを再ビルドしたくないMLエンジニアリングチーム。
- CUDAライブラリや独自システムパッケージなどコンテナ内部を細かく制御したいが、SageMakerのマネージド学習基盤は使い続けたいチーム。
- scikit-learn・PyTorch・XGBoost・生成AIモデルなど複数フレームワークに散らばっていたSageMaker利用コードを、単一のAPIパターンに統一・標準化したいチーム。
