---
type: announcement
title: Amazon BedrockでGLM 5.3が利用可能に
title_original: Introducing GLM 5.3 on Amazon Bedrock
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- ai-agent
- multi-model-routing
components:
- Amazon Bedrock
- GLM 5.3
- Strix
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-glm-5-3-on-amazon-bedrock/
published_at: '2026-10-05'
---

## 概要

Z.aiの753Bパラメータ・MoEモデルGLM 5.3がBedrockで提供開始。OpenAI互換API、クロスリージョン推論、プロンプトキャッシュ、サービスティアを使え、OSSのAIペネトレーションテストエージェントStrixでの活用例も示される。

## 設計のポイント

- OpenAI互換APIで既存クライアントから切り替えやすくする。
- プロンプトキャッシュで長期エージェントのコストと遅延を下げる。
- クロスリージョン推論プロファイルで容量と可用性を確保する。

## 使いどころ

- コーディングや長時間エージェントにオープンウェイトモデルを自前運用なしで使いたいチーム。
- 自社アプリの認可済みセキュリティテストを自動化したい場面。
