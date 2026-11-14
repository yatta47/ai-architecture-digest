---
type: case
title: AssemblyAIがECS+EC2 Spot+SQSで音声認識GPU推論のコストを下げた構成
title_original: Cost-optimizing AssemblyAI speech-to-text inference on AWS with Amazon EC2 Spot
company: AssemblyAI
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- inference-optimization
- realtime-transcription
components:
- Amazon ECS
- Amazon EC2 Spot
- Amazon SQS
- NVIDIA GPU
- AWS Marketplace
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/cost-optimizing-assemblyai-speech-to-text-inference-on-aws-with-amazon-ec2-spot/
published_at: '2026-11-13'
---

## 概要

AssemblyAIは音声認識の推論をECSキャパシティプロバイダでSpotとOn-Demandを混在させ、複数GPUファミリーで分散し、SQSの再試行キューで中断を吸収する構成にした。SLAを保ちつつ欧州リージョンのデータ居住要件にも対応している。

## 設計のポイント

- ECSキャパシティプロバイダでSpotとOn-Demandを混在させ、可用性の下限を確保する。
- 複数のGPUインスタンスファミリーに分散してSpot枯渇・中断の影響を減らす。
- SQSによる再試行で2分前通知の中断時も処理を失わない。

## 使いどころ

- GPU推論を大規模に常時運用しコストを下げたいAI SaaS事業者。
- データ居住要件のある規制業種向けに地域内で推論を回す場合。
