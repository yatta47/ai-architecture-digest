---
type: guidance
title: カナダのRegionからOpenAI GPTをBedrockのクロスRegion推論で使う
title_original: Access OpenAI GPT models on Amazon Bedrock from Canada with cross-Region inference
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- cost-optimization
components:
- Amazon Bedrock
- Cross-Region Inference
- OpenAI GPT-6.1
- AWS IAM
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/access-openai-gpt-models-on-amazon-bedrock-from-canada-with-cross-region-inference/
published_at: '2026-10-20'
---

## 概要

Amazon BedrockのクロスRegion推論(CRIS)により、カナダの2 RegionからOpenAI GPT-5.6/6/6.1を呼び出せるようになった。推論プロファイルを指定するだけで宛先Regionへのルーティングと容量確保をBedrockが担う。

## 設計のポイント

- 推論プロファイル(us./global.)をモデルIDの代わりに指定し、宛先Regionのルーティングをアプリから切り離す。
- データ所在要件に応じて、北米内に閉じるUS地域プロファイルとglobalプロファイルを使い分ける。
- Responses API・Chat Completions・Converseの複数APIで同じモデルを呼べ、既存コードを流用できる。

## 使いどころ

- データ所在地の規制があるカナダ企業が最新モデルを利用する場面。
- 需要スパイク時のスループットを広い容量プールで吸収したいワークロード。
